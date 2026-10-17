# capo-iam: typed, async Python SDK for AWS IAM

`capo-iam` is a typed Python SDK for AWS IAM. It has an async client, `AsyncIAMClient`, for asyncio and trio, and a sync client, `IAMClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/iam/](https://capo-sdk.dev/services/iam/)

## Installation

```
pip install capo-iam
```

## Usage

```python
from capo_iam import AsyncIAMClient


async def main():
    async with AsyncIAMClient() as iam:
        # Example: call the accept_delegation_request operation
        response = await iam.accept_delegation_request()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_iam import AsyncIAMClient


async def main():
    async with AsyncIAMClient() as iam:
        # Example: paginate over get_account_authorization_details
        async for item in iam.iter_get_account_authorization_details():
            print(item)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_until_` prefixed method.

```python
from capo_iam import AsyncIAMClient


async def main():
    async with AsyncIAMClient() as iam:
        # Example: wait for instance_profile_exists
        await iam.wait_until_instance_profile_exists(max_wait_time=300)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_iam import AsyncIAMClient
from capo_iam.error import ConcurrentModificationException


async def main():
    async with AsyncIAMClient() as iam:
        try:
            await iam.accept_delegation_request()
        except ConcurrentModificationException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_iam import AsyncIAMClient


async def main():
    async with AsyncIAMClient() as iam:
        # Default: 3 attempts for every operation
        response = await iam.accept_delegation_request()

        # Override per operation
        response = await iam.accept_delegation_request(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await iam.accept_delegation_request(config_overrides={"retry_max_attempts": 1})
```
