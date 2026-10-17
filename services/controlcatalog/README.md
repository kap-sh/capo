# capo-controlcatalog: typed, async Python SDK for AWS Controlcatalog

`capo-controlcatalog` is a typed Python SDK for AWS Controlcatalog. It has an async client, `AsyncControlCatalogClient`, for asyncio and trio, and a sync client, `ControlCatalogClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/controlcatalog/](https://capo-sdk.dev/services/controlcatalog/)

## Installation

```
pip install capo-controlcatalog
```

## Usage

```python
from capo_controlcatalog import AsyncControlCatalogClient


async def main():
    async with AsyncControlCatalogClient() as control_catalog:
        # Example: call the list_control_mappings operation
        response = await control_catalog.list_control_mappings()
        print(response["control_mappings"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_controlcatalog import AsyncControlCatalogClient


async def main():
    async with AsyncControlCatalogClient() as control_catalog:
        # Example: paginate over list_control_mappings
        async for item in control_catalog.iter_list_control_mappings():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_controlcatalog import AsyncControlCatalogClient
from capo_controlcatalog.error import AccessDeniedException


async def main():
    async with AsyncControlCatalogClient() as control_catalog:
        try:
            await control_catalog.list_control_mappings()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_controlcatalog import AsyncControlCatalogClient


async def main():
    async with AsyncControlCatalogClient() as control_catalog:
        # Default: 3 attempts for every operation
        response = await control_catalog.list_control_mappings()

        # Override per operation
        response = await control_catalog.list_control_mappings(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await control_catalog.list_control_mappings(config_overrides={"retry_max_attempts": 1})
```
