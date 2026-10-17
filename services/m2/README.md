# capo-m2: typed, async Python SDK for AWS M2

`capo-m2` is a typed Python SDK for AWS M2. It has an async client, `Asyncm2Client`, for asyncio and trio, and a sync client, `m2Client`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/m2/](https://capo-sdk.dev/services/m2/)

## Installation

```
pip install capo-m2
```

## Usage

```python
from capo_m2 import Asyncm2Client


async def main():
    async with Asyncm2Client() as m2:
        # Example: call the get_signed_bluinsights_url operation
        response = await m2.get_signed_bluinsights_url()
        print(response["signed_bi_url"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_m2 import Asyncm2Client


async def main():
    async with Asyncm2Client() as m2:
        # Example: paginate over list_engine_versions
        async for item in m2.iter_list_engine_versions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_m2 import Asyncm2Client
from capo_m2.error import AccessDeniedException


async def main():
    async with Asyncm2Client() as m2:
        try:
            await m2.get_signed_bluinsights_url()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_m2 import Asyncm2Client


async def main():
    async with Asyncm2Client() as m2:
        # Default: 3 attempts for every operation
        response = await m2.get_signed_bluinsights_url()

        # Override per operation
        response = await m2.get_signed_bluinsights_url(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await m2.get_signed_bluinsights_url(config_overrides={"retry_max_attempts": 1})
```
