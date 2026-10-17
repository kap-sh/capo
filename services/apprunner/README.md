# capo-apprunner: typed, async Python SDK for AWS Apprunner

`capo-apprunner` is a typed Python SDK for AWS Apprunner. It has an async client, `AsyncAppRunnerClient`, for asyncio and trio, and a sync client, `AppRunnerClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/apprunner/](https://capo-sdk.dev/services/apprunner/)

## Installation

```
pip install capo-apprunner
```

## Usage

```python
from capo_apprunner import AsyncAppRunnerClient


async def main():
    async with AsyncAppRunnerClient() as app_runner:
        # Example: call the associate_custom_domain operation
        response = await app_runner.associate_custom_domain()
        print(response["dns_target"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_apprunner import AsyncAppRunnerClient


async def main():
    async with AsyncAppRunnerClient() as app_runner:
        # Example: paginate over describe_custom_domains
        async for item in app_runner.iter_describe_custom_domains():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_apprunner import AsyncAppRunnerClient
from capo_apprunner.error import InternalServiceErrorException


async def main():
    async with AsyncAppRunnerClient() as app_runner:
        try:
            await app_runner.associate_custom_domain()
        except InternalServiceErrorException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_apprunner import AsyncAppRunnerClient


async def main():
    async with AsyncAppRunnerClient() as app_runner:
        # Default: 3 attempts for every operation
        response = await app_runner.associate_custom_domain()

        # Override per operation
        response = await app_runner.associate_custom_domain(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await app_runner.associate_custom_domain(config_overrides={"retry_max_attempts": 1})
```
