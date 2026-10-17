# capo-secrets-manager: typed, async Python SDK for AWS Secrets Manager

`capo-secrets-manager` is a typed Python SDK for AWS Secrets Manager. It has an async client, `AsyncSecretsManagerClient`, for asyncio and trio, and a sync client, `SecretsManagerClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/secrets-manager/](https://capo-sdk.dev/services/secrets-manager/)

## Installation

```
pip install capo-secrets-manager
```

## Usage

```python
from capo_secrets_manager import AsyncSecretsManagerClient


async def main():
    async with AsyncSecretsManagerClient() as secrets_manager:
        # Example: call the batch_get_secret_value operation
        response = await secrets_manager.batch_get_secret_value()
        print(response["secret_values"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_secrets_manager import AsyncSecretsManagerClient


async def main():
    async with AsyncSecretsManagerClient() as secrets_manager:
        # Example: paginate over batch_get_secret_value
        async for item in secrets_manager.iter_batch_get_secret_value():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_secrets_manager import AsyncSecretsManagerClient
from capo_secrets_manager.error import DecryptionFailure


async def main():
    async with AsyncSecretsManagerClient() as secrets_manager:
        try:
            await secrets_manager.batch_get_secret_value()
        except DecryptionFailure as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_secrets_manager import AsyncSecretsManagerClient


async def main():
    async with AsyncSecretsManagerClient() as secrets_manager:
        # Default: 3 attempts for every operation
        response = await secrets_manager.batch_get_secret_value()

        # Override per operation
        response = await secrets_manager.batch_get_secret_value(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await secrets_manager.batch_get_secret_value(config_overrides={"retry_max_attempts": 1})
```
