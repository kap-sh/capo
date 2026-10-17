# capo-amplify: typed, async Python SDK for AWS Amplify

`capo-amplify` is a typed Python SDK for AWS Amplify. It has an async client, `AsyncAmplifyClient`, for asyncio and trio, and a sync client, `AmplifyClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/amplify/](https://capo-sdk.dev/services/amplify/)

## Installation

```
pip install capo-amplify
```

## Usage

```python
from capo_amplify import AsyncAmplifyClient


async def main():
    async with AsyncAmplifyClient() as amplify:
        # Example: call the create_app operation
        response = await amplify.create_app()
        print(response["app"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_amplify import AsyncAmplifyClient


async def main():
    async with AsyncAmplifyClient() as amplify:
        # Example: paginate over list_apps
        async for item in amplify.iter_list_apps():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_amplify import AsyncAmplifyClient
from capo_amplify.error import BadRequestException


async def main():
    async with AsyncAmplifyClient() as amplify:
        try:
            await amplify.create_app()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_amplify import AsyncAmplifyClient


async def main():
    async with AsyncAmplifyClient() as amplify:
        # Default: 3 attempts for every operation
        response = await amplify.create_app()

        # Override per operation
        response = await amplify.create_app(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await amplify.create_app(config_overrides={"retry_max_attempts": 1})
```
