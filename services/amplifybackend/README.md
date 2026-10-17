# capo-amplifybackend: typed, async Python SDK for AWS Amplifybackend

`capo-amplifybackend` is a typed Python SDK for AWS Amplifybackend. It has an async client, `AsyncAmplifyBackendClient`, for asyncio and trio, and a sync client, `AmplifyBackendClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/amplifybackend/](https://capo-sdk.dev/services/amplifybackend/)

## Installation

```
pip install capo-amplifybackend
```

## Usage

```python
from capo_amplifybackend import AsyncAmplifyBackendClient


async def main():
    async with AsyncAmplifyBackendClient() as amplify_backend:
        # Example: call the clone_backend operation
        response = await amplify_backend.clone_backend()
        print(response["app_id"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_amplifybackend import AsyncAmplifyBackendClient
from capo_amplifybackend.error import BadRequestException


async def main():
    async with AsyncAmplifyBackendClient() as amplify_backend:
        try:
            await amplify_backend.clone_backend()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_amplifybackend import AsyncAmplifyBackendClient


async def main():
    async with AsyncAmplifyBackendClient() as amplify_backend:
        # Default: 3 attempts for every operation
        response = await amplify_backend.clone_backend()

        # Override per operation
        response = await amplify_backend.clone_backend(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await amplify_backend.clone_backend(config_overrides={"retry_max_attempts": 1})
```
