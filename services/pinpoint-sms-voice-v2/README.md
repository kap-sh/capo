# capo-pinpoint-sms-voice-v2: typed, async Python SDK for AWS Pinpoint Sms Voice V2

`capo-pinpoint-sms-voice-v2` is a typed Python SDK for AWS Pinpoint Sms Voice V2. It has an async client, `AsyncPinpointSMSVoiceV2Client`, for asyncio and trio, and a sync client, `PinpointSMSVoiceV2Client`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/pinpoint-sms-voice-v2/](https://capo-sdk.dev/services/pinpoint-sms-voice-v2/)

## Installation

```
pip install capo-pinpoint-sms-voice-v2
```

## Usage

```python
from capo_pinpoint_sms_voice_v2 import AsyncPinpointSMSVoiceV2Client


async def main():
    async with AsyncPinpointSMSVoiceV2Client() as pinpoint_sms_voice_v2:
        # Example: call the associate_origination_identity operation
        response = await pinpoint_sms_voice_v2.associate_origination_identity()
        print(response["pool_arn"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_pinpoint_sms_voice_v2 import AsyncPinpointSMSVoiceV2Client
from capo_pinpoint_sms_voice_v2.error import AccessDeniedException


async def main():
    async with AsyncPinpointSMSVoiceV2Client() as pinpoint_sms_voice_v2:
        try:
            await pinpoint_sms_voice_v2.associate_origination_identity()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_pinpoint_sms_voice_v2 import AsyncPinpointSMSVoiceV2Client


async def main():
    async with AsyncPinpointSMSVoiceV2Client() as pinpoint_sms_voice_v2:
        # Default: 3 attempts for every operation
        response = await pinpoint_sms_voice_v2.associate_origination_identity()

        # Override per operation
        response = await pinpoint_sms_voice_v2.associate_origination_identity(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await pinpoint_sms_voice_v2.associate_origination_identity(config_overrides={"retry_max_attempts": 1})
```
