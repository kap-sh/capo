# Getting Started

## Installation

```
pip install capo-bedrock-runtime
```

## Usage

```python
from capo_bedrock_runtime import AsyncBedrockRuntimeClient


async def main():
    async with AsyncBedrockRuntimeClient() as bedrock_runtime:
        # Example: call the get_async_invoke operation
        response = await bedrock_runtime.get_async_invoke()
        print(response["invocation_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_bedrock_runtime import AsyncBedrockRuntimeClient


async def main():
    async with AsyncBedrockRuntimeClient() as bedrock_runtime:
        # Example: paginate over list_async_invokes
        async for item in bedrock_runtime.iter_list_async_invokes():
            print(item)
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks, or the whole body as `bytes`, for the streaming parameter.

A plain iterator can be sent only once, so if a request fails after its body was transmitted the operation is not retried. To get retries for streamed uploads, pass a `Body` instead: it wraps a source that can be reopened, and every attempt streams a fresh copy. `Body.from_path` (sync client) and `Body.async_from_path` (async client, needs `anyio`) stream a file from disk; `Body(opener)` takes any context manager that yields a `(stream, length)` pair.

```python
from capo_bedrock_runtime import AsyncBedrockRuntimeClient, Body


async def main():
    async with AsyncBedrockRuntimeClient() as bedrock_runtime:
        # Example: call invoke_model_with_bidirectional_stream with a streaming request body
        async def chunks():
            yield b'Hello, World!'

        response = await bedrock_runtime.invoke_model_with_bidirectional_stream(body=chunks())
        print(response)

        # Or pass the whole body as bytes
        response = await bedrock_runtime.invoke_model_with_bidirectional_stream(body=b'Hello, World!')
        print(response)

        # Or stream a file with Body: the file is reopened on every retry
        # and Content-Length is taken from its size, so no content_length needed
        response = await bedrock_runtime.invoke_model_with_bidirectional_stream(body=Body.async_from_path("hello.txt"))
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_bedrock_runtime import AsyncBedrockRuntimeClient
from capo_bedrock_runtime.error import AccessDeniedException


async def main():
    async with AsyncBedrockRuntimeClient() as bedrock_runtime:
        try:
            await bedrock_runtime.get_async_invoke()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_bedrock_runtime import AsyncBedrockRuntimeClient


async def main():
    async with AsyncBedrockRuntimeClient() as bedrock_runtime:
        # Default: 3 attempts for every operation
        response = await bedrock_runtime.get_async_invoke()

        # Override per operation
        response = await bedrock_runtime.get_async_invoke(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await bedrock_runtime.get_async_invoke(config_overrides={"retry_max_attempts": 1})
```
