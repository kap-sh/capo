# capo-glue: typed, async Python SDK for AWS Glue

`capo-glue` is a typed Python SDK for AWS Glue. It has an async client, `AsyncGlueClient`, for asyncio and trio, and a sync client, `GlueClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/glue/](https://capo-sdk.dev/services/glue/)

## Installation

```
pip install capo-glue
```

## Usage

```python
from capo_glue import AsyncGlueClient


async def main():
    async with AsyncGlueClient() as glue:
        # Example: call the associate_glossary_terms operation
        response = await glue.associate_glossary_terms()
        print(response["asset_identifier"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_glue import AsyncGlueClient


async def main():
    async with AsyncGlueClient() as glue:
        # Example: paginate over describe_entity
        async for item in glue.iter_describe_entity():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_glue import AsyncGlueClient
from capo_glue.error import AccessDeniedException


async def main():
    async with AsyncGlueClient() as glue:
        try:
            await glue.associate_glossary_terms()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_glue import AsyncGlueClient


async def main():
    async with AsyncGlueClient() as glue:
        # Default: 3 attempts for every operation
        response = await glue.associate_glossary_terms()

        # Override per operation
        response = await glue.associate_glossary_terms(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await glue.associate_glossary_terms(config_overrides={"retry_max_attempts": 1})
```
