# capo-cognito-sync: typed, async Python SDK for AWS Cognito Sync

`capo-cognito-sync` is a typed Python SDK for AWS Cognito Sync. It has an async client, `AsyncCognitoSyncClient`, for asyncio and trio, and a sync client, `CognitoSyncClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cognito-sync/](https://capo-sdk.dev/services/cognito-sync/)

## Installation

```
pip install capo-cognito-sync
```

## Usage

```python
from capo_cognito_sync import AsyncCognitoSyncClient


async def main():
    async with AsyncCognitoSyncClient() as cognito_sync:
        # Example: call the bulk_publish operation
        response = await cognito_sync.bulk_publish()
        print(response["identity_pool_id"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cognito_sync import AsyncCognitoSyncClient
from capo_cognito_sync.error import AlreadyStreamedException


async def main():
    async with AsyncCognitoSyncClient() as cognito_sync:
        try:
            await cognito_sync.bulk_publish()
        except AlreadyStreamedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cognito_sync import AsyncCognitoSyncClient


async def main():
    async with AsyncCognitoSyncClient() as cognito_sync:
        # Default: 3 attempts for every operation
        response = await cognito_sync.bulk_publish()

        # Override per operation
        response = await cognito_sync.bulk_publish(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cognito_sync.bulk_publish(config_overrides={"retry_max_attempts": 1})
```
