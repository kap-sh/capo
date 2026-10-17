# capo-workmail: typed, async Python SDK for AWS Workmail

`capo-workmail` is a typed Python SDK for AWS Workmail. It has an async client, `AsyncWorkMailClient`, for asyncio and trio, and a sync client, `WorkMailClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/workmail/](https://capo-sdk.dev/services/workmail/)

## Installation

```
pip install capo-workmail
```

## Usage

```python
from capo_workmail import AsyncWorkMailClient


async def main():
    async with AsyncWorkMailClient() as work_mail:
        # Example: call the associate_delegate_to_resource operation
        response = await work_mail.associate_delegate_to_resource()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_workmail import AsyncWorkMailClient


async def main():
    async with AsyncWorkMailClient() as work_mail:
        # Example: paginate over list_aliases
        async for item in work_mail.iter_list_aliases():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_workmail import AsyncWorkMailClient
from capo_workmail.error import EntityNotFoundException


async def main():
    async with AsyncWorkMailClient() as work_mail:
        try:
            await work_mail.associate_delegate_to_resource()
        except EntityNotFoundException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_workmail import AsyncWorkMailClient


async def main():
    async with AsyncWorkMailClient() as work_mail:
        # Default: 3 attempts for every operation
        response = await work_mail.associate_delegate_to_resource()

        # Override per operation
        response = await work_mail.associate_delegate_to_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await work_mail.associate_delegate_to_resource(config_overrides={"retry_max_attempts": 1})
```
