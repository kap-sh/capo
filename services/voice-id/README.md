# capo-voice-id: typed, async Python SDK for AWS Voice Id

`capo-voice-id` is a typed Python SDK for AWS Voice Id. It has an async client, `AsyncVoiceIDClient`, for asyncio and trio, and a sync client, `VoiceIDClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/voice-id/](https://capo-sdk.dev/services/voice-id/)

## Installation

```
pip install capo-voice-id
```

## Usage

```python
from capo_voice_id import AsyncVoiceIDClient


async def main():
    async with AsyncVoiceIDClient() as voice_id:
        # Example: call the associate_fraudster operation
        response = await voice_id.associate_fraudster()
        print(response["fraudster"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_voice_id import AsyncVoiceIDClient


async def main():
    async with AsyncVoiceIDClient() as voice_id:
        # Example: paginate over list_fraudster_registration_jobs
        async for item in voice_id.iter_list_fraudster_registration_jobs():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_voice_id import AsyncVoiceIDClient
from capo_voice_id.error import AccessDeniedException


async def main():
    async with AsyncVoiceIDClient() as voice_id:
        try:
            await voice_id.associate_fraudster()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_voice_id import AsyncVoiceIDClient


async def main():
    async with AsyncVoiceIDClient() as voice_id:
        # Default: 3 attempts for every operation
        response = await voice_id.associate_fraudster()

        # Override per operation
        response = await voice_id.associate_fraudster(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await voice_id.associate_fraudster(config_overrides={"retry_max_attempts": 1})
```
