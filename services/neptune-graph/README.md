# capo-neptune-graph: typed, async Python SDK for AWS Neptune Graph

`capo-neptune-graph` is a typed Python SDK for AWS Neptune Graph. It has an async client, `AsyncNeptuneGraphClient`, for asyncio and trio, and a sync client, `NeptuneGraphClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/neptune-graph/](https://capo-sdk.dev/services/neptune-graph/)

## Installation

```
pip install capo-neptune-graph
```

## Usage

```python
from capo_neptune_graph import AsyncNeptuneGraphClient


async def main():
    async with AsyncNeptuneGraphClient() as neptune_graph:
        # Example: call the cancel_query operation
        response = await neptune_graph.cancel_query()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_neptune_graph import AsyncNeptuneGraphClient


async def main():
    async with AsyncNeptuneGraphClient() as neptune_graph:
        # Example: paginate over list_graphs
        async for item in neptune_graph.iter_list_graphs():
            print(item)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_neptune_graph import AsyncNeptuneGraphClient


async def main():
    async with AsyncNeptuneGraphClient() as neptune_graph:
        # Example: call execute_query and read the streaming response
        async with neptune_graph.execute_query() as response:
            async for chunk in response["payload"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_neptune_graph import AsyncNeptuneGraphClient
from capo_neptune_graph.error import AccessDeniedException


async def main():
    async with AsyncNeptuneGraphClient() as neptune_graph:
        try:
            await neptune_graph.cancel_query()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_neptune_graph import AsyncNeptuneGraphClient


async def main():
    async with AsyncNeptuneGraphClient() as neptune_graph:
        # Default: 3 attempts for every operation
        response = await neptune_graph.cancel_query()

        # Override per operation
        response = await neptune_graph.cancel_query(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await neptune_graph.cancel_query(config_overrides={"retry_max_attempts": 1})
```
