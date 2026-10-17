# capo-cloudformation: typed, async Python SDK for AWS Cloudformation

`capo-cloudformation` is a typed Python SDK for AWS Cloudformation. It has an async client, `AsyncCloudFormationClient`, for asyncio and trio, and a sync client, `CloudFormationClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cloudformation/](https://capo-sdk.dev/services/cloudformation/)

## Installation

```
pip install capo-cloudformation
```

## Usage

```python
from capo_cloudformation import AsyncCloudFormationClient


async def main():
    async with AsyncCloudFormationClient() as cloud_formation:
        # Example: call the activate_organizations_access operation
        response = await cloud_formation.activate_organizations_access()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_cloudformation import AsyncCloudFormationClient


async def main():
    async with AsyncCloudFormationClient() as cloud_formation:
        # Example: paginate over describe_account_limits
        async for item in cloud_formation.iter_describe_account_limits():
            print(item)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_until_` prefixed method.

```python
from capo_cloudformation import AsyncCloudFormationClient


async def main():
    async with AsyncCloudFormationClient() as cloud_formation:
        # Example: wait for stack_exists
        await cloud_formation.wait_until_stack_exists(max_wait_time=300)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cloudformation import AsyncCloudFormationClient
from capo_cloudformation.error import InvalidOperationException


async def main():
    async with AsyncCloudFormationClient() as cloud_formation:
        try:
            await cloud_formation.activate_organizations_access()
        except InvalidOperationException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cloudformation import AsyncCloudFormationClient


async def main():
    async with AsyncCloudFormationClient() as cloud_formation:
        # Default: 3 attempts for every operation
        response = await cloud_formation.activate_organizations_access()

        # Override per operation
        response = await cloud_formation.activate_organizations_access(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cloud_formation.activate_organizations_access(config_overrides={"retry_max_attempts": 1})
```
