# capo-securitylake: typed, async Python SDK for AWS Securitylake

`capo-securitylake` is a typed Python SDK for AWS Securitylake. It has an async client, `AsyncSecurityLakeClient`, for asyncio and trio, and a sync client, `SecurityLakeClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/securitylake/](https://capo-sdk.dev/services/securitylake/)

## Installation

```
pip install capo-securitylake
```

## Usage

```python
from capo_securitylake import AsyncSecurityLakeClient


async def main():
    async with AsyncSecurityLakeClient() as security_lake:
        # Example: call the create_data_lake_exception_subscription operation
        response = await security_lake.create_data_lake_exception_subscription()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_securitylake import AsyncSecurityLakeClient


async def main():
    async with AsyncSecurityLakeClient() as security_lake:
        # Example: paginate over list_data_lake_exceptions
        async for item in security_lake.iter_list_data_lake_exceptions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_securitylake import AsyncSecurityLakeClient
from capo_securitylake.error import AccessDeniedException


async def main():
    async with AsyncSecurityLakeClient() as security_lake:
        try:
            await security_lake.create_data_lake_exception_subscription()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_securitylake import AsyncSecurityLakeClient


async def main():
    async with AsyncSecurityLakeClient() as security_lake:
        # Default: 3 attempts for every operation
        response = await security_lake.create_data_lake_exception_subscription()

        # Override per operation
        response = await security_lake.create_data_lake_exception_subscription(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await security_lake.create_data_lake_exception_subscription(config_overrides={"retry_max_attempts": 1})
```
