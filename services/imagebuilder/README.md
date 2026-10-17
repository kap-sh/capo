# capo-imagebuilder: typed, async Python SDK for AWS Imagebuilder

`capo-imagebuilder` is a typed Python SDK for AWS Imagebuilder. It has an async client, `AsyncimagebuilderClient`, for asyncio and trio, and a sync client, `imagebuilderClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/imagebuilder/](https://capo-sdk.dev/services/imagebuilder/)

## Installation

```
pip install capo-imagebuilder
```

## Usage

```python
from capo_imagebuilder import AsyncimagebuilderClient


async def main():
    async with AsyncimagebuilderClient() as imagebuilder:
        # Example: call the cancel_image_creation operation
        response = await imagebuilder.cancel_image_creation()
        print(response["request_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_imagebuilder import AsyncimagebuilderClient


async def main():
    async with AsyncimagebuilderClient() as imagebuilder:
        # Example: paginate over list_component_build_versions
        async for item in imagebuilder.iter_list_component_build_versions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_imagebuilder import AsyncimagebuilderClient
from capo_imagebuilder.error import CallRateLimitExceededException


async def main():
    async with AsyncimagebuilderClient() as imagebuilder:
        try:
            await imagebuilder.cancel_image_creation()
        except CallRateLimitExceededException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_imagebuilder import AsyncimagebuilderClient


async def main():
    async with AsyncimagebuilderClient() as imagebuilder:
        # Default: 3 attempts for every operation
        response = await imagebuilder.cancel_image_creation()

        # Override per operation
        response = await imagebuilder.cancel_image_creation(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await imagebuilder.cancel_image_creation(config_overrides={"retry_max_attempts": 1})
```
