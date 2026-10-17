# capo-migrationhuborchestrator: typed, async Python SDK for AWS Migrationhuborchestrator

`capo-migrationhuborchestrator` is a typed Python SDK for AWS Migrationhuborchestrator. It has an async client, `AsyncMigrationHubOrchestratorClient`, for asyncio and trio, and a sync client, `MigrationHubOrchestratorClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/migrationhuborchestrator/](https://capo-sdk.dev/services/migrationhuborchestrator/)

## Installation

```
pip install capo-migrationhuborchestrator
```

## Usage

```python
from capo_migrationhuborchestrator import AsyncMigrationHubOrchestratorClient


async def main():
    async with AsyncMigrationHubOrchestratorClient() as migration_hub_orchestrator:
        # Example: call the list_tags_for_resource operation
        response = await migration_hub_orchestrator.list_tags_for_resource()
        print(response["tags"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_migrationhuborchestrator import AsyncMigrationHubOrchestratorClient


async def main():
    async with AsyncMigrationHubOrchestratorClient() as migration_hub_orchestrator:
        # Example: paginate over list_workflows
        async for item in migration_hub_orchestrator.iter_list_workflows():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_migrationhuborchestrator import AsyncMigrationHubOrchestratorClient
from capo_migrationhuborchestrator.error import ResourceNotFoundException


async def main():
    async with AsyncMigrationHubOrchestratorClient() as migration_hub_orchestrator:
        try:
            await migration_hub_orchestrator.list_tags_for_resource()
        except ResourceNotFoundException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_migrationhuborchestrator import AsyncMigrationHubOrchestratorClient


async def main():
    async with AsyncMigrationHubOrchestratorClient() as migration_hub_orchestrator:
        # Default: 3 attempts for every operation
        response = await migration_hub_orchestrator.list_tags_for_resource()

        # Override per operation
        response = await migration_hub_orchestrator.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await migration_hub_orchestrator.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
