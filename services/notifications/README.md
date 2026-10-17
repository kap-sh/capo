# capo-notifications: typed, async Python SDK for AWS Notifications

`capo-notifications` is a typed Python SDK for AWS Notifications. It has an async client, `AsyncNotificationsClient`, for asyncio and trio, and a sync client, `NotificationsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/notifications/](https://capo-sdk.dev/services/notifications/)

## Installation

```
pip install capo-notifications
```

## Usage

```python
from capo_notifications import AsyncNotificationsClient


async def main():
    async with AsyncNotificationsClient() as notifications:
        # Example: call the list_managed_notification_channel_associations operation
        response = await notifications.list_managed_notification_channel_associations()
        print(response["next_token"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_notifications import AsyncNotificationsClient


async def main():
    async with AsyncNotificationsClient() as notifications:
        # Example: paginate over list_managed_notification_channel_associations
        async for item in notifications.iter_list_managed_notification_channel_associations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_notifications import AsyncNotificationsClient
from capo_notifications.error import AccessDeniedException


async def main():
    async with AsyncNotificationsClient() as notifications:
        try:
            await notifications.list_managed_notification_channel_associations()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_notifications import AsyncNotificationsClient


async def main():
    async with AsyncNotificationsClient() as notifications:
        # Default: 3 attempts for every operation
        response = await notifications.list_managed_notification_channel_associations()

        # Override per operation
        response = await notifications.list_managed_notification_channel_associations(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await notifications.list_managed_notification_channel_associations(config_overrides={"retry_max_attempts": 1})
```
