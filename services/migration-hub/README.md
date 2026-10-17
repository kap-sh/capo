# capo-migration-hub: typed, async Python SDK for AWS Migration Hub

`capo-migration-hub` is a typed Python SDK for AWS Migration Hub. It has an async client, `AsyncMigrationHubClient`, for asyncio and trio, and a sync client, `MigrationHubClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/migration-hub/](https://capo-sdk.dev/services/migration-hub/)

## Installation

```
pip install capo-migration-hub
```

## Usage

```python
from capo_migration_hub import AsyncMigrationHubClient


async def main():
    async with AsyncMigrationHubClient() as migration_hub:
        # Example: call the associate_created_artifact operation
        response = await migration_hub.associate_created_artifact()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_migration_hub import AsyncMigrationHubClient


async def main():
    async with AsyncMigrationHubClient() as migration_hub:
        # Example: paginate over list_application_states
        async for item in migration_hub.iter_list_application_states():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_migration_hub import AsyncMigrationHubClient
from capo_migration_hub.error import AccessDeniedException


async def main():
    async with AsyncMigrationHubClient() as migration_hub:
        try:
            await migration_hub.associate_created_artifact()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_migration_hub import AsyncMigrationHubClient


async def main():
    async with AsyncMigrationHubClient() as migration_hub:
        # Default: 3 attempts for every operation
        response = await migration_hub.associate_created_artifact()

        # Override per operation
        response = await migration_hub.associate_created_artifact(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await migration_hub.associate_created_artifact(config_overrides={"retry_max_attempts": 1})
```
