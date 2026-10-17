# capo-sns: typed, async Python SDK for AWS SNS

`capo-sns` is a typed Python SDK for AWS SNS. It has an async client, `AsyncSNSClient`, for asyncio and trio, and a sync client, `SNSClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/sns/](https://capo-sdk.dev/services/sns/)

## Installation

```
pip install capo-sns
```

## Usage

```python
from capo_sns import AsyncSNSClient


async def main():
    async with AsyncSNSClient() as sns:
        # Example: call the add_permission operation
        response = await sns.add_permission()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_sns import AsyncSNSClient


async def main():
    async with AsyncSNSClient() as sns:
        # Example: paginate over list_endpoints_by_platform_application
        async for item in sns.iter_list_endpoints_by_platform_application():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sns import AsyncSNSClient
from capo_sns.error import AuthorizationErrorException


async def main():
    async with AsyncSNSClient() as sns:
        try:
            await sns.add_permission()
        except AuthorizationErrorException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sns import AsyncSNSClient


async def main():
    async with AsyncSNSClient() as sns:
        # Default: 3 attempts for every operation
        response = await sns.add_permission()

        # Override per operation
        response = await sns.add_permission(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await sns.add_permission(config_overrides={"retry_max_attempts": 1})
```
