"""Event streams over real connections.

* Output stream: S3 ``SelectObjectContent`` against the local RustFS server (free).
* Input + output stream: Transcribe ``StartStreamTranscription`` against AWS
  (paid, billed per audio minute). This is the operation that needs every
  request event signed with a chained SigV4 ``:chunk-signature`` frame, so it
  can only be proven live.

Each async class is the source and runs on asyncio and trio; ``ry`` generates
the sync twin below it.
"""

from __future__ import annotations

import hashlib
import time
from collections.abc import Iterator, Mapping, Sequence
from pathlib import Path
from typing import Any

import anyio
import pytest
from capo_s3 import AsyncS3Client, S3Client
from capo_s3.errors import ServiceError
from capo_transcribe_streaming import (
    AsyncTranscribeStreamingClient,
    TranscribeStreamingClient,
)
from capo_transcribe_streaming.errors.bad_request_exception import BadRequestException

from tests.conftest import AWS_REGION, agather, gather, purge_bucket, unique_name

# ---------------------------------------------------------------------------
# S3 SelectObjectContent
# ---------------------------------------------------------------------------

SMALL = b"id,name,score\n1,ann,10\n2,bob,20\n3,cyd,30\n"
SMALL_ROWS = SMALL.split(b"\n", 1)[1]
BIG_ROWS = 300_000
BIG = b"id,name,score\n" + b"".join(b"%d,user%d,%d\n" % (i, i, i % 100) for i in range(BIG_ROWS))
BIG_BODY = BIG[len(b"id,name,score\n") :]
JSONL = b'{"id":1,"tag":"a"}\n{"id":2,"tag":"b"}\n{"id":3,"tag":"a"}\n'

CSV_IN = {"csv": {"file_header_info": "USE"}}
CSV_OUT = {"csv": {}}
SELECT_ALL = "SELECT * FROM S3Object"


def query(expression: str, inp=CSV_IN, out=CSV_OUT, **extra) -> dict:
    return dict(
        expression=expression,
        expression_type="SQL",
        input_serialization=inp,
        output_serialization=out,
        **extra,
    )


def summarize(events: Sequence[Mapping[str, Any]]) -> tuple[list[str], bytes]:
    kinds = [next(iter(e)) for e in events]
    data = b"".join(e["Records"].get("payload", b"") for e in events if "Records" in e)
    return kinds, data


@pytest.fixture(scope="module")
def csv_bucket(s3: S3Client, s3_backend: str) -> Iterator[str]:
    # S3 Select is closed to new AWS accounts (MethodNotAllowed), so only the local backends run it.
    # The skip lives here because this module-scoped fixture is set up before any function-scoped one.
    if s3_backend == "aws":
        pytest.skip("S3 Select is not available on AWS")
    name = unique_name("capotest-select")
    s3.create_bucket(name)
    try:
        s3.put_object(name, "small.csv", body=SMALL)
        s3.put_object(name, "big.csv", body=BIG)
        s3.put_object(name, "data.jsonl", body=JSONL)
        yield name
    finally:
        purge_bucket(s3, name)


