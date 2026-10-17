# capo-databrew: typed, async Python SDK for AWS Databrew

`capo-databrew` is a typed Python SDK for AWS Databrew. It has an async client, `AsyncDataBrewClient`, for asyncio and trio, and a sync client, `DataBrewClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/databrew/](https://capo-sdk.dev/services/databrew/)

## Installation

```
pip install capo-databrew
```

## Usage

```python
from capo_databrew import AsyncDataBrewClient


async def main():
    async with AsyncDataBrewClient() as data_brew:
        # Example: call the batch_delete_recipe_version operation
        response = await data_brew.batch_delete_recipe_version()
        print(response["name"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_databrew import AsyncDataBrewClient


async def main():
    async with AsyncDataBrewClient() as data_brew:
        # Example: paginate over list_datasets
        async for item in data_brew.iter_list_datasets():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_databrew import AsyncDataBrewClient
from capo_databrew.error import ConflictException


async def main():
    async with AsyncDataBrewClient() as data_brew:
        try:
            await data_brew.batch_delete_recipe_version()
        except ConflictException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_databrew import AsyncDataBrewClient


async def main():
    async with AsyncDataBrewClient() as data_brew:
        # Default: 3 attempts for every operation
        response = await data_brew.batch_delete_recipe_version()

        # Override per operation
        response = await data_brew.batch_delete_recipe_version(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await data_brew.batch_delete_recipe_version(config_overrides={"retry_max_attempts": 1})
```
