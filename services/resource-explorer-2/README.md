# capo-resource-explorer-2: typed, async Python SDK for AWS Resource Explorer 2

`capo-resource-explorer-2` is a typed Python SDK for AWS Resource Explorer 2. It has an async client, `AsyncResourceExplorer2Client`, for asyncio and trio, and a sync client, `ResourceExplorer2Client`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/resource-explorer-2/](https://capo-sdk.dev/services/resource-explorer-2/)

## Installation

```
pip install capo-resource-explorer-2
```

## Usage

```python
from capo_resource_explorer_2 import AsyncResourceExplorer2Client


async def main():
    async with AsyncResourceExplorer2Client() as resource_explorer2:
        # Example: call the batch_get_view operation
        response = await resource_explorer2.batch_get_view()
        print(response["views"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_resource_explorer_2 import AsyncResourceExplorer2Client


async def main():
    async with AsyncResourceExplorer2Client() as resource_explorer2:
        # Example: paginate over get_resource_explorer_setup
        async for item in resource_explorer2.iter_get_resource_explorer_setup():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_resource_explorer_2 import AsyncResourceExplorer2Client
from capo_resource_explorer_2.error import AccessDeniedException


async def main():
    async with AsyncResourceExplorer2Client() as resource_explorer2:
        try:
            await resource_explorer2.batch_get_view()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_resource_explorer_2 import AsyncResourceExplorer2Client


async def main():
    async with AsyncResourceExplorer2Client() as resource_explorer2:
        # Default: 3 attempts for every operation
        response = await resource_explorer2.batch_get_view()

        # Override per operation
        response = await resource_explorer2.batch_get_view(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await resource_explorer2.batch_get_view(config_overrides={"retry_max_attempts": 1})
```