class TestAsyncSelectObjectContent:  # unasync: generate
    async def test_small_csv(self, async_s3: AsyncS3Client, csv_bucket: str):
        async with async_s3.select_object_content(csv_bucket, "small.csv", **query(SELECT_ALL)) as out:
            kinds, data = summarize([e async for e in out["payload"]])
        assert data == SMALL_ROWS
        assert kinds[-1] == "End"

    async def test_where_with_json_output(self, async_s3: AsyncS3Client, csv_bucket: str):
        q = query("SELECT s.name FROM S3Object s WHERE CAST(s.score AS INT) > 15", out={"json": {}})
        async with async_s3.select_object_content(csv_bucket, "small.csv", **q) as out:
            _, data = summarize([e async for e in out["payload"]])
        assert data == b'{"name":"bob"}\n{"name":"cyd"}\n'

    async def test_json_lines_input(self, async_s3: AsyncS3Client, csv_bucket: str):
        q = query("SELECT s.id FROM S3Object s WHERE s.tag = 'a'", inp={"json": {"type": "LINES"}})
        async with async_s3.select_object_content(csv_bucket, "data.jsonl", **q) as out:
            _, data = summarize([e async for e in out["payload"]])
        assert data == b"1\n3\n"

    async def test_large_result_spans_many_frames(self, async_s3: AsyncS3Client, csv_bucket: str):
        async with async_s3.select_object_content(csv_bucket, "big.csv", **query(SELECT_ALL)) as out:
            kinds, data = summarize([e async for e in out["payload"]])
        assert hashlib.sha256(data).digest() == hashlib.sha256(BIG_BODY).digest()
        assert kinds.count("Records") > 1
        assert kinds[-1] == "End"

    async def test_progress_and_stats_events(self, async_s3: AsyncS3Client, csv_bucket: str):
        q = query("SELECT COUNT(*) FROM S3Object", request_progress={"enabled": True})
        async with async_s3.select_object_content(csv_bucket, "big.csv", **q) as out:
            events = [e async for e in out["payload"]]
        kinds, data = summarize(events)
        assert data.strip() == str(BIG_ROWS).encode()
        assert "Stats" in kinds
        stats = next(e["Stats"] for e in events if "Stats" in e)
        assert stats["details"]["bytes_scanned"] == len(BIG)

    async def test_scan_range(self, async_s3: AsyncS3Client, csv_bucket: str):
        q = query(SELECT_ALL, inp={"csv": {"file_header_info": "NONE"}}, scan_range={"start": 0, "end": 100})
        async with async_s3.select_object_content(csv_bucket, "big.csv", **q) as out:
            _, data = summarize([e async for e in out["payload"]])
        assert data.startswith(b"id,name,score\n")
        assert 100 <= len(data) < 400  # whole records only, up to the first past `end`

    async def test_bad_sql_raises(self, async_s3: AsyncS3Client, csv_bucket: str):
        with pytest.raises(ServiceError) as info:
            async with async_s3.select_object_content(csv_bucket, "small.csv", **query("SELEC nonsense FRM")) as out:
                [e async for e in out["payload"]]
        assert info.value.code

    async def test_missing_key_raises(self, async_s3: AsyncS3Client, csv_bucket: str):
        with pytest.raises(ServiceError) as info:
            async with async_s3.select_object_content(csv_bucket, "nope.csv", **query(SELECT_ALL)) as out:
                [e async for e in out["payload"]]
        assert info.value.code == "NoSuchKey"

    async def test_abandoned_stream_leaves_client_usable(self, async_s3: AsyncS3Client, csv_bucket: str):
        async with async_s3.select_object_content(csv_bucket, "big.csv", **query(SELECT_ALL)) as out:
            async for first in out["payload"]:
                break
        assert "Records" in first
        async with async_s3.select_object_content(csv_bucket, "small.csv", **query(SELECT_ALL)) as out:
            _, data = summarize([e async for e in out["payload"]])
        assert data == SMALL_ROWS

    async def test_concurrent_streams(self, async_s3: AsyncS3Client, csv_bucket: str):
        async def count() -> bytes:
            q = query("SELECT COUNT(*) FROM S3Object")
            async with async_s3.select_object_content(csv_bucket, "big.csv", **q) as out:
                return summarize([e async for e in out["payload"]])[1].strip()

        assert await agather(count, 5) == [str(BIG_ROWS).encode()] * 5

class TestSelectObjectContent:  # unasync: generated
    def test_small_csv(self, s3: S3Client, csv_bucket: str):
        with s3.select_object_content(csv_bucket, "small.csv", **query(SELECT_ALL)) as out:
            kinds, data = summarize([e for e in out["payload"]])
        assert data == SMALL_ROWS
        assert kinds[-1] == "End"

    def test_where_with_json_output(self, s3: S3Client, csv_bucket: str):
        q = query("SELECT s.name FROM S3Object s WHERE CAST(s.score AS INT) > 15", out={"json": {}})
        with s3.select_object_content(csv_bucket, "small.csv", **q) as out:
            _, data = summarize([e for e in out["payload"]])
        assert data == b'{"name":"bob"}\n{"name":"cyd"}\n'

    def test_json_lines_input(self, s3: S3Client, csv_bucket: str):
        q = query("SELECT s.id FROM S3Object s WHERE s.tag = 'a'", inp={"json": {"type": "LINES"}})
        with s3.select_object_content(csv_bucket, "data.jsonl", **q) as out:
            _, data = summarize([e for e in out["payload"]])
        assert data == b"1\n3\n"

    def test_large_result_spans_many_frames(self, s3: S3Client, csv_bucket: str):
        with s3.select_object_content(csv_bucket, "big.csv", **query(SELECT_ALL)) as out:
            kinds, data = summarize([e for e in out["payload"]])
        assert hashlib.sha256(data).digest() == hashlib.sha256(BIG_BODY).digest()
        assert kinds.count("Records") > 1
        assert kinds[-1] == "End"

    def test_progress_and_stats_events(self, s3: S3Client, csv_bucket: str):
        q = query("SELECT COUNT(*) FROM S3Object", request_progress={"enabled": True})
        with s3.select_object_content(csv_bucket, "big.csv", **q) as out:
            events = [e for e in out["payload"]]
        kinds, data = summarize(events)
        assert data.strip() == str(BIG_ROWS).encode()
        assert "Stats" in kinds
        stats = next(e["Stats"] for e in events if "Stats" in e)
        assert stats["details"]["bytes_scanned"] == len(BIG)

    def test_scan_range(self, s3: S3Client, csv_bucket: str):
        q = query(SELECT_ALL, inp={"csv": {"file_header_info": "NONE"}}, scan_range={"start": 0, "end": 100})
        with s3.select_object_content(csv_bucket, "big.csv", **q) as out:
            _, data = summarize([e for e in out["payload"]])
        assert data.startswith(b"id,name,score\n")
        assert 100 <= len(data) < 400  # whole records only, up to the first past `end`

    def test_bad_sql_raises(self, s3: S3Client, csv_bucket: str):
        with pytest.raises(ServiceError) as info:
            with s3.select_object_content(csv_bucket, "small.csv", **query("SELEC nonsense FRM")) as out:
                [e for e in out["payload"]]
        assert info.value.code

    def test_missing_key_raises(self, s3: S3Client, csv_bucket: str):
        with pytest.raises(ServiceError) as info:
            with s3.select_object_content(csv_bucket, "nope.csv", **query(SELECT_ALL)) as out:
                [e for e in out["payload"]]
        assert info.value.code == "NoSuchKey"

    def test_abandoned_stream_leaves_client_usable(self, s3: S3Client, csv_bucket: str):
        with s3.select_object_content(csv_bucket, "big.csv", **query(SELECT_ALL)) as out:
            for first in out["payload"]:
                break
        assert "Records" in first
        with s3.select_object_content(csv_bucket, "small.csv", **query(SELECT_ALL)) as out:
            _, data = summarize([e for e in out["payload"]])
        assert data == SMALL_ROWS

    def test_concurrent_streams(self, s3: S3Client, csv_bucket: str):
        def count() -> bytes:
            q = query("SELECT COUNT(*) FROM S3Object")
            with s3.select_object_content(csv_bucket, "big.csv", **q) as out:
                return summarize([e for e in out["payload"]])[1].strip()

        assert gather(count, 5) == [str(BIG_ROWS).encode()] * 5


