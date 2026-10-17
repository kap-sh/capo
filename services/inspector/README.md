# capo-inspector: typed, async Python SDK for AWS Inspector

`capo-inspector` is a typed Python SDK for AWS Inspector. It has an async client, `AsyncInspectorClient`, for asyncio and trio, and a sync client, `InspectorClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/inspector/](https://capo-sdk.dev/services/inspector/)

## Installation

```
pip install capo-inspector
```

## Usage

```python
from capo_inspector import AsyncInspectorClient


async def main():
    async with AsyncInspectorClient() as inspector:
        # Example: call the add_attributes_to_findings operation
        response = await inspector.add_attributes_to_findings()
        print(response["failed_items"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_inspector import AsyncInspectorClient


async def main():
    async with AsyncInspectorClient() as inspector:
        # Example: paginate over get_exclusions_preview
        async for item in inspector.iter_get_exclusions_preview():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_inspector import AsyncInspectorClient
from capo_inspector.error import AccessDeniedException


async def main():
    async with AsyncInspectorClient() as inspector:
        try:
            await inspector.add_attributes_to_findings()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_inspector import AsyncInspectorClient


async def main():
    async with AsyncInspectorClient() as inspector:
        # Default: 3 attempts for every operation
        response = await inspector.add_attributes_to_findings()

        # Override per operation
        response = await inspector.add_attributes_to_findings(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await inspector.add_attributes_to_findings(config_overrides={"retry_max_attempts": 1})
```
