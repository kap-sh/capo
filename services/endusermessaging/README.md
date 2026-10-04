# Getting Started

## Installation

```
pip install capo-endusermessaging
```

## Usage

```python
from capo_endusermessaging import AsyncEndUserMessagingClient


async def main():
    async with AsyncEndUserMessagingClient() as end_user_messaging:
        # Example: call the create_brand_profile operation
        response = await end_user_messaging.create_brand_profile()
        print(response["brand_profile_id"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_endusermessaging import AsyncEndUserMessagingClient
from capo_endusermessaging.error import AccessDeniedException


async def main():
    async with AsyncEndUserMessagingClient() as end_user_messaging:
        try:
            await end_user_messaging.create_brand_profile()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_endusermessaging import AsyncEndUserMessagingClient


async def main():
    async with AsyncEndUserMessagingClient() as end_user_messaging:
        # Default: 3 attempts for every operation
        response = await end_user_messaging.create_brand_profile()

        # Override per operation
        response = await end_user_messaging.create_brand_profile(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await end_user_messaging.create_brand_profile(config_overrides={"retry_max_attempts": 1})
```
