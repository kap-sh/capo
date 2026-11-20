"""Request body abstraction for streaming operations.

Hand-written, not regenerated.
"""

from __future__ import annotations

import os
from collections.abc import AsyncIterator, Callable, Iterator
from contextlib import (
    AbstractAsyncContextManager,
    AbstractContextManager,
    asynccontextmanager,
    contextmanager,
)
from typing import TYPE_CHECKING, Generic, TypeVar, Union, cast

from ._iter import AnyIterator

if TYPE_CHECKING:
    import anyio
else:
    try:
        import anyio
    except ImportError:
        anyio = None

_CHUNK_SIZE = 64 * 1024

TStream = TypeVar("TStream", Iterator[bytes], AsyncIterator[bytes])

# The opener yields the fresh stream together with its length, or ``None`` when
# no stream could be produced (an exhausted or non-rewindable source, or logic
# that decides dynamically it cannot reopen). Pairing the length with each open
# lets it change between rebuilds instead of being fixed for the whole body.
_ContextManager = Union[
    AbstractContextManager[Union[tuple[TStream, int], None]],
    AbstractAsyncContextManager[Union[tuple[TStream, int], None]],
]


class Body(AnyIterator[bytes], Generic[TStream]):
    """A replayable request body whose length travels with each open.

    A plain ``Iterator[bytes]`` can be sent only once, so a failed request
    cannot be retried. A ``Body`` instead holds an *opener* — a context manager
    that opens a fresh stream over the same source — and rebuilds the stream
    before every attempt, closing whatever was left of the previous one.

    ``TStream`` is ``Iterator[bytes]`` for bodies built with :meth:`from_path`
    and ``AsyncIterator[bytes]`` for :meth:`async_from_path`; the former use
    ``rebuild()``/``close()``, the latter ``arebuild()``/``aclose()``.
    ``build_request`` rebuilds before every attempt.

    Each open produces ``(stream, length)`` together, so the length is not bound
    to the whole body and may differ from one rebuild to the next. A rebuild is
    also not guaranteed to succeed: the source may be exhausted or
    non-rewindable, so the opener can yield ``None`` and :meth:`rebuild` then
    returns ``None`` instead of a pair. Callers check the return value::

        for attempt in range(max_attempts):
            opened = body.rebuild()
            if opened is None:
                raise RuntimeError("body could not be rebuilt")
            stream, length = opened
            send(stream, length)

    ``length`` also holds the current stream's length as an attribute (``None``
    before the first rebuild). Iterating a ``Body`` reads its current stream.
    """

    def __init__(self, opener: Callable[[], _ContextManager[TStream]]) -> None:
        self._opener = opener
        self._cm: _ContextManager[TStream] | None = None
        self._stream: TStream | None = None
        self.length: int | None = None

    @classmethod
    def from_path(
        cls, path: str | os.PathLike[str], chunk_size: int = _CHUNK_SIZE
    ) -> Body[Iterator[bytes]]:
        """A body that reads ``path`` in ``chunk_size`` chunks, reopening it (and re-measuring it) on every rebuild."""

        @contextmanager
        def open_() -> Iterator[tuple[Iterator[bytes], int]]:
            with open(path, "rb") as file:
                length = os.fstat(file.fileno()).st_size
                yield iter(lambda: file.read(chunk_size), b""), length

        return Body(open_)

    @classmethod
    def async_from_path(
        cls, path: str | os.PathLike[str], chunk_size: int = _CHUNK_SIZE
    ) -> Body[AsyncIterator[bytes]]:
        """The async counterpart of :meth:`from_path`; needs ``anyio`` installed."""
        if anyio is None:
            dist = (__package__ or "capo").replace("_", "-")
            raise RuntimeError(
                "Body.async_from_path() requires the anyio package; "
                f"reinstall with the anyio feature enabled: {dist}[anyio]"
            )

        @asynccontextmanager
        async def open_() -> AsyncIterator[tuple[AsyncIterator[bytes], int]]:
            async with await anyio.open_file(path, "rb") as file:
                length = os.fstat(file.wrapped.fileno()).st_size

                async def chunks() -> AsyncIterator[bytes]:
                    while chunk := await file.read(chunk_size):
                        yield chunk

                yield chunks(), length

        return Body(open_)

    @property
    def stream(self) -> TStream | None:
        """The current open stream, or ``None`` if none is open (before the first
        rebuild, or after a close).

        ``build_request`` reuses a non-``None`` stream instead of rebuilding, so
        the retry layer stays in control of when a fresh stream is created.
        """
        return self._stream

    def rebuild(self: Body[Iterator[bytes]]) -> tuple[Iterator[bytes], int] | None:
        """Reopen the stream, closing any previous one, and return ``(stream, length)``.

        ``None`` if the source could not be reopened.
        """
        self.close()
        cm = self._opener()
        if not isinstance(cm, AbstractContextManager):
            raise TypeError(
                "this Body has an async opener; use it with the async client (arebuild/aclose)"
            )
        cm = cast(AbstractContextManager["tuple[Iterator[bytes], int] | None"], cm)
        opened = cm.__enter__()
        if opened is None:
            cm.__exit__(None, None, None)
            return None
        stream, length = opened
        self._stream, self.length, self._cm = stream, length, cm
        return stream, length

    async def arebuild(
        self: Body[AsyncIterator[bytes]],
    ) -> tuple[AsyncIterator[bytes], int] | None:
        """Async :meth:`rebuild`, returning ``(stream, length)`` or ``None``."""
        await self.aclose()
        cm = self._opener()
        if not isinstance(cm, AbstractAsyncContextManager):
            raise TypeError(
                "this Body has a sync opener; use it with the sync client (rebuild/close)"
            )
        cm = cast(
            AbstractAsyncContextManager["tuple[AsyncIterator[bytes], int] | None"], cm
        )
        opened = await cm.__aenter__()
        if opened is None:
            await cm.__aexit__(None, None, None)
            return None
        stream, length = opened
        self._stream, self.length, self._cm = stream, length, cm
        return stream, length

    def close(self: Body[Iterator[bytes]]) -> None:
        cm, self._cm, self._stream, self.length = self._cm, None, None, None
        if cm is not None:
            cast(AbstractContextManager[object], cm).__exit__(None, None, None)

    async def aclose(self: Body[AsyncIterator[bytes]]) -> None:
        cm, self._cm, self._stream, self.length = self._cm, None, None, None
        if cm is not None:
            await cast(AbstractAsyncContextManager[object], cm).__aexit__(
                None, None, None
            )

    def __next__(self) -> bytes:
        if self._stream is None:
            raise RuntimeError("body has no open stream; call rebuild() first")
        return next(cast(Iterator[bytes], self._stream))

    async def __anext__(self) -> bytes:
        if self._stream is None:
            raise RuntimeError("body has no open stream; call rebuild() first")
        return await cast(AsyncIterator[bytes], self._stream).__anext__()


@contextmanager
def closing_bodies(inp: object) -> Iterator[None]:
    """Close every :class:`Body` in a request input when the operation finishes.

    The operation method wraps its whole run (request build across retries, plus
    response handling) in this, so a ``Body``'s stream is released once — and only
    once — the operation is done. Non-``Body`` values (bytes, plain iterators,
    ``StaticAnyIterator``) are left untouched.
    """
    try:
        yield
    finally:
        if isinstance(inp, dict):
            for value in inp.values():
                if isinstance(value, Body):
                    cast("Body[Iterator[bytes]]", value).close()


@asynccontextmanager
async def aclosing_bodies(inp: object) -> AsyncIterator[None]:
    """Async :func:`closing_bodies`, awaiting :meth:`Body.aclose`."""
    try:
        yield
    finally:
        if isinstance(inp, dict):
            for value in inp.values():
                if isinstance(value, Body):
                    await cast("Body[AsyncIterator[bytes]]", value).aclose()


__all__ = ["Body", "aclosing_bodies", "closing_bodies"]
