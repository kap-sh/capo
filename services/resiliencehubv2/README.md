# capo-resiliencehubv2: typed, async Python SDK for AWS Resiliencehubv2

`capo-resiliencehubv2` is a typed Python SDK for AWS Resiliencehubv2. It has an async client, `Asyncresiliencehubv2Client`, for asyncio and trio, and a sync client, `resiliencehubv2Client`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/resiliencehubv2/](https://capo-sdk.dev/services/resiliencehubv2/)

## Installation

```
pip install capo-resiliencehubv2
```

## Usage

```python
from capo_resiliencehubv2 import Asyncresiliencehubv2Client


async def main():
    async with Asyncresiliencehubv2Client() as resiliencehubv2:
        # Example: call the create_assertion operation
        response = await resiliencehubv2.create_assertion()
        print(response["assertion"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_resiliencehubv2 import Asyncresiliencehubv2Client


async def main():
    async with Asyncresiliencehubv2Client() as resiliencehubv2:
        # Example: paginate over list_assertions
        async for item in resiliencehubv2.iter_list_assertions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_resiliencehubv2 import Asyncresiliencehubv2Client
from capo_resiliencehubv2.error import AccessDeniedException


async def main():
    async with Asyncresiliencehubv2Client() as resiliencehubv2:
        try:
            await resiliencehubv2.create_assertion()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_resiliencehubv2 import Asyncresiliencehubv2Client


async def main():
    async with Asyncresiliencehubv2Client() as resiliencehubv2:
        # Default: 3 attempts for every operation
        response = await resiliencehubv2.create_assertion()

        # Override per operation
        response = await resiliencehubv2.create_assertion(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await resiliencehubv2.create_assertion(config_overrides={"retry_max_attempts": 1})
```
