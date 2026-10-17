# capo-pinpoint-sms-voice: typed, async Python SDK for AWS Pinpoint Sms Voice

`capo-pinpoint-sms-voice` is a typed Python SDK for AWS Pinpoint Sms Voice. It has an async client, `AsyncPinpointSMSVoiceClient`, for asyncio and trio, and a sync client, `PinpointSMSVoiceClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/pinpoint-sms-voice/](https://capo-sdk.dev/services/pinpoint-sms-voice/)

## Installation

```
pip install capo-pinpoint-sms-voice
```

## Usage

```python
from capo_pinpoint_sms_voice import AsyncPinpointSMSVoiceClient


async def main():
    async with AsyncPinpointSMSVoiceClient() as pinpoint_sms_voice:
        # Example: call the create_configuration_set operation
        response = await pinpoint_sms_voice.create_configuration_set()
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_pinpoint_sms_voice import AsyncPinpointSMSVoiceClient
from capo_pinpoint_sms_voice.error import AlreadyExistsException


async def main():
    async with AsyncPinpointSMSVoiceClient() as pinpoint_sms_voice:
        try:
            await pinpoint_sms_voice.create_configuration_set()
        except AlreadyExistsException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_pinpoint_sms_voice import AsyncPinpointSMSVoiceClient


async def main():
    async with AsyncPinpointSMSVoiceClient() as pinpoint_sms_voice:
        # Default: 3 attempts for every operation
        response = await pinpoint_sms_voice.create_configuration_set()

        # Override per operation
        response = await pinpoint_sms_voice.create_configuration_set(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await pinpoint_sms_voice.create_configuration_set(config_overrides={"retry_max_attempts": 1})
```
