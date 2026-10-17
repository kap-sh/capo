# capo-support: typed, async Python SDK for AWS Support

`capo-support` is a typed Python SDK for AWS Support. It has an async client, `AsyncSupportClient`, for asyncio and trio, and a sync client, `SupportClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/support/](https://capo-sdk.dev/services/support/)

## Installation

```
pip install capo-support
```

## Usage

```python
from capo_support import AsyncSupportClient


async def main():
    async with AsyncSupportClient() as support:
        # Example: call the add_attachments_to_set operation
        response = await support.add_attachments_to_set()
        print(response["attachment_set_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_support import AsyncSupportClient


async def main():
    async with AsyncSupportClient() as support:
        # Example: paginate over describe_cases
        async for item in support.iter_describe_cases():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_support import AsyncSupportClient
from capo_support.error import AttachmentLimitExceeded


async def main():
    async with AsyncSupportClient() as support:
        try:
            await support.add_attachments_to_set()
        except AttachmentLimitExceeded as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_support import AsyncSupportClient


async def main():
    async with AsyncSupportClient() as support:
        # Default: 3 attempts for every operation
        response = await support.add_attachments_to_set()

        # Override per operation
        response = await support.add_attachments_to_set(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await support.add_attachments_to_set(config_overrides={"retry_max_attempts": 1})
```