# ---------------------------------------------------------------------------
# Transcribe StartStreamTranscription (signed request event stream)
# ---------------------------------------------------------------------------

# 2.7 s of "Hello, this is a test of event stream signing." as 16 kHz s16le mono.
SPEECH = (Path(__file__).parent / "data" / "speech-16k-mono.pcm").read_bytes()
CHUNK = 3200  # 100 ms


def final_transcripts(events: Sequence[Mapping[str, Any]]) -> list[str]:
    return [
        alt["transcript"]
        for event in events
        for result in event.get("TranscriptEvent", {}).get("transcript", {}).get("results", [])
        if not result.get("is_partial")
        for alt in result.get("alternatives", [])[:1]
    ]


class TestAsyncTranscribeStreaming:  # unasync: generate
    pytestmark = pytest.mark.paid

    async def test_stream_is_transcribed(self):
        async def audio():
            for i in range(0, len(SPEECH), CHUNK):
                yield {"AudioEvent": {"audio_chunk": SPEECH[i : i + CHUNK]}}
                await anyio.sleep(0.1)  # real-time pacing

        async with AsyncTranscribeStreamingClient(region=AWS_REGION) as client:
            async with client.start_stream_transcription(
                media_sample_rate_hertz=16000, media_encoding="pcm", language_code="en-US", audio_stream=audio()
            ) as out:
                events = [e async for e in out["transcript_result_stream"]]
        assert events, "no events came back"
        assert all("TranscriptEvent" in e for e in events)
        transcript = " ".join(final_transcripts(events)).lower()
        assert "hello" in transcript, transcript

    async def test_in_stream_exception_is_raised_typed(self):
        # One chunk, then silence: AWS closes the stream with an in-band
        # BadRequestException frame after 15 s without audio.
        async def audio():
            yield {"AudioEvent": {"audio_chunk": SPEECH[:CHUNK]}}
            await anyio.sleep(20)

        with pytest.raises(BadRequestException, match="no new audio"):
            async with AsyncTranscribeStreamingClient(region=AWS_REGION) as client:
                async with client.start_stream_transcription(
                    media_sample_rate_hertz=16000, media_encoding="pcm", language_code="en-US", audio_stream=audio()
                ) as out:
                    async for _ in out["transcript_result_stream"]:
                        pass

class TestTranscribeStreaming:  # unasync: generated
    pytestmark = pytest.mark.paid

    def test_stream_is_transcribed(self):
        def audio():
            for i in range(0, len(SPEECH), CHUNK):
                yield {"AudioEvent": {"audio_chunk": SPEECH[i : i + CHUNK]}}
                time.sleep(0.1)  # real-time pacing

        with TranscribeStreamingClient(region=AWS_REGION) as client:
            with client.start_stream_transcription(
                media_sample_rate_hertz=16000, media_encoding="pcm", language_code="en-US", audio_stream=audio()
            ) as out:
                events = [e for e in out["transcript_result_stream"]]
        assert events, "no events came back"
        assert all("TranscriptEvent" in e for e in events)
        transcript = " ".join(final_transcripts(events)).lower()
        assert "hello" in transcript, transcript

    def test_in_stream_exception_is_raised_typed(self):
        # One chunk, then silence: AWS closes the stream with an in-band
        # BadRequestException frame after 15 s without audio.
        def audio():
            yield {"AudioEvent": {"audio_chunk": SPEECH[:CHUNK]}}
            time.sleep(20)

        with pytest.raises(BadRequestException, match="no new audio"):
            with TranscribeStreamingClient(region=AWS_REGION) as client:
                with client.start_stream_transcription(
                    media_sample_rate_hertz=16000, media_encoding="pcm", language_code="en-US", audio_stream=audio()
                ) as out:
                    for _ in out["transcript_result_stream"]:
                        pass
