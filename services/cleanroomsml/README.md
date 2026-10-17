# capo-cleanroomsml: typed, async Python SDK for AWS Cleanroomsml

`capo-cleanroomsml` is a typed Python SDK for AWS Cleanroomsml. It has an async client, `AsyncCleanRoomsMLClient`, for asyncio and trio, and a sync client, `CleanRoomsMLClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cleanroomsml/](https://capo-sdk.dev/services/cleanroomsml/)

## Installation

```
pip install capo-cleanroomsml
```

## Usage

```python
from capo_cleanroomsml import AsyncCleanRoomsMLClient


async def main():
    async with AsyncCleanRoomsMLClient() as clean_rooms_ml:
        # Example: call the list_collaboration_configured_model_algorithm_associations operation
        response = await clean_rooms_ml.list_collaboration_configured_model_algorithm_associations()
        print(response["next_token"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_cleanroomsml import AsyncCleanRoomsMLClient


async def main():
    async with AsyncCleanRoomsMLClient() as clean_rooms_ml:
        # Example: paginate over list_collaboration_configured_model_algorithm_associations
        async for item in clean_rooms_ml.iter_list_collaboration_configured_model_algorithm_associations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cleanroomsml import AsyncCleanRoomsMLClient
from capo_cleanroomsml.error import AccessDeniedException


async def main():
    async with AsyncCleanRoomsMLClient() as clean_rooms_ml:
        try:
            await clean_rooms_ml.list_collaboration_configured_model_algorithm_associations()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cleanroomsml import AsyncCleanRoomsMLClient


async def main():
    async with AsyncCleanRoomsMLClient() as clean_rooms_ml:
        # Default: 3 attempts for every operation
        response = await clean_rooms_ml.list_collaboration_configured_model_algorithm_associations()

        # Override per operation
        response = await clean_rooms_ml.list_collaboration_configured_model_algorithm_associations(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await clean_rooms_ml.list_collaboration_configured_model_algorithm_associations(config_overrides={"retry_max_attempts": 1})
```
