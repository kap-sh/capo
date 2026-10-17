# capo-s3-control: typed, async Python SDK for AWS S3 Control

`capo-s3-control` is a typed Python SDK for AWS S3 Control. It has an async client, `AsyncS3ControlClient`, for asyncio and trio, and a sync client, `S3ControlClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/s3-control/](https://capo-sdk.dev/services/s3-control/)

## Installation

```
pip install capo-s3-control
```

## Usage

```python
from capo_s3_control import AsyncS3ControlClient


async def main():
    async with AsyncS3ControlClient() as s3_control:
        # Example: call the associate_access_grants_identity_center operation
        response = await s3_control.associate_access_grants_identity_center()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_s3_control import AsyncS3ControlClient


async def main():
    async with AsyncS3ControlClient() as s3_control:
        # Example: paginate over list_access_grants
        async for item in s3_control.iter_list_access_grants():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_s3_control import AsyncS3ControlClient
from capo_s3_control.error import BucketAlreadyExists


async def main():
    async with AsyncS3ControlClient() as s3_control:
        try:
            await s3_control.create_bucket()
        except BucketAlreadyExists as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_s3_control import AsyncS3ControlClient


async def main():
    async with AsyncS3ControlClient() as s3_control:
        # Default: 3 attempts for every operation
        response = await s3_control.associate_access_grants_identity_center()

        # Override per operation
        response = await s3_control.associate_access_grants_identity_center(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3_control.associate_access_grants_identity_center(config_overrides={"retry_max_attempts": 1})
```
