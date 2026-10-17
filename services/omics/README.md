# capo-omics: typed, async Python SDK for AWS Omics

`capo-omics` is a typed Python SDK for AWS Omics. It has an async client, `AsyncOmicsClient`, for asyncio and trio, and a sync client, `OmicsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/omics/](https://capo-sdk.dev/services/omics/)

## Installation

```
pip install capo-omics
```

## Usage

```python
from capo_omics import AsyncOmicsClient


async def main():
    async with AsyncOmicsClient() as omics:
        # Example: call the delete_s3_access_policy operation
        response = await omics.delete_s3_access_policy()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_omics import AsyncOmicsClient


async def main():
    async with AsyncOmicsClient() as omics:
        # Example: paginate over list_annotation_import_jobs
        async for item in omics.iter_list_annotation_import_jobs():
            print(item)
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks, or the whole body as `bytes`, for the streaming parameter.

A plain iterator can be sent only once, so if a request fails after its body was transmitted the operation is not retried. To get retries for streamed uploads, pass a `Body` instead: it wraps a source that can be reopened, and every attempt streams a fresh copy. `Body.from_path` (sync client) and `Body.async_from_path` (async client, needs `anyio`) stream a file from disk; `Body(opener)` takes any context manager that yields a `(stream, length)` pair.

```python
from capo_omics import AsyncOmicsClient, Body


async def main():
    async with AsyncOmicsClient() as omics:
        # Example: call upload_read_set_part with a streaming request body
        async def chunks():
            yield b'Hello, World!'

        response = await omics.upload_read_set_part(payload=chunks())
        print(response)

        # Or pass the whole body as bytes
        response = await omics.upload_read_set_part(payload=b'Hello, World!')
        print(response)

        # Or stream a file with Body: the file is reopened on every retry
        # and Content-Length is taken from its size, so no content_length needed
        response = await omics.upload_read_set_part(payload=Body.async_from_path("hello.txt"))
        print(response)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_omics import AsyncOmicsClient


async def main():
    async with AsyncOmicsClient() as omics:
        # Example: call get_reference and read the streaming response
        async with omics.get_reference() as response:
            async for chunk in response["payload"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_omics import AsyncOmicsClient
from capo_omics.error import AccessDeniedException


async def main():
    async with AsyncOmicsClient() as omics:
        try:
            await omics.delete_s3_access_policy()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_omics import AsyncOmicsClient


async def main():
    async with AsyncOmicsClient() as omics:
        # Default: 3 attempts for every operation
        response = await omics.delete_s3_access_policy()

        # Override per operation
        response = await omics.delete_s3_access_policy(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await omics.delete_s3_access_policy(config_overrides={"retry_max_attempts": 1})
```
