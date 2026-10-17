# capo-polly: typed, async Python SDK for AWS Polly

`capo-polly` is a typed Python SDK for AWS Polly. It has an async client, `AsyncPollyClient`, for asyncio and trio, and a sync client, `PollyClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/polly/](https://capo-sdk.dev/services/polly/)

## Installation

```
pip install capo-polly
```

## Usage

```python
from capo_polly import AsyncPollyClient


async def main():
    async with AsyncPollyClient() as polly:
        # Example: call the delete_lexicon operation
        response = await polly.delete_lexicon()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_polly import AsyncPollyClient


async def main():
    async with AsyncPollyClient() as polly:
        # Example: paginate over list_speech_synthesis_tasks
        async for item in polly.iter_list_speech_synthesis_tasks():
            print(item)
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks, or the whole body as `bytes`, for the streaming parameter.

A plain iterator can be sent only once, so if a request fails after its body was transmitted the operation is not retried. To get retries for streamed uploads, pass a `Body` instead: it wraps a source that can be reopened, and every attempt streams a fresh copy. `Body.from_path` (sync client) and `Body.async_from_path` (async client, needs `anyio`) stream a file from disk; `Body(opener)` takes any context manager that yields a `(stream, length)` pair.

```python
from capo_polly import AsyncPollyClient, Body


async def main():
    async with AsyncPollyClient() as polly:
        # Example: call start_speech_synthesis_stream with a streaming request body
        async def chunks():
            yield b'Hello, World!'

        response = await polly.start_speech_synthesis_stream(action_stream=chunks())
        print(response)

        # Or pass the whole body as bytes
        response = await polly.start_speech_synthesis_stream(action_stream=b'Hello, World!')
        print(response)

        # Or stream a file with Body: the file is reopened on every retry
        # and Content-Length is taken from its size, so no content_length needed
        response = await polly.start_speech_synthesis_stream(action_stream=Body.async_from_path("hello.txt"))
        print(response)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_polly import AsyncPollyClient


async def main():
    async with AsyncPollyClient() as polly:
        # Example: call synthesize_speech and read the streaming response
        async with polly.synthesize_speech() as response:
            async for chunk in response["audio_stream"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_polly import AsyncPollyClient
from capo_polly.error import LexiconNotFoundException


async def main():
    async with AsyncPollyClient() as polly:
        try:
            await polly.delete_lexicon()
        except LexiconNotFoundException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_polly import AsyncPollyClient


async def main():
    async with AsyncPollyClient() as polly:
        # Default: 3 attempts for every operation
        response = await polly.delete_lexicon()

        # Override per operation
        response = await polly.delete_lexicon(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await polly.delete_lexicon(config_overrides={"retry_max_attempts": 1})
```
