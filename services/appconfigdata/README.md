# capo-appconfigdata: typed, async Python SDK for AWS Appconfigdata

`capo-appconfigdata` is a typed Python SDK for AWS Appconfigdata. It has an async client, `AsyncAppConfigDataClient`, for asyncio and trio, and a sync client, `AppConfigDataClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/appconfigdata/](https://capo-sdk.dev/services/appconfigdata/)

## Installation

```
pip install capo-appconfigdata
```

## Usage

```python
from capo_appconfigdata import AsyncAppConfigDataClient


async def main():
    async with AsyncAppConfigDataClient() as app_config_data:
        # Example: call the get_latest_configuration operation
        response = await app_config_data.get_latest_configuration()
        print(response["next_poll_configuration_token"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_appconfigdata import AsyncAppConfigDataClient
from capo_appconfigdata.error import BadRequestException


async def main():
    async with AsyncAppConfigDataClient() as app_config_data:
        try:
            await app_config_data.get_latest_configuration()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_appconfigdata import AsyncAppConfigDataClient


async def main():
    async with AsyncAppConfigDataClient() as app_config_data:
        # Default: 3 attempts for every operation
        response = await app_config_data.get_latest_configuration()

        # Override per operation
        response = await app_config_data.get_latest_configuration(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await app_config_data.get_latest_configuration(config_overrides={"retry_max_attempts": 1})
```
