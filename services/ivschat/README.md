# capo-ivschat: typed, async Python SDK for AWS Ivschat

`capo-ivschat` is a typed Python SDK for AWS Ivschat. It has an async client, `AsyncivschatClient`, for asyncio and trio, and a sync client, `ivschatClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/ivschat/](https://capo-sdk.dev/services/ivschat/)

## Installation

```
pip install capo-ivschat
```

## Usage

```python
from capo_ivschat import AsyncivschatClient


async def main():
    async with AsyncivschatClient() as ivschat:
        # Example: call the create_chat_token operation
        response = await ivschat.create_chat_token()
        print(response["token"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_ivschat import AsyncivschatClient


async def main():
    async with AsyncivschatClient() as ivschat:
        # Example: paginate over list_logging_configurations
        async for item in ivschat.iter_list_logging_configurations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_ivschat import AsyncivschatClient
from capo_ivschat.error import AccessDeniedException


async def main():
    async with AsyncivschatClient() as ivschat:
        try:
            await ivschat.create_chat_token()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_ivschat import AsyncivschatClient


async def main():
    async with AsyncivschatClient() as ivschat:
        # Default: 3 attempts for every operation
        response = await ivschat.create_chat_token()

        # Override per operation
        response = await ivschat.create_chat_token(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await ivschat.create_chat_token(config_overrides={"retry_max_attempts": 1})
```
