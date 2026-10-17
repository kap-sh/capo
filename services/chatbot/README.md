# capo-chatbot: typed, async Python SDK for AWS Chatbot

`capo-chatbot` is a typed Python SDK for AWS Chatbot. It has an async client, `AsyncchatbotClient`, for asyncio and trio, and a sync client, `chatbotClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/chatbot/](https://capo-sdk.dev/services/chatbot/)

## Installation

```
pip install capo-chatbot
```

## Usage

```python
from capo_chatbot import AsyncchatbotClient


async def main():
    async with AsyncchatbotClient() as chatbot:
        # Example: call the associate_to_configuration operation
        response = await chatbot.associate_to_configuration()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_chatbot import AsyncchatbotClient


async def main():
    async with AsyncchatbotClient() as chatbot:
        # Example: paginate over describe_chime_webhook_configurations
        async for item in chatbot.iter_describe_chime_webhook_configurations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_chatbot import AsyncchatbotClient
from capo_chatbot.error import InternalServiceError


async def main():
    async with AsyncchatbotClient() as chatbot:
        try:
            await chatbot.associate_to_configuration()
        except InternalServiceError as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_chatbot import AsyncchatbotClient


async def main():
    async with AsyncchatbotClient() as chatbot:
        # Default: 3 attempts for every operation
        response = await chatbot.associate_to_configuration()

        # Override per operation
        response = await chatbot.associate_to_configuration(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await chatbot.associate_to_configuration(config_overrides={"retry_max_attempts": 1})
```
