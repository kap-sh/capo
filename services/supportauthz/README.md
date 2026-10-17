# capo-supportauthz: typed, async Python SDK for AWS SupportAuthZ

`capo-supportauthz` is a typed Python SDK for AWS SupportAuthZ. It has an async client, `AsyncSupportAuthZClient`, for asyncio and trio, and a sync client, `SupportAuthZClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/supportauthz/](https://capo-sdk.dev/services/supportauthz/)

## Installation

```
pip install capo-supportauthz
```

## Usage

```python
from capo_supportauthz import AsyncSupportAuthZClient


async def main():
    async with AsyncSupportAuthZClient() as support_auth_z:
        # Example: call the create_support_permit operation
        response = await support_auth_z.create_support_permit()
        print(response["name"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_supportauthz import AsyncSupportAuthZClient


async def main():
    async with AsyncSupportAuthZClient() as support_auth_z:
        # Example: paginate over list_actions
        async for item in support_auth_z.iter_list_actions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_supportauthz import AsyncSupportAuthZClient
from capo_supportauthz.error import AccessDeniedException


async def main():
    async with AsyncSupportAuthZClient() as support_auth_z:
        try:
            await support_auth_z.create_support_permit()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_supportauthz import AsyncSupportAuthZClient


async def main():
    async with AsyncSupportAuthZClient() as support_auth_z:
        # Default: 3 attempts for every operation
        response = await support_auth_z.create_support_permit()

        # Override per operation
        response = await support_auth_z.create_support_permit(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await support_auth_z.create_support_permit(config_overrides={"retry_max_attempts": 1})
```
