# capo-lightsail: typed, async Python SDK for AWS Lightsail

`capo-lightsail` is a typed Python SDK for AWS Lightsail. It has an async client, `AsyncLightsailClient`, for asyncio and trio, and a sync client, `LightsailClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/lightsail/](https://capo-sdk.dev/services/lightsail/)

## Installation

```
pip install capo-lightsail
```

## Usage

```python
from capo_lightsail import AsyncLightsailClient


async def main():
    async with AsyncLightsailClient() as lightsail:
        # Example: call the allocate_static_ip operation
        response = await lightsail.allocate_static_ip()
        print(response["operations"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_lightsail import AsyncLightsailClient
from capo_lightsail.error import AccessDeniedException


async def main():
    async with AsyncLightsailClient() as lightsail:
        try:
            await lightsail.allocate_static_ip()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_lightsail import AsyncLightsailClient


async def main():
    async with AsyncLightsailClient() as lightsail:
        # Default: 3 attempts for every operation
        response = await lightsail.allocate_static_ip()

        # Override per operation
        response = await lightsail.allocate_static_ip(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await lightsail.allocate_static_ip(config_overrides={"retry_max_attempts": 1})
```
