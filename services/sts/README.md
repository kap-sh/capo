# capo-sts: typed, async Python SDK for AWS STS

`capo-sts` is a typed Python SDK for AWS STS. It has an async client, `AsyncSTSClient`, for asyncio and trio, and a sync client, `STSClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/sts/](https://capo-sdk.dev/services/sts/)

## Installation

```
pip install capo-sts
```

## Usage

```python
from capo_sts import AsyncSTSClient


async def main():
    async with AsyncSTSClient() as sts:
        # Example: call the assume_role operation
        response = await sts.assume_role()
        print(response["credentials"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sts import AsyncSTSClient
from capo_sts.error import ExpiredTokenException


async def main():
    async with AsyncSTSClient() as sts:
        try:
            await sts.assume_role()
        except ExpiredTokenException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sts import AsyncSTSClient


async def main():
    async with AsyncSTSClient() as sts:
        # Default: 3 attempts for every operation
        response = await sts.assume_role()

        # Override per operation
        response = await sts.assume_role(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await sts.assume_role(config_overrides={"retry_max_attempts": 1})
```
