# Getting Started

## Installation

```
pip install capo-cloudsearch-domain
```

## Usage

```python
from capo_cloudsearch_domain import AsyncCloudSearchDomainClient


async def main():
    async with AsyncCloudSearchDomainClient() as cloud_search_domain:
        # Example: call the search operation
        response = await cloud_search_domain.search()
        print(response["status"])
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks, or the whole body as `bytes`, for the streaming parameter.

A plain iterator can be sent only once, so if a request fails after its body was transmitted the operation is not retried. To get retries for streamed uploads, pass a `Body` instead: it wraps a source that can be reopened, and every attempt streams a fresh copy. `Body.from_path` (sync client) and `Body.async_from_path` (async client, needs `anyio`) stream a file from disk; `Body(opener)` takes any context manager that yields a `(stream, length)` pair.

```python
from capo_cloudsearch_domain import AsyncCloudSearchDomainClient, Body


async def main():
    async with AsyncCloudSearchDomainClient() as cloud_search_domain:
        # Example: call upload_documents with a streaming request body
        async def chunks():
            yield b'Hello, World!'

        response = await cloud_search_domain.upload_documents(documents=chunks())
        print(response)

        # Or pass the whole body as bytes
        response = await cloud_search_domain.upload_documents(documents=b'Hello, World!')
        print(response)

        # Or stream a file with Body: the file is reopened on every retry
        # and Content-Length is taken from its size, so no content_length needed
        response = await cloud_search_domain.upload_documents(documents=Body.async_from_path("hello.txt"))
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cloudsearch_domain import AsyncCloudSearchDomainClient
from capo_cloudsearch_domain.error import SearchException


async def main():
    async with AsyncCloudSearchDomainClient() as cloud_search_domain:
        try:
            await cloud_search_domain.search()
        except SearchException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cloudsearch_domain import AsyncCloudSearchDomainClient


async def main():
    async with AsyncCloudSearchDomainClient() as cloud_search_domain:
        # Default: 3 attempts for every operation
        response = await cloud_search_domain.search()

        # Override per operation
        response = await cloud_search_domain.search(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cloud_search_domain.search(config_overrides={"retry_max_attempts": 1})
```
