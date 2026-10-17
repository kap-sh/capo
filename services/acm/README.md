# capo-acm: typed, async Python SDK for AWS ACM

`capo-acm` is a typed Python SDK for AWS ACM. It has an async client, `AsyncACMClient`, for asyncio and trio, and a sync client, `ACMClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/acm/](https://capo-sdk.dev/services/acm/)

## Installation

```
pip install capo-acm
```

## Usage

```python
from capo_acm import AsyncACMClient


async def main():
    async with AsyncACMClient() as acm:
        # Example: call the add_tags_to_certificate operation
        response = await acm.add_tags_to_certificate()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_acm import AsyncACMClient


async def main():
    async with AsyncACMClient() as acm:
        # Example: paginate over list_acme_accounts
        async for item in acm.iter_list_acme_accounts():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_acm import AsyncACMClient
from capo_acm.error import InvalidArnException


async def main():
    async with AsyncACMClient() as acm:
        try:
            await acm.add_tags_to_certificate()
        except InvalidArnException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_acm import AsyncACMClient


async def main():
    async with AsyncACMClient() as acm:
        # Default: 3 attempts for every operation
        response = await acm.add_tags_to_certificate()

        # Override per operation
        response = await acm.add_tags_to_certificate(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await acm.add_tags_to_certificate(config_overrides={"retry_max_attempts": 1})
```
