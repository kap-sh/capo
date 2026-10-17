# capo-cloud9: typed, async Python SDK for AWS Cloud9

`capo-cloud9` is a typed Python SDK for AWS Cloud9. It has an async client, `AsyncCloud9Client`, for asyncio and trio, and a sync client, `Cloud9Client`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cloud9/](https://capo-sdk.dev/services/cloud9/)

## Installation

```
pip install capo-cloud9
```

## Usage

```python
from capo_cloud9 import AsyncCloud9Client


async def main():
    async with AsyncCloud9Client() as cloud9:
        # Example: call the create_environment_ec2 operation
        response = await cloud9.create_environment_ec2()
        print(response["environment_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_cloud9 import AsyncCloud9Client


async def main():
    async with AsyncCloud9Client() as cloud9:
        # Example: paginate over describe_environment_memberships
        async for item in cloud9.iter_describe_environment_memberships():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cloud9 import AsyncCloud9Client
from capo_cloud9.error import BadRequestException


async def main():
    async with AsyncCloud9Client() as cloud9:
        try:
            await cloud9.create_environment_ec2()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cloud9 import AsyncCloud9Client


async def main():
    async with AsyncCloud9Client() as cloud9:
        # Default: 3 attempts for every operation
        response = await cloud9.create_environment_ec2()

        # Override per operation
        response = await cloud9.create_environment_ec2(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cloud9.create_environment_ec2(config_overrides={"retry_max_attempts": 1})
```
