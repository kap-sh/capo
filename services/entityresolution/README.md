# capo-entityresolution: typed, async Python SDK for AWS Entityresolution

`capo-entityresolution` is a typed Python SDK for AWS Entityresolution. It has an async client, `AsyncEntityResolutionClient`, for asyncio and trio, and a sync client, `EntityResolutionClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/entityresolution/](https://capo-sdk.dev/services/entityresolution/)

## Installation

```
pip install capo-entityresolution
```

## Usage

```python
from capo_entityresolution import AsyncEntityResolutionClient


async def main():
    async with AsyncEntityResolutionClient() as entity_resolution:
        # Example: call the add_policy_statement operation
        response = await entity_resolution.add_policy_statement()
        print(response["arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_entityresolution import AsyncEntityResolutionClient


async def main():
    async with AsyncEntityResolutionClient() as entity_resolution:
        # Example: paginate over list_id_mapping_jobs
        async for item in entity_resolution.iter_list_id_mapping_jobs():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_entityresolution import AsyncEntityResolutionClient
from capo_entityresolution.error import AccessDeniedException


async def main():
    async with AsyncEntityResolutionClient() as entity_resolution:
        try:
            await entity_resolution.add_policy_statement()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_entityresolution import AsyncEntityResolutionClient


async def main():
    async with AsyncEntityResolutionClient() as entity_resolution:
        # Default: 3 attempts for every operation
        response = await entity_resolution.add_policy_statement()

        # Override per operation
        response = await entity_resolution.add_policy_statement(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await entity_resolution.add_policy_statement(config_overrides={"retry_max_attempts": 1})
```
