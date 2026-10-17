# capo-frauddetector: typed, async Python SDK for AWS Frauddetector

`capo-frauddetector` is a typed Python SDK for AWS Frauddetector. It has an async client, `AsyncFraudDetectorClient`, for asyncio and trio, and a sync client, `FraudDetectorClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/frauddetector/](https://capo-sdk.dev/services/frauddetector/)

## Installation

```
pip install capo-frauddetector
```

## Usage

```python
from capo_frauddetector import AsyncFraudDetectorClient


async def main():
    async with AsyncFraudDetectorClient() as fraud_detector:
        # Example: call the batch_create_variable operation
        response = await fraud_detector.batch_create_variable()
        print(response["errors"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_frauddetector import AsyncFraudDetectorClient


async def main():
    async with AsyncFraudDetectorClient() as fraud_detector:
        # Example: paginate over describe_model_versions
        async for item in fraud_detector.iter_describe_model_versions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_frauddetector import AsyncFraudDetectorClient
from capo_frauddetector.error import AccessDeniedException


async def main():
    async with AsyncFraudDetectorClient() as fraud_detector:
        try:
            await fraud_detector.batch_create_variable()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_frauddetector import AsyncFraudDetectorClient


async def main():
    async with AsyncFraudDetectorClient() as fraud_detector:
        # Default: 3 attempts for every operation
        response = await fraud_detector.batch_create_variable()

        # Override per operation
        response = await fraud_detector.batch_create_variable(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await fraud_detector.batch_create_variable(config_overrides={"retry_max_attempts": 1})
```
