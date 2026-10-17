# capo-chime-sdk-voice: typed, async Python SDK for AWS Chime SDK Voice

`capo-chime-sdk-voice` is a typed Python SDK for AWS Chime SDK Voice. It has an async client, `AsyncChimeSDKVoiceClient`, for asyncio and trio, and a sync client, `ChimeSDKVoiceClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/chime-sdk-voice/](https://capo-sdk.dev/services/chime-sdk-voice/)

## Installation

```
pip install capo-chime-sdk-voice
```

## Usage

```python
from capo_chime_sdk_voice import AsyncChimeSDKVoiceClient


async def main():
    async with AsyncChimeSDKVoiceClient() as chime_sdk_voice:
        # Example: call the associate_phone_numbers_with_voice_connector operation
        response = await chime_sdk_voice.associate_phone_numbers_with_voice_connector()
        print(response["phone_number_errors"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_chime_sdk_voice import AsyncChimeSDKVoiceClient


async def main():
    async with AsyncChimeSDKVoiceClient() as chime_sdk_voice:
        # Example: paginate over list_phone_number_orders
        async for item in chime_sdk_voice.iter_list_phone_number_orders():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_chime_sdk_voice import AsyncChimeSDKVoiceClient
from capo_chime_sdk_voice.error import AccessDeniedException


async def main():
    async with AsyncChimeSDKVoiceClient() as chime_sdk_voice:
        try:
            await chime_sdk_voice.associate_phone_numbers_with_voice_connector()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_chime_sdk_voice import AsyncChimeSDKVoiceClient


async def main():
    async with AsyncChimeSDKVoiceClient() as chime_sdk_voice:
        # Default: 3 attempts for every operation
        response = await chime_sdk_voice.associate_phone_numbers_with_voice_connector()

        # Override per operation
        response = await chime_sdk_voice.associate_phone_numbers_with_voice_connector(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await chime_sdk_voice.associate_phone_numbers_with_voice_connector(config_overrides={"retry_max_attempts": 1})
```
