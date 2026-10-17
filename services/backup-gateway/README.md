# capo-backup-gateway: typed, async Python SDK for AWS Backup Gateway

`capo-backup-gateway` is a typed Python SDK for AWS Backup Gateway. It has an async client, `AsyncBackupGatewayClient`, for asyncio and trio, and a sync client, `BackupGatewayClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/backup-gateway/](https://capo-sdk.dev/services/backup-gateway/)

## Installation

```
pip install capo-backup-gateway
```

## Usage

```python
from capo_backup_gateway import AsyncBackupGatewayClient


async def main():
    async with AsyncBackupGatewayClient() as backup_gateway:
        # Example: call the list_tags_for_resource operation
        response = await backup_gateway.list_tags_for_resource()
        print(response["resource_arn"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_backup_gateway import AsyncBackupGatewayClient
from capo_backup_gateway.error import InternalServerException


async def main():
    async with AsyncBackupGatewayClient() as backup_gateway:
        try:
            await backup_gateway.list_tags_for_resource()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_backup_gateway import AsyncBackupGatewayClient


async def main():
    async with AsyncBackupGatewayClient() as backup_gateway:
        # Default: 3 attempts for every operation
        response = await backup_gateway.list_tags_for_resource()

        # Override per operation
        response = await backup_gateway.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await backup_gateway.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
