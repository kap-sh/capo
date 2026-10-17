# capo-comprehendmedical: typed, async Python SDK for AWS Comprehendmedical

`capo-comprehendmedical` is a typed Python SDK for AWS Comprehendmedical. It has an async client, `AsyncComprehendMedicalClient`, for asyncio and trio, and a sync client, `ComprehendMedicalClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/comprehendmedical/](https://capo-sdk.dev/services/comprehendmedical/)

## Installation

```
pip install capo-comprehendmedical
```

## Usage

```python
from capo_comprehendmedical import AsyncComprehendMedicalClient


async def main():
    async with AsyncComprehendMedicalClient() as comprehend_medical:
        # Example: call the describe_entities_detection_v2_job operation
        response = await comprehend_medical.describe_entities_detection_v2_job()
        print(response["comprehend_medical_async_job_properties"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_comprehendmedical import AsyncComprehendMedicalClient
from capo_comprehendmedical.error import InternalServerException


async def main():
    async with AsyncComprehendMedicalClient() as comprehend_medical:
        try:
            await comprehend_medical.describe_entities_detection_v2_job()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_comprehendmedical import AsyncComprehendMedicalClient


async def main():
    async with AsyncComprehendMedicalClient() as comprehend_medical:
        # Default: 3 attempts for every operation
        response = await comprehend_medical.describe_entities_detection_v2_job()

        # Override per operation
        response = await comprehend_medical.describe_entities_detection_v2_job(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await comprehend_medical.describe_entities_detection_v2_job(config_overrides={"retry_max_attempts": 1})
```
