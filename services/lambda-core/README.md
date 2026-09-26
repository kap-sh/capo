# Getting Started

## Installation

```
pip install capo-lambda-core
```

## Usage

```python
from capo_lambda_core import AsyncLambdaCoreClient


async def main():
    async with AsyncLambdaCoreClient() as lambda_core:
        # Example: call the create_network_connector operation
        response = await lambda_core.create_network_connector()
        print(response["arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_lambda_core import AsyncLambdaCoreClient


async def main():
    async with AsyncLambdaCoreClient() as lambda_core:
        # Example: paginate over list_network_connectors
        async for item in lambda_core.iter_list_network_connectors():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_lambda_core import AsyncLambdaCoreClient
from capo_lambda_core.error import InvalidParameterValueException


async def main():
    async with AsyncLambdaCoreClient() as lambda_core:
        try:
            await lambda_core.create_network_connector()
        except InvalidParameterValueException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_lambda_core import AsyncLambdaCoreClient


async def main():
    async with AsyncLambdaCoreClient() as lambda_core:
        # Default: 3 attempts for every operation
        response = await lambda_core.create_network_connector()

        # Override per operation
        response = await lambda_core.create_network_connector(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await lambda_core.create_network_connector(config_overrides={"retry_max_attempts": 1})
```
