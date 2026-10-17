# capo-lakeformation: typed, async Python SDK for AWS Lakeformation

`capo-lakeformation` is a typed Python SDK for AWS Lakeformation. It has an async client, `AsyncLakeFormationClient`, for asyncio and trio, and a sync client, `LakeFormationClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/lakeformation/](https://capo-sdk.dev/services/lakeformation/)

## Installation

```
pip install capo-lakeformation
```

## Usage

```python
from capo_lakeformation import AsyncLakeFormationClient


async def main():
    async with AsyncLakeFormationClient() as lake_formation:
        # Example: call the add_lf_tags_to_resource operation
        response = await lake_formation.add_lf_tags_to_resource()
        print(response["failures"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_lakeformation import AsyncLakeFormationClient


async def main():
    async with AsyncLakeFormationClient() as lake_formation:
        # Example: paginate over get_effective_permissions_for_path
        async for item in lake_formation.iter_get_effective_permissions_for_path():
            print(item)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_lakeformation import AsyncLakeFormationClient


async def main():
    async with AsyncLakeFormationClient() as lake_formation:
        # Example: call get_work_unit_results and read the streaming response
        async with lake_formation.get_work_unit_results() as response:
            async for chunk in response["result_stream"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_lakeformation import AsyncLakeFormationClient
from capo_lakeformation.error import AccessDeniedException


async def main():
    async with AsyncLakeFormationClient() as lake_formation:
        try:
            await lake_formation.add_lf_tags_to_resource()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_lakeformation import AsyncLakeFormationClient


async def main():
    async with AsyncLakeFormationClient() as lake_formation:
        # Default: 3 attempts for every operation
        response = await lake_formation.add_lf_tags_to_resource()

        # Override per operation
        response = await lake_formation.add_lf_tags_to_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await lake_formation.add_lf_tags_to_resource(config_overrides={"retry_max_attempts": 1})
```
