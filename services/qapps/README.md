# capo-qapps: typed, async Python SDK for AWS Qapps

`capo-qapps` is a typed Python SDK for AWS Qapps. It has an async client, `AsyncQAppsClient`, for asyncio and trio, and a sync client, `QAppsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/qapps/](https://capo-sdk.dev/services/qapps/)

## Installation

```
pip install capo-qapps
```

## Usage

```python
from capo_qapps import AsyncQAppsClient


async def main():
    async with AsyncQAppsClient() as q_apps:
        # Example: call the associate_library_item_review operation
        response = await q_apps.associate_library_item_review()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_qapps import AsyncQAppsClient


async def main():
    async with AsyncQAppsClient() as q_apps:
        # Example: paginate over list_library_items
        async for item in q_apps.iter_list_library_items():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_qapps import AsyncQAppsClient
from capo_qapps.error import AccessDeniedException


async def main():
    async with AsyncQAppsClient() as q_apps:
        try:
            await q_apps.associate_library_item_review()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_qapps import AsyncQAppsClient


async def main():
    async with AsyncQAppsClient() as q_apps:
        # Default: 3 attempts for every operation
        response = await q_apps.associate_library_item_review()

        # Override per operation
        response = await q_apps.associate_library_item_review(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await q_apps.associate_library_item_review(config_overrides={"retry_max_attempts": 1})
```
