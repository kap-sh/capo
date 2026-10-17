# capo-mediastore-data: typed, async Python SDK for AWS Mediastore Data

`capo-mediastore-data` is a typed Python SDK for AWS Mediastore Data. It has an async client, `AsyncMediaStoreDataClient`, for asyncio and trio, and a sync client, `MediaStoreDataClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/mediastore-data/](https://capo-sdk.dev/services/mediastore-data/)

## Installation

```
pip install capo-mediastore-data
```

## Usage

```python
from capo_mediastore_data import AsyncMediaStoreDataClient


async def main():
    async with AsyncMediaStoreDataClient() as media_store_data:
        # Example: call the delete_object operation
        response = await media_store_data.delete_object()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_mediastore_data import AsyncMediaStoreDataClient


async def main():
    async with AsyncMediaStoreDataClient() as media_store_data:
        # Example: paginate over list_items
        async for item in media_store_data.iter_list_items():
            print(item)
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks, or the whole body as `bytes`, for the streaming parameter.

A plain iterator can be sent only once, so if a request fails after its body was transmitted the operation is not retried. To get retries for streamed uploads, pass a `Body` instead: it wraps a source that can be reopened, and every attempt streams a fresh copy. `Body.from_path` (sync client) and `Body.async_from_path` (async client, needs `anyio`) stream a file from disk; `Body(opener)` takes any context manager that yields a `(stream, length)` pair.

```python
from capo_mediastore_data import AsyncMediaStoreDataClient, Body


async def main():
    async with AsyncMediaStoreDataClient() as media_store_data:
        # Example: call put_object with a streaming request body
        async def chunks():
            yield b'Hello, World!'

        response = await media_store_data.put_object(body=chunks())
        print(response)

        # Or pass the whole body as bytes
        response = await media_store_data.put_object(body=b'Hello, World!')
        print(response)

        # Or stream a file with Body: the file is reopened on every retry
        # and Content-Length is taken from its size, so no content_length needed
        response = await media_store_data.put_object(body=Body.async_from_path("hello.txt"))
        print(response)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_mediastore_data import AsyncMediaStoreDataClient


async def main():
    async with AsyncMediaStoreDataClient() as media_store_data:
        # Example: call get_object and read the streaming response
        async with media_store_data.get_object() as response:
            async for chunk in response["body"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_mediastore_data import AsyncMediaStoreDataClient
from capo_mediastore_data.error import ContainerNotFoundException


async def main():
    async with AsyncMediaStoreDataClient() as media_store_data:
        try:
            await media_store_data.delete_object()
        except ContainerNotFoundException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_mediastore_data import AsyncMediaStoreDataClient


async def main():
    async with AsyncMediaStoreDataClient() as media_store_data:
        # Default: 3 attempts for every operation
        response = await media_store_data.delete_object()

        # Override per operation
        response = await media_store_data.delete_object(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await media_store_data.delete_object(config_overrides={"retry_max_attempts": 1})
```
