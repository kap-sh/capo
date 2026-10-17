# capo-cloudhsm: typed, async Python SDK for AWS Cloudhsm

`capo-cloudhsm` is a typed Python SDK for AWS Cloudhsm. It has an async client, `AsyncCloudHSMClient`, for asyncio and trio, and a sync client, `CloudHSMClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cloudhsm/](https://capo-sdk.dev/services/cloudhsm/)

## Installation

```
pip install capo-cloudhsm
```

## Usage

```python
from capo_cloudhsm import AsyncCloudHSMClient


async def main():
    async with AsyncCloudHSMClient() as cloud_hsm:
        # Example: call the add_tags_to_resource operation
        response = await cloud_hsm.add_tags_to_resource()
        print(response["status"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cloudhsm import AsyncCloudHSMClient
from capo_cloudhsm.error import CloudHsmInternalException


async def main():
    async with AsyncCloudHSMClient() as cloud_hsm:
        try:
            await cloud_hsm.add_tags_to_resource()
        except CloudHsmInternalException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cloudhsm import AsyncCloudHSMClient


async def main():
    async with AsyncCloudHSMClient() as cloud_hsm:
        # Default: 3 attempts for every operation
        response = await cloud_hsm.add_tags_to_resource()

        # Override per operation
        response = await cloud_hsm.add_tags_to_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cloud_hsm.add_tags_to_resource(config_overrides={"retry_max_attempts": 1})
```
