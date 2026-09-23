# Getting Started

## Installation

```
pip install capo-transcribe-streaming
```

## Usage

```python
from capo_transcribe_streaming import AsyncTranscribeStreamingClient


async def main():
    async with AsyncTranscribeStreamingClient() as transcribe_streaming:
        # Example: call the get_medical_scribe_stream operation
        response = await transcribe_streaming.get_medical_scribe_stream()
        print(response["medical_scribe_stream_details"])
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks, or the whole body as `bytes`, for the streaming parameter.

A plain iterator can be sent only once, so if a request fails after its body was transmitted the operation is not retried. To get retries for streamed uploads, pass a `Body` instead: it wraps a source that can be reopened, and every attempt streams a fresh copy. `Body.from_path` (sync client) and `Body.async_from_path` (async client, needs `anyio`) stream a file from disk; `Body(opener)` takes any context manager that yields a `(stream, length)` pair.

```python
from capo_transcribe_streaming import AsyncTranscribeStreamingClient, Body


async def main():
    async with AsyncTranscribeStreamingClient() as transcribe_streaming:
        # Example: call start_call_analytics_stream_transcription with a streaming request body
        async def chunks():
            yield b'Hello, World!'

        response = await transcribe_streaming.start_call_analytics_stream_transcription(audio_stream=chunks())
        print(response)

        # Or pass the whole body as bytes
        response = await transcribe_streaming.start_call_analytics_stream_transcription(audio_stream=b'Hello, World!')
        print(response)

        # Or stream a file with Body: the file is reopened on every retry
        # and Content-Length is taken from its size, so no content_length needed
        response = await transcribe_streaming.start_call_analytics_stream_transcription(audio_stream=Body.async_from_path("hello.txt"))
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_transcribe_streaming import AsyncTranscribeStreamingClient
from capo_transcribe_streaming.error import BadRequestException


async def main():
    async with AsyncTranscribeStreamingClient() as transcribe_streaming:
        try:
            await transcribe_streaming.get_medical_scribe_stream()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_transcribe_streaming import AsyncTranscribeStreamingClient


async def main():
    async with AsyncTranscribeStreamingClient() as transcribe_streaming:
        # Default: 3 attempts for every operation
        response = await transcribe_streaming.get_medical_scribe_stream()

        # Override per operation
        response = await transcribe_streaming.get_medical_scribe_stream(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await transcribe_streaming.get_medical_scribe_stream(config_overrides={"retry_max_attempts": 1})
```
