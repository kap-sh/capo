"""Iterator helpers used by generated streaming operations.

Hand-written, not regenerated.
"""

from __future__ import annotations

from collections.abc import AsyncIterable, AsyncIterator, Callable, Iterable, Iterator
from typing import Generic, TypeVar, cast

T = TypeVar("T")
U = TypeVar("U")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]):
    """A type that is both a synchronous and asynchronous iterator.

    Streaming output fields use this so the same TypedDict type works for
    both sync and async operation variants.
    """

    ...


class StaticAnyIterator(AnyIterator[T], Generic[T]):
    """An :class:`AnyIterator` backed by static, in-memory content.

    Used when streaming output is produced from already-materialized bytes
    rather than a live stream. The ``content`` is yielded once and remains
    accessible as a public attribute.
    """

    def __init__(self, content: T) -> None:
        self.content = content
        self._consumed = False

    def __next__(self) -> T:
        if self._consumed:
            raise StopIteration
        self._consumed = True
        return self.content

    async def __anext__(self) -> T:
        if self._consumed:
            raise StopAsyncIteration
        self._consumed = True
        return self.content


def map_sync_iterator(iterable: Iterable[T], fn: Callable[[T], U]) -> Iterator[U]:
    """Map ``fn`` over a synchronous iterable, yielding results lazily."""
    for item in iterable:
        yield fn(item)


async def map_async_iterator(
    async_iterable: AsyncIterable[T], fn: Callable[[T], U]
) -> AsyncIterator[U]:
    """Map ``fn`` over an asynchronous iterable, yielding results lazily."""
    async for item in async_iterable:
        yield fn(item)


def chain_sync_iterator(*iterables: Iterable[T]) -> Iterator[T]:
    """Yield items from each iterable in order."""
    for iterable in iterables:
        yield from iterable


async def chain_async_iterator(
    prefix: Iterable[T], rest: AsyncIterable[T]
) -> AsyncIterator[T]:
    """Yield the synchronous ``prefix`` items, then the async ``rest`` items."""
    for item in prefix:
        yield item
    async for item in rest:
        yield item


def ensure_async_iterator(value: AsyncIterator[T] | T) -> AnyIterator[T]:
    """Return ``value`` as an :class:`AnyIterator`.

    An async iterator is returned unchanged; a single value is wrapped in a
    fresh single-item async iterator.
    """
    if isinstance(value, AsyncIterator):
        return cast(AnyIterator[T], value)

    return StaticAnyIterator(value)


def ensure_sync_iterator(value: Iterator[T] | T) -> AnyIterator[T]:
    """Return ``value`` as an :class:`AnyIterator`.

    A sync iterator is returned unchanged; a single value is wrapped in a
    fresh single-item sync iterator.
    """
    if isinstance(value, Iterator):
        return cast(AnyIterator[T], value)

    return StaticAnyIterator(value)


__all__ = [
    "AnyIterator",
    "StaticAnyIterator",
    "chain_async_iterator",
    "chain_sync_iterator",
    "ensure_async_iterator",
    "ensure_sync_iterator",
    "map_async_iterator",
    "map_sync_iterator",
]
