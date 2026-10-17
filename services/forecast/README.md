# capo-forecast: typed, async Python SDK for AWS Forecast

`capo-forecast` is a typed Python SDK for AWS Forecast. It has an async client, `AsyncforecastClient`, for asyncio and trio, and a sync client, `forecastClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/forecast/](https://capo-sdk.dev/services/forecast/)

## Installation

```
pip install capo-forecast
```

## Usage

```python
from capo_forecast import AsyncforecastClient


async def main():
    async with AsyncforecastClient() as forecast:
        # Example: call the create_auto_predictor operation
        response = await forecast.create_auto_predictor()
        print(response["predictor_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_forecast import AsyncforecastClient


async def main():
    async with AsyncforecastClient() as forecast:
        # Example: paginate over list_dataset_groups
        async for item in forecast.iter_list_dataset_groups():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_forecast import AsyncforecastClient
from capo_forecast.error import InvalidInputException


async def main():
    async with AsyncforecastClient() as forecast:
        try:
            await forecast.create_auto_predictor()
        except InvalidInputException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_forecast import AsyncforecastClient


async def main():
    async with AsyncforecastClient() as forecast:
        # Default: 3 attempts for every operation
        response = await forecast.create_auto_predictor()

        # Override per operation
        response = await forecast.create_auto_predictor(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await forecast.create_auto_predictor(config_overrides={"retry_max_attempts": 1})
```
