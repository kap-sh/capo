# Getting Started

## Installation

```
pip install capo-glacier
```

## Usage

```python
from capo_glacier import AsyncGlacierClient


async def main():
    async with AsyncGlacierClient() as glacier:
        # Example: call the abort_multipart_upload operation
        response = await glacier.abort_multipart_upload()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_glacier import AsyncGlacierClient


async def main():
    async with AsyncGlacierClient() as glacier:
        # Example: paginate over list_jobs
        async for item in glacier.iter_list_jobs():
            print(item)
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks, or the whole body as `bytes`, for the streaming parameter.

A plain iterator can be sent only once, so if a request fails after its body was transmitted the operation is not retried. To get retries for streamed uploads, pass a `Body` instead: it wraps a source that can be reopened, and every attempt streams a fresh copy. `Body.from_path` (sync client) and `Body.async_from_path` (async client, needs `anyio`) stream a file from disk; `Body(opener)` takes any context manager that yields a `(stream, length)` pair.

```python
from capo_glacier import AsyncGlacierClient, Body


async def main():
    async with AsyncGlacierClient() as glacier:
        # Example: call upload_archive with a streaming request body
        async def chunks():
            yield b'Hello, World!'

        response = await glacier.upload_archive(body=chunks())
        print(response)

        # Or pass the whole body as bytes
        response = await glacier.upload_archive(body=b'Hello, World!')
        print(response)

        # Or stream a file with Body: the file is reopened on every retry
        # and Content-Length is taken from its size, so no content_length needed
        response = await glacier.upload_archive(body=Body.async_from_path("hello.txt"))
        print(response)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_glacier import AsyncGlacierClient


async def main():
    async with AsyncGlacierClient() as glacier:
        # Example: call get_job_output and read the streaming response
        async with glacier.get_job_output() as response:
            async for chunk in response["body"]:
                print(chunk)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_until_` prefixed method.

```python
from capo_glacier import AsyncGlacierClient


async def main():
    async with AsyncGlacierClient() as glacier:
        # Example: wait for vault_exists
        await glacier.wait_until_vault_exists(max_wait_time=300)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_glacier import AsyncGlacierClient
from capo_glacier.error import InvalidParameterValueException


async def main():
    async with AsyncGlacierClient() as glacier:
        try:
            await glacier.abort_multipart_upload()
        except InvalidParameterValueException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_glacier import AsyncGlacierClient


async def main():
    async with AsyncGlacierClient() as glacier:
        # Default: 3 attempts for every operation
        response = await glacier.abort_multipart_upload()

        # Override per operation
        response = await glacier.abort_multipart_upload(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await glacier.abort_multipart_upload(config_overrides={"retry_max_attempts": 1})
```
