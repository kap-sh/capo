# capo-osis: typed, async Python SDK for AWS OSIS

`capo-osis` is a typed Python SDK for AWS OSIS. It has an async client, `AsyncOSISClient`, for asyncio and trio, and a sync client, `OSISClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/osis/](https://capo-sdk.dev/services/osis/)

## Installation

```
pip install capo-osis
```

## Usage

```python
from capo_osis import AsyncOSISClient


async def main():
    async with AsyncOSISClient() as osis:
        # Example: call the create_pipeline operation
        response = await osis.create_pipeline()
        print(response["pipeline"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_osis import AsyncOSISClient


async def main():
    async with AsyncOSISClient() as osis:
        # Example: paginate over list_pipeline_endpoint_connections
        async for item in osis.iter_list_pipeline_endpoint_connections():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_osis import AsyncOSISClient
from capo_osis.error import AccessDeniedException


async def main():
    async with AsyncOSISClient() as osis:
        try:
            await osis.create_pipeline()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_osis import AsyncOSISClient


async def main():
    async with AsyncOSISClient() as osis:
        # Default: 3 attempts for every operation
        response = await osis.create_pipeline()

        # Override per operation
        response = await osis.create_pipeline(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await osis.create_pipeline(config_overrides={"retry_max_attempts": 1})
```
