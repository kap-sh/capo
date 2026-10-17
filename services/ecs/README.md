# capo-ecs: typed, async Python SDK for Amazon ECS

`capo-ecs` is a typed Python SDK for Amazon ECS. It has an async client, `AsyncECSClient`, for asyncio and trio, and a sync client, `ECSClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/ecs/](https://capo-sdk.dev/services/ecs/)

## Installation

```
pip install capo-ecs
```

## Usage

```python
from capo_ecs import AsyncECSClient


async def main():
    async with AsyncECSClient() as ecs:
        # Example: call the continue_service_deployment operation
        response = await ecs.continue_service_deployment()
        print(response["service_deployment_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_ecs import AsyncECSClient


async def main():
    async with AsyncECSClient() as ecs:
        # Example: paginate over list_account_settings
        async for item in ecs.iter_list_account_settings():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_ecs import AsyncECSClient
from capo_ecs.error import AccessDeniedException


async def main():
    async with AsyncECSClient() as ecs:
        try:
            await ecs.continue_service_deployment()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_ecs import AsyncECSClient


async def main():
    async with AsyncECSClient() as ecs:
        # Default: 3 attempts for every operation
        response = await ecs.continue_service_deployment()

        # Override per operation
        response = await ecs.continue_service_deployment(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await ecs.continue_service_deployment(config_overrides={"retry_max_attempts": 1})
```
