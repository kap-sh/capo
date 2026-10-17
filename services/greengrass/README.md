# capo-greengrass: typed, async Python SDK for AWS Greengrass

`capo-greengrass` is a typed Python SDK for AWS Greengrass. It has an async client, `AsyncGreengrassClient`, for asyncio and trio, and a sync client, `GreengrassClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/greengrass/](https://capo-sdk.dev/services/greengrass/)

## Installation

```
pip install capo-greengrass
```

## Usage

```python
from capo_greengrass import AsyncGreengrassClient


async def main():
    async with AsyncGreengrassClient() as greengrass:
        # Example: call the associate_role_to_group operation
        response = await greengrass.associate_role_to_group()
        print(response["associated_at"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_greengrass import AsyncGreengrassClient
from capo_greengrass.error import BadRequestException


async def main():
    async with AsyncGreengrassClient() as greengrass:
        try:
            await greengrass.associate_role_to_group()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_greengrass import AsyncGreengrassClient


async def main():
    async with AsyncGreengrassClient() as greengrass:
        # Default: 3 attempts for every operation
        response = await greengrass.associate_role_to_group()

        # Override per operation
        response = await greengrass.associate_role_to_group(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await greengrass.associate_role_to_group(config_overrides={"retry_max_attempts": 1})
```
