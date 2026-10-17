# capo-fis: typed, async Python SDK for AWS FIS

`capo-fis` is a typed Python SDK for AWS FIS. It has an async client, `AsyncfisClient`, for asyncio and trio, and a sync client, `fisClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/fis/](https://capo-sdk.dev/services/fis/)

## Installation

```
pip install capo-fis
```

## Usage

```python
from capo_fis import AsyncfisClient


async def main():
    async with AsyncfisClient() as fis:
        # Example: call the create_experiment_template operation
        response = await fis.create_experiment_template()
        print(response["experiment_template"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_fis import AsyncfisClient


async def main():
    async with AsyncfisClient() as fis:
        # Example: paginate over list_actions
        async for item in fis.iter_list_actions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_fis import AsyncfisClient
from capo_fis.error import ConflictException


async def main():
    async with AsyncfisClient() as fis:
        try:
            await fis.create_experiment_template()
        except ConflictException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_fis import AsyncfisClient


async def main():
    async with AsyncfisClient() as fis:
        # Default: 3 attempts for every operation
        response = await fis.create_experiment_template()

        # Override per operation
        response = await fis.create_experiment_template(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await fis.create_experiment_template(config_overrides={"retry_max_attempts": 1})
```
