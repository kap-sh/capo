# capo-securityhub: typed, async Python SDK for AWS Securityhub

`capo-securityhub` is a typed Python SDK for AWS Securityhub. It has an async client, `AsyncSecurityHubClient`, for asyncio and trio, and a sync client, `SecurityHubClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/securityhub/](https://capo-sdk.dev/services/securityhub/)

## Installation

```
pip install capo-securityhub
```

## Usage

```python
from capo_securityhub import AsyncSecurityHubClient


async def main():
    async with AsyncSecurityHubClient() as security_hub:
        # Example: call the accept_administrator_invitation operation
        response = await security_hub.accept_administrator_invitation()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_securityhub import AsyncSecurityHubClient


async def main():
    async with AsyncSecurityHubClient() as security_hub:
        # Example: paginate over describe_action_targets
        async for item in security_hub.iter_describe_action_targets():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_securityhub import AsyncSecurityHubClient
from capo_securityhub.error import InternalException


async def main():
    async with AsyncSecurityHubClient() as security_hub:
        try:
            await security_hub.accept_administrator_invitation()
        except InternalException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_securityhub import AsyncSecurityHubClient


async def main():
    async with AsyncSecurityHubClient() as security_hub:
        # Default: 3 attempts for every operation
        response = await security_hub.accept_administrator_invitation()

        # Override per operation
        response = await security_hub.accept_administrator_invitation(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await security_hub.accept_administrator_invitation(config_overrides={"retry_max_attempts": 1})
```
