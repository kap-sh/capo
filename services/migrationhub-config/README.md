# capo-migrationhub-config: typed, async Python SDK for AWS Migrationhub Config

`capo-migrationhub-config` is a typed Python SDK for AWS Migrationhub Config. It has an async client, `AsyncMigrationHubConfigClient`, for asyncio and trio, and a sync client, `MigrationHubConfigClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/migrationhub-config/](https://capo-sdk.dev/services/migrationhub-config/)

## Installation

```
pip install capo-migrationhub-config
```

## Usage

```python
from capo_migrationhub_config import AsyncMigrationHubConfigClient


async def main():
    async with AsyncMigrationHubConfigClient() as migration_hub_config:
        # Example: call the create_home_region_control operation
        response = await migration_hub_config.create_home_region_control()
        print(response["home_region_control"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_migrationhub_config import AsyncMigrationHubConfigClient


async def main():
    async with AsyncMigrationHubConfigClient() as migration_hub_config:
        # Example: paginate over describe_home_region_controls
        async for item in migration_hub_config.iter_describe_home_region_controls():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_migrationhub_config import AsyncMigrationHubConfigClient
from capo_migrationhub_config.error import AccessDeniedException


async def main():
    async with AsyncMigrationHubConfigClient() as migration_hub_config:
        try:
            await migration_hub_config.create_home_region_control()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_migrationhub_config import AsyncMigrationHubConfigClient


async def main():
    async with AsyncMigrationHubConfigClient() as migration_hub_config:
        # Default: 3 attempts for every operation
        response = await migration_hub_config.create_home_region_control()

        # Override per operation
        response = await migration_hub_config.create_home_region_control(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await migration_hub_config.create_home_region_control(config_overrides={"retry_max_attempts": 1})
```
