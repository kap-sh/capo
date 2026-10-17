# capo-cloudsearch: typed, async Python SDK for AWS Cloudsearch

`capo-cloudsearch` is a typed Python SDK for AWS Cloudsearch. It has an async client, `AsyncCloudSearchClient`, for asyncio and trio, and a sync client, `CloudSearchClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cloudsearch/](https://capo-sdk.dev/services/cloudsearch/)

## Installation

```
pip install capo-cloudsearch
```

## Usage

```python
from capo_cloudsearch import AsyncCloudSearchClient


async def main():
    async with AsyncCloudSearchClient() as cloud_search:
        # Example: call the build_suggesters operation
        response = await cloud_search.build_suggesters()
        print(response["field_names"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cloudsearch import AsyncCloudSearchClient
from capo_cloudsearch.error import BaseException


async def main():
    async with AsyncCloudSearchClient() as cloud_search:
        try:
            await cloud_search.build_suggesters()
        except BaseException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cloudsearch import AsyncCloudSearchClient


async def main():
    async with AsyncCloudSearchClient() as cloud_search:
        # Default: 3 attempts for every operation
        response = await cloud_search.build_suggesters()

        # Override per operation
        response = await cloud_search.build_suggesters(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cloud_search.build_suggesters(config_overrides={"retry_max_attempts": 1})
```
