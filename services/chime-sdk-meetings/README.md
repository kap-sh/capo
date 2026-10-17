# capo-chime-sdk-meetings: typed, async Python SDK for AWS Chime SDK Meetings

`capo-chime-sdk-meetings` is a typed Python SDK for AWS Chime SDK Meetings. It has an async client, `AsyncChimeSDKMeetingsClient`, for asyncio and trio, and a sync client, `ChimeSDKMeetingsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/chime-sdk-meetings/](https://capo-sdk.dev/services/chime-sdk-meetings/)

## Installation

```
pip install capo-chime-sdk-meetings
```

## Usage

```python
from capo_chime_sdk_meetings import AsyncChimeSDKMeetingsClient


async def main():
    async with AsyncChimeSDKMeetingsClient() as chime_sdk_meetings:
        # Example: call the batch_create_attendee operation
        response = await chime_sdk_meetings.batch_create_attendee()
        print(response["attendees"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_chime_sdk_meetings import AsyncChimeSDKMeetingsClient


async def main():
    async with AsyncChimeSDKMeetingsClient() as chime_sdk_meetings:
        # Example: paginate over list_attendees
        async for item in chime_sdk_meetings.iter_list_attendees():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_chime_sdk_meetings import AsyncChimeSDKMeetingsClient
from capo_chime_sdk_meetings.error import BadRequestException


async def main():
    async with AsyncChimeSDKMeetingsClient() as chime_sdk_meetings:
        try:
            await chime_sdk_meetings.batch_create_attendee()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_chime_sdk_meetings import AsyncChimeSDKMeetingsClient


async def main():
    async with AsyncChimeSDKMeetingsClient() as chime_sdk_meetings:
        # Default: 3 attempts for every operation
        response = await chime_sdk_meetings.batch_create_attendee()

        # Override per operation
        response = await chime_sdk_meetings.batch_create_attendee(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await chime_sdk_meetings.batch_create_attendee(config_overrides={"retry_max_attempts": 1})
```
