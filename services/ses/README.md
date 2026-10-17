# capo-ses: typed, async Python SDK for AWS SES

`capo-ses` is a typed Python SDK for AWS SES. It has an async client, `AsyncSESClient`, for asyncio and trio, and a sync client, `SESClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/ses/](https://capo-sdk.dev/services/ses/)

## Installation

```
pip install capo-ses
```

## Usage

```python
from capo_ses import AsyncSESClient


async def main():
    async with AsyncSESClient() as ses:
        # Example: call the clone_receipt_rule_set operation
        response = await ses.clone_receipt_rule_set()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_ses import AsyncSESClient


async def main():
    async with AsyncSESClient() as ses:
        # Example: paginate over list_custom_verification_email_templates
        async for item in ses.iter_list_custom_verification_email_templates():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_ses import AsyncSESClient
from capo_ses.error import AlreadyExistsException


async def main():
    async with AsyncSESClient() as ses:
        try:
            await ses.clone_receipt_rule_set()
        except AlreadyExistsException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_ses import AsyncSESClient


async def main():
    async with AsyncSESClient() as ses:
        # Default: 3 attempts for every operation
        response = await ses.clone_receipt_rule_set()

        # Override per operation
        response = await ses.clone_receipt_rule_set(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await ses.clone_receipt_rule_set(config_overrides={"retry_max_attempts": 1})
```
