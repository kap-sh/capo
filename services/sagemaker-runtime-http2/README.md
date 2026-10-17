# capo-sagemaker-runtime-http2: typed, async Python SDK for AWS Sagemaker Runtime Http2

`capo-sagemaker-runtime-http2` is a typed Python SDK for AWS Sagemaker Runtime Http2. It has an async client, `AsyncSageMakerRuntimeHTTP2Client`, for asyncio and trio, and a sync client, `SageMakerRuntimeHTTP2Client`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/sagemaker-runtime-http2/](https://capo-sdk.dev/services/sagemaker-runtime-http2/)

## Installation

```
pip install capo-sagemaker-runtime-http2
```

## Usage

```python
from capo_sagemaker_runtime_http2 import AsyncSageMakerRuntimeHTTP2Client


async def main():
    async with AsyncSageMakerRuntimeHTTP2Client() as sage_maker_runtime_http2:
        # Example: call the invoke_endpoint_with_bidirectional_stream operation
        response = await sage_maker_runtime_http2.invoke_endpoint_with_bidirectional_stream()
        print(response["body"])
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks, or the whole body as `bytes`, for the streaming parameter.

A plain iterator can be sent only once, so if a request fails after its body was transmitted the operation is not retried. To get retries for streamed uploads, pass a `Body` instead: it wraps a source that can be reopened, and every attempt streams a fresh copy. `Body.from_path` (sync client) and `Body.async_from_path` (async client, needs `anyio`) stream a file from disk; `Body(opener)` takes any context manager that yields a `(stream, length)` pair.

```python
from capo_sagemaker_runtime_http2 import AsyncSageMakerRuntimeHTTP2Client, Body


async def main():
    async with AsyncSageMakerRuntimeHTTP2Client() as sage_maker_runtime_http2:
        # Example: call invoke_endpoint_with_bidirectional_stream with a streaming request body
        async def chunks():
            yield b'Hello, World!'

        response = await sage_maker_runtime_http2.invoke_endpoint_with_bidirectional_stream(body=chunks())
        print(response)

        # Or pass the whole body as bytes
        response = await sage_maker_runtime_http2.invoke_endpoint_with_bidirectional_stream(body=b'Hello, World!')
        print(response)

        # Or stream a file with Body: the file is reopened on every retry
        # and Content-Length is taken from its size, so no content_length needed
        response = await sage_maker_runtime_http2.invoke_endpoint_with_bidirectional_stream(body=Body.async_from_path("hello.txt"))
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sagemaker_runtime_http2 import AsyncSageMakerRuntimeHTTP2Client
from capo_sagemaker_runtime_http2.error import InputValidationError


async def main():
    async with AsyncSageMakerRuntimeHTTP2Client() as sage_maker_runtime_http2:
        try:
            await sage_maker_runtime_http2.invoke_endpoint_with_bidirectional_stream()
        except InputValidationError as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sagemaker_runtime_http2 import AsyncSageMakerRuntimeHTTP2Client


async def main():
    async with AsyncSageMakerRuntimeHTTP2Client() as sage_maker_runtime_http2:
        # Default: 3 attempts for every operation
        response = await sage_maker_runtime_http2.invoke_endpoint_with_bidirectional_stream()

        # Override per operation
        response = await sage_maker_runtime_http2.invoke_endpoint_with_bidirectional_stream(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await sage_maker_runtime_http2.invoke_endpoint_with_bidirectional_stream(config_overrides={"retry_max_attempts": 1})
```
