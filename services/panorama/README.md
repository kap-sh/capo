# capo-panorama: typed, async Python SDK for AWS Panorama

`capo-panorama` is a typed Python SDK for AWS Panorama. It has an async client, `AsyncPanoramaClient`, for asyncio and trio, and a sync client, `PanoramaClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/panorama/](https://capo-sdk.dev/services/panorama/)

## Installation

```
pip install capo-panorama
```

## Usage

```python
from capo_panorama import AsyncPanoramaClient


async def main():
    async with AsyncPanoramaClient() as panorama:
        # Example: call the create_application_instance operation
        response = await panorama.create_application_instance()
        print(response["application_instance_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_panorama import AsyncPanoramaClient


async def main():
    async with AsyncPanoramaClient() as panorama:
        # Example: paginate over list_application_instance_dependencies
        async for item in panorama.iter_list_application_instance_dependencies():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_panorama import AsyncPanoramaClient
from capo_panorama.error import AccessDeniedException


async def main():
    async with AsyncPanoramaClient() as panorama:
        try:
            await panorama.create_application_instance()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_panorama import AsyncPanoramaClient


async def main():
    async with AsyncPanoramaClient() as panorama:
        # Default: 3 attempts for every operation
        response = await panorama.create_application_instance()

        # Override per operation
        response = await panorama.create_application_instance(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await panorama.create_application_instance(config_overrides={"retry_max_attempts": 1})
```
