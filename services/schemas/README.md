# capo-schemas: typed, async Python SDK for AWS Schemas

`capo-schemas` is a typed Python SDK for AWS Schemas. It has an async client, `AsyncschemasClient`, for asyncio and trio, and a sync client, `schemasClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/schemas/](https://capo-sdk.dev/services/schemas/)

## Installation

```
pip install capo-schemas
```

## Usage

```python
from capo_schemas import AsyncschemasClient


async def main():
    async with AsyncschemasClient() as schemas:
        # Example: call the create_discoverer operation
        response = await schemas.create_discoverer()
        print(response["description"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_schemas import AsyncschemasClient


async def main():
    async with AsyncschemasClient() as schemas:
        # Example: paginate over list_discoverers
        async for item in schemas.iter_list_discoverers():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_schemas import AsyncschemasClient
from capo_schemas.error import BadRequestException


async def main():
    async with AsyncschemasClient() as schemas:
        try:
            await schemas.create_discoverer()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_schemas import AsyncschemasClient


async def main():
    async with AsyncschemasClient() as schemas:
        # Default: 3 attempts for every operation
        response = await schemas.create_discoverer()

        # Override per operation
        response = await schemas.create_discoverer(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await schemas.create_discoverer(config_overrides={"retry_max_attempts": 1})
```
