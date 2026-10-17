# capo-personalize-events: typed, async Python SDK for AWS Personalize Events

`capo-personalize-events` is a typed Python SDK for AWS Personalize Events. It has an async client, `AsyncPersonalizeEventsClient`, for asyncio and trio, and a sync client, `PersonalizeEventsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/personalize-events/](https://capo-sdk.dev/services/personalize-events/)

## Installation

```
pip install capo-personalize-events
```

## Usage

```python
from capo_personalize_events import AsyncPersonalizeEventsClient


async def main():
    async with AsyncPersonalizeEventsClient() as personalize_events:
        # Example: call the put_action_interactions operation
        response = await personalize_events.put_action_interactions()
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_personalize_events import AsyncPersonalizeEventsClient
from capo_personalize_events.error import InvalidInputException


async def main():
    async with AsyncPersonalizeEventsClient() as personalize_events:
        try:
            await personalize_events.put_action_interactions()
        except InvalidInputException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_personalize_events import AsyncPersonalizeEventsClient


async def main():
    async with AsyncPersonalizeEventsClient() as personalize_events:
        # Default: 3 attempts for every operation
        response = await personalize_events.put_action_interactions()

        # Override per operation
        response = await personalize_events.put_action_interactions(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await personalize_events.put_action_interactions(config_overrides={"retry_max_attempts": 1})
```
