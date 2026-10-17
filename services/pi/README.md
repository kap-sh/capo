# capo-pi: typed, async Python SDK for AWS PI

`capo-pi` is a typed Python SDK for AWS PI. It has an async client, `AsyncPIClient`, for asyncio and trio, and a sync client, `PIClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/pi/](https://capo-sdk.dev/services/pi/)

## Installation

```
pip install capo-pi
```

## Usage

```python
from capo_pi import AsyncPIClient


async def main():
    async with AsyncPIClient() as pi:
        # Example: call the create_performance_analysis_report operation
        response = await pi.create_performance_analysis_report()
        print(response["analysis_report_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_pi import AsyncPIClient


async def main():
    async with AsyncPIClient() as pi:
        # Example: paginate over describe_dimension_keys
        async for item in pi.iter_describe_dimension_keys():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_pi import AsyncPIClient
from capo_pi.error import InternalServiceError


async def main():
    async with AsyncPIClient() as pi:
        try:
            await pi.create_performance_analysis_report()
        except InternalServiceError as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_pi import AsyncPIClient


async def main():
    async with AsyncPIClient() as pi:
        # Default: 3 attempts for every operation
        response = await pi.create_performance_analysis_report()

        # Override per operation
        response = await pi.create_performance_analysis_report(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await pi.create_performance_analysis_report(config_overrides={"retry_max_attempts": 1})
```
