# capo-lex-runtime-service: typed, async Python SDK for AWS Lex Runtime Service

`capo-lex-runtime-service` is a typed Python SDK for AWS Lex Runtime Service. It has an async client, `AsyncLexRuntimeServiceClient`, for asyncio and trio, and a sync client, `LexRuntimeServiceClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/lex-runtime-service/](https://capo-sdk.dev/services/lex-runtime-service/)

## Installation

```
pip install capo-lex-runtime-service
```

## Usage

```python
from capo_lex_runtime_service import AsyncLexRuntimeServiceClient


async def main():
    async with AsyncLexRuntimeServiceClient() as lex_runtime_service:
        # Example: call the delete_session operation
        response = await lex_runtime_service.delete_session()
        print(response["bot_name"])
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks, or the whole body as `bytes`, for the streaming parameter.

A plain iterator can be sent only once, so if a request fails after its body was transmitted the operation is not retried. To get retries for streamed uploads, pass a `Body` instead: it wraps a source that can be reopened, and every attempt streams a fresh copy. `Body.from_path` (sync client) and `Body.async_from_path` (async client, needs `anyio`) stream a file from disk; `Body(opener)` takes any context manager that yields a `(stream, length)` pair.

```python
from capo_lex_runtime_service import AsyncLexRuntimeServiceClient, Body


async def main():
    async with AsyncLexRuntimeServiceClient() as lex_runtime_service:
        # Example: call post_content with a streaming request body
        async def chunks():
            yield b'Hello, World!'

        response = await lex_runtime_service.post_content(input_stream=chunks())
        print(response)

        # Or pass the whole body as bytes
        response = await lex_runtime_service.post_content(input_stream=b'Hello, World!')
        print(response)

        # Or stream a file with Body: the file is reopened on every retry
        # and Content-Length is taken from its size, so no content_length needed
        response = await lex_runtime_service.post_content(input_stream=Body.async_from_path("hello.txt"))
        print(response)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_lex_runtime_service import AsyncLexRuntimeServiceClient


async def main():
    async with AsyncLexRuntimeServiceClient() as lex_runtime_service:
        # Example: call post_content and read the streaming response
        async with lex_runtime_service.post_content() as response:
            async for chunk in response["audio_stream"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_lex_runtime_service import AsyncLexRuntimeServiceClient
from capo_lex_runtime_service.error import BadRequestException


async def main():
    async with AsyncLexRuntimeServiceClient() as lex_runtime_service:
        try:
            await lex_runtime_service.delete_session()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_lex_runtime_service import AsyncLexRuntimeServiceClient


async def main():
    async with AsyncLexRuntimeServiceClient() as lex_runtime_service:
        # Default: 3 attempts for every operation
        response = await lex_runtime_service.delete_session()

        # Override per operation
        response = await lex_runtime_service.delete_session(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await lex_runtime_service.delete_session(config_overrides={"retry_max_attempts": 1})
```
