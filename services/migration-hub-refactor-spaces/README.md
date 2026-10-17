# capo-migration-hub-refactor-spaces: typed, async Python SDK for AWS Migration Hub Refactor Spaces

`capo-migration-hub-refactor-spaces` is a typed Python SDK for AWS Migration Hub Refactor Spaces. It has an async client, `AsyncMigrationHubRefactorSpacesClient`, for asyncio and trio, and a sync client, `MigrationHubRefactorSpacesClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/migration-hub-refactor-spaces/](https://capo-sdk.dev/services/migration-hub-refactor-spaces/)

## Installation

```
pip install capo-migration-hub-refactor-spaces
```

## Usage

```python
from capo_migration_hub_refactor_spaces import AsyncMigrationHubRefactorSpacesClient


async def main():
    async with AsyncMigrationHubRefactorSpacesClient() as migration_hub_refactor_spaces:
        # Example: call the create_application operation
        response = await migration_hub_refactor_spaces.create_application()
        print(response["name"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_migration_hub_refactor_spaces import AsyncMigrationHubRefactorSpacesClient


async def main():
    async with AsyncMigrationHubRefactorSpacesClient() as migration_hub_refactor_spaces:
        # Example: paginate over list_applications
        async for item in migration_hub_refactor_spaces.iter_list_applications():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_migration_hub_refactor_spaces import AsyncMigrationHubRefactorSpacesClient
from capo_migration_hub_refactor_spaces.error import AccessDeniedException


async def main():
    async with AsyncMigrationHubRefactorSpacesClient() as migration_hub_refactor_spaces:
        try:
            await migration_hub_refactor_spaces.create_application()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_migration_hub_refactor_spaces import AsyncMigrationHubRefactorSpacesClient


async def main():
    async with AsyncMigrationHubRefactorSpacesClient() as migration_hub_refactor_spaces:
        # Default: 3 attempts for every operation
        response = await migration_hub_refactor_spaces.create_application()

        # Override per operation
        response = await migration_hub_refactor_spaces.create_application(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await migration_hub_refactor_spaces.create_application(config_overrides={"retry_max_attempts": 1})
```
