# capo-license-manager-linux-subscriptions: typed, async Python SDK for AWS License Manager Linux Subscriptions

`capo-license-manager-linux-subscriptions` is a typed Python SDK for AWS License Manager Linux Subscriptions. It has an async client, `AsyncLicenseManagerLinuxSubscriptionsClient`, for asyncio and trio, and a sync client, `LicenseManagerLinuxSubscriptionsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/license-manager-linux-subscriptions/](https://capo-sdk.dev/services/license-manager-linux-subscriptions/)

## Installation

```
pip install capo-license-manager-linux-subscriptions
```

## Usage

```python
from capo_license_manager_linux_subscriptions import AsyncLicenseManagerLinuxSubscriptionsClient


async def main():
    async with AsyncLicenseManagerLinuxSubscriptionsClient() as license_manager_linux_subscriptions:
        # Example: call the deregister_subscription_provider operation
        response = await license_manager_linux_subscriptions.deregister_subscription_provider()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_license_manager_linux_subscriptions import AsyncLicenseManagerLinuxSubscriptionsClient


async def main():
    async with AsyncLicenseManagerLinuxSubscriptionsClient() as license_manager_linux_subscriptions:
        # Example: paginate over list_linux_subscription_instances
        async for item in license_manager_linux_subscriptions.iter_list_linux_subscription_instances():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_license_manager_linux_subscriptions import AsyncLicenseManagerLinuxSubscriptionsClient
from capo_license_manager_linux_subscriptions.error import InternalServerException


async def main():
    async with AsyncLicenseManagerLinuxSubscriptionsClient() as license_manager_linux_subscriptions:
        try:
            await license_manager_linux_subscriptions.deregister_subscription_provider()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_license_manager_linux_subscriptions import AsyncLicenseManagerLinuxSubscriptionsClient


async def main():
    async with AsyncLicenseManagerLinuxSubscriptionsClient() as license_manager_linux_subscriptions:
        # Default: 3 attempts for every operation
        response = await license_manager_linux_subscriptions.deregister_subscription_provider()

        # Override per operation
        response = await license_manager_linux_subscriptions.deregister_subscription_provider(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await license_manager_linux_subscriptions.deregister_subscription_provider(config_overrides={"retry_max_attempts": 1})
```
