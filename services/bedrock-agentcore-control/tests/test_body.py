"""Body: replayable streaming request bodies."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator
from contextlib import asynccontextmanager, contextmanager
from pathlib import Path

import pytest

from capo_bedrock_agentcore_control._body import Body
from capo_bedrock_agentcore_control._iter import AnyIterator, ensure_async_iterator, ensure_sync_iterator


@pytest.fixture
def data_file(tmp_path: Path) -> Path:
    path = tmp_path / "data.bin"
    path.write_bytes(b"0123456789" * 3)
    return path


def test_from_path_reads_in_chunks(data_file: Path) -> None:
    body = Body.from_path(data_file, chunk_size=10)
    assert body.length is None  # not known until the first open
    opened = body.rebuild()
    assert opened is not None
    stream, length = opened
    assert length == 30
    assert body.length == 30
    assert list(stream) == [b"0123456789"] * 3
    body.close()
    assert body.length is None  # cleared on close


def test_rebuild_returns_stream_and_length(data_file: Path) -> None:
    body = Body.from_path(data_file, chunk_size=10)
    opened = body.rebuild()
    assert opened is not None
    stream, length = opened
    assert stream is body.stream
    assert length == 30
    body.close()


def test_length_can_change_between_rebuilds(data_file: Path) -> None:
    body = Body.from_path(data_file, chunk_size=10)
    first = body.rebuild()
    assert first is not None and first[1] == 30
    data_file.write_bytes(b"shorter")  # source shrinks between attempts
    second = body.rebuild()
    assert second is not None and second[1] == 7
    assert body.length == 7
    body.close()


def test_rebuild_replays_a_consumed_stream(data_file: Path) -> None:
    body = Body.from_path(data_file, chunk_size=10)
    first = body.rebuild()
    assert first is not None
    assert next(first[0]) == b"0123456789"
    second = body.rebuild()
    assert second is not None
    assert b"".join(second[0]) == data_file.read_bytes()
    body.close()


def test_rebuild_closes_the_previous_stream(data_file: Path) -> None:
    body = Body.from_path(data_file)
    opened = body.rebuild()
    assert opened is not None
    first = opened[0]
    again = body.rebuild()
    assert again is not None and first is not again[0]
    with pytest.raises(ValueError):  # the file behind the first stream is closed
        next(first)
    body.close()


def test_stream_is_none_before_rebuild_and_after_close(data_file: Path) -> None:
    body = Body.from_path(data_file)
    assert body.stream is None
    body.rebuild()
    assert body.stream is not None
    body.close()
    assert body.stream is None


def test_iterating_an_unopened_body_raises(data_file: Path) -> None:
    with pytest.raises(RuntimeError):
        next(Body.from_path(data_file))


def test_close_without_stream_is_a_noop(data_file: Path) -> None:
    Body.from_path(data_file).close()


def test_body_is_an_any_iterator_over_its_stream(data_file: Path) -> None:
    body = Body.from_path(data_file, chunk_size=10)
    assert isinstance(body, AnyIterator)
    assert ensure_sync_iterator(body) is body
    body.rebuild()
    assert list(body) == [b"0123456789"] * 3
    body.close()


def test_rebuild_returns_none_when_opener_yields_none() -> None:
    @contextmanager
    def opener() -> Iterator[tuple[Iterator[bytes], int] | None]:
        yield None

    body: Body[Iterator[bytes]] = Body(opener)
    assert body.rebuild() is None
    assert body.length is None
    assert body.stream is None  # nothing was opened
    body.close()


def test_async_from_path(data_file: Path) -> None:
    anyio = pytest.importorskip("anyio")

    async def main() -> None:
        body = Body.async_from_path(data_file, chunk_size=10)
        assert body.length is None
        assert ensure_async_iterator(body) is body
        opened = await body.arebuild()
        assert opened is not None
        stream, length = opened
        assert length == 30
        assert body.length == 30
        assert [chunk async for chunk in stream] == [b"0123456789"] * 3
        await body.arebuild()
        assert [chunk async for chunk in body] == [b"0123456789"] * 3
        await body.aclose()
        assert body.stream is None

    anyio.run(main)


def test_arebuild_returns_none_when_opener_yields_none() -> None:
    anyio = pytest.importorskip("anyio")

    @asynccontextmanager
    async def opener() -> AsyncIterator[tuple[AsyncIterator[bytes], int] | None]:
        yield None

    async def main() -> None:
        body: Body[AsyncIterator[bytes]] = Body(opener)
        assert await body.arebuild() is None
        assert body.length is None
        assert body.stream is None
        await body.aclose()

    anyio.run(main)


def test_rebuild_on_an_async_opener_raises_a_clear_typeerror() -> None:
    # The guard is for untyped callers who reach a sync Body method with an
    # async opener; typed code cannot construct this pairing.
    @asynccontextmanager
    async def opener() -> AsyncIterator[tuple[AsyncIterator[bytes], int]]:
        async def chunks() -> AsyncIterator[bytes]:
            yield b"x"

        yield chunks(), 1

    body: Body[Iterator[bytes]] = Body(opener)
    with pytest.raises(TypeError, match="async opener"):
        body.rebuild()


def test_arebuild_on_a_sync_opener_raises_a_clear_typeerror() -> None:
    anyio = pytest.importorskip("anyio")

    @contextmanager
    def opener() -> Iterator[tuple[Iterator[bytes], int]]:
        yield iter([b"x"]), 1

    async def main() -> None:
        body: Body[AsyncIterator[bytes]] = Body(opener)
        with pytest.raises(TypeError, match="sync opener"):
            await body.arebuild()

    anyio.run(main)


def test_custom_opener() -> None:
    opened = 0

    @contextmanager
    def opener() -> Iterator[tuple[Iterator[bytes], int]]:
        nonlocal opened
        opened += 1
        yield iter([b"ab", b"cd"]), 4

    body: Body[Iterator[bytes]] = Body(opener)
    body.rebuild()
    result = body.rebuild()
    assert opened == 2
    assert result is not None
    stream, length = result
    assert stream is body.stream and length == 4
    assert b"".join(stream) == b"abcd"


def test_custom_async_opener() -> None:
    anyio = pytest.importorskip("anyio")

    @asynccontextmanager
    async def opener() -> AsyncIterator[tuple[AsyncIterator[bytes], int]]:
        async def chunks() -> AsyncIterator[bytes]:
            yield b"ab"
            yield b"cd"

        yield chunks(), 4

    async def main() -> None:
        body: Body[AsyncIterator[bytes]] = Body(opener)
        opened = await body.arebuild()
        assert opened is not None
        stream, length = opened
        assert length == 4
        assert b"".join([chunk async for chunk in stream]) == b"abcd"
        await body.aclose()

    anyio.run(main)
