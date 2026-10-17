# capo-personalize-runtime: typed, async Python SDK for AWS Personalize Runtime

`capo-personalize-runtime` is a typed Python SDK for AWS Personalize Runtime. It has an async client, `AsyncPersonalizeRuntimeClient`, for asyncio and trio, and a sync client, `PersonalizeRuntimeClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/personalize-runtime/](https://capo-sdk.dev/services/personalize-runtime/)

## Installation

```
pip install capo-personalize-runtime
```

## Usage

```python
from capo_personalize_runtime import AsyncPersonalizeRuntimeClient


async def main():
    async with AsyncPersonalizeRuntimeClient() as personalize_runtime:
        # Example: call the get_action_recommendations operation
        response = await personalize_runtime.get_action_recommendations()
        print(response["action_list"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_personalize_runtime import AsyncPersonalizeRuntimeClient
from capo_personalize_runtime.error import InvalidInputException


async def main():
    async with AsyncPersonalizeRuntimeClient() as personalize_runtime:
        try:
            await personalize_runtime.get_action_recommendations()
        except InvalidInputException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_personalize_runtime import AsyncPersonalizeRuntimeClient


async def main():
    async with AsyncPersonalizeRuntimeClient() as personalize_runtime:
        # Default: 3 attempts for every operation
        response = await personalize_runtime.get_action_recommendations()

        # Override per operation
        response = await personalize_runtime.get_action_recommendations(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await personalize_runtime.get_action_recommendations(config_overrides={"retry_max_attempts": 1})
```
