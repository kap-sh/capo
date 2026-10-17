# capo-connect: typed, async Python SDK for AWS Connect

`capo-connect` is a typed Python SDK for AWS Connect. It has an async client, `AsyncConnectClient`, for asyncio and trio, and a sync client, `ConnectClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/connect/](https://capo-sdk.dev/services/connect/)

## Installation

```
pip install capo-connect
```

## Usage

```python
from capo_connect import AsyncConnectClient


async def main():
    async with AsyncConnectClient() as connect:
        # Example: call the activate_evaluation_form operation
        response = await connect.activate_evaluation_form()
        print(response["evaluation_form_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_connect import AsyncConnectClient


async def main():
    async with AsyncConnectClient() as connect:
        # Example: paginate over evaluate_data_table_values
        async for item in connect.iter_evaluate_data_table_values():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_connect import AsyncConnectClient
from capo_connect.error import InternalServiceException


async def main():
    async with AsyncConnectClient() as connect:
        try:
            await connect.activate_evaluation_form()
        except InternalServiceException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_connect import AsyncConnectClient


async def main():
    async with AsyncConnectClient() as connect:
        # Default: 3 attempts for every operation
        response = await connect.activate_evaluation_form()

        # Override per operation
        response = await connect.activate_evaluation_form(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await connect.activate_evaluation_form(config_overrides={"retry_max_attempts": 1})
```
