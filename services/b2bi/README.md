# capo-b2bi: typed, async Python SDK for AWS B2Bi

`capo-b2bi` is a typed Python SDK for AWS B2Bi. It has an async client, `Asyncb2biClient`, for asyncio and trio, and a sync client, `b2biClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/b2bi/](https://capo-sdk.dev/services/b2bi/)

## Installation

```
pip install capo-b2bi
```

## Usage

```python
from capo_b2bi import Asyncb2biClient


async def main():
    async with Asyncb2biClient() as b2bi:
        # Example: call the create_starter_mapping_template operation
        response = await b2bi.create_starter_mapping_template()
        print(response["mapping_template"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_b2bi import Asyncb2biClient


async def main():
    async with Asyncb2biClient() as b2bi:
        # Example: paginate over list_capabilities
        async for item in b2bi.iter_list_capabilities():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_b2bi import Asyncb2biClient
from capo_b2bi.error import AccessDeniedException


async def main():
    async with Asyncb2biClient() as b2bi:
        try:
            await b2bi.create_starter_mapping_template()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_b2bi import Asyncb2biClient


async def main():
    async with Asyncb2biClient() as b2bi:
        # Default: 3 attempts for every operation
        response = await b2bi.create_starter_mapping_template()

        # Override per operation
        response = await b2bi.create_starter_mapping_template(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await b2bi.create_starter_mapping_template(config_overrides={"retry_max_attempts": 1})
```
