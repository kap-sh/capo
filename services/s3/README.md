# Getting Started

## Installation

```
pip install capo-s3
```

## Usage

```python
from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Example: call the abort_multipart_upload operation
        response = await s3.abort_multipart_upload()
        print(response["request_charged"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Example: paginate over list_buckets
        async for item in s3.iter_list_buckets():
            print(item)
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks, or the whole body as `bytes`, for the streaming parameter.

A plain iterator can be sent only once, so if a request fails after its body was transmitted the operation is not retried. To get retries for streamed uploads, pass a `Body` instead: it wraps a source that can be reopened, and every attempt streams a fresh copy. `Body.from_path` (sync client) and `Body.async_from_path` (async client, needs `anyio`) stream a file from disk; `Body(opener)` takes any context manager that yields a `(stream, length)` pair.

```python
from capo_s3 import AsyncS3Client, Body


async def main():
    async with AsyncS3Client() as s3:
        # Example: call put_object with a streaming request body
        async def chunks():
            yield b'Hello, World!'

        # content_length is required: AWS must know the total body size up front
        response = await s3.put_object(body=chunks(), content_length=13)
        print(response)

        # Or pass the whole body as bytes
        response = await s3.put_object(body=b'Hello, World!')
        print(response)

        # Or stream a file with Body: the file is reopened on every retry
        # and Content-Length is taken from its size, so no content_length needed
        response = await s3.put_object(body=Body.async_from_path("hello.txt"))
        print(response)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Example: call get_object and read the streaming response
        async with s3.get_object() as response:
            async for chunk in response["body"]:
                print(chunk)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_until_` prefixed method.

```python
from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Example: wait for bucket_exists
        await s3.wait_until_bucket_exists(max_wait_time=300)
```

## Presigning

Some operations support presigning, which generates a URL that can be used without credentials. Use the `presigned_` prefixed method on the client to get a presigned URL.

```python
from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Example: get a presigned URL for delete_object
        url = s3.presigned_delete_object()
        print(url)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_s3 import AsyncS3Client
from capo_s3.error import NoSuchUpload


async def main():
    async with AsyncS3Client() as s3:
        try:
            await s3.abort_multipart_upload()
        except NoSuchUpload as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Default: 3 attempts for every operation
        response = await s3.abort_multipart_upload()

        # Override per operation
        response = await s3.abort_multipart_upload(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3.abort_multipart_upload(config_overrides={"retry_max_attempts": 1})
```
