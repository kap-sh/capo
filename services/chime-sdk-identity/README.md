# capo-chime-sdk-identity: typed, async Python SDK for AWS Chime SDK Identity

`capo-chime-sdk-identity` is a typed Python SDK for AWS Chime SDK Identity. It has an async client, `AsyncChimeSDKIdentityClient`, for asyncio and trio, and a sync client, `ChimeSDKIdentityClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/chime-sdk-identity/](https://capo-sdk.dev/services/chime-sdk-identity/)

## Installation

```
pip install capo-chime-sdk-identity
```

## Usage

```python
from capo_chime_sdk_identity import AsyncChimeSDKIdentityClient


async def main():
    async with AsyncChimeSDKIdentityClient() as chime_sdk_identity:
        # Example: call the create_app_instance operation
        response = await chime_sdk_identity.create_app_instance()
        print(response["app_instance_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_chime_sdk_identity import AsyncChimeSDKIdentityClient


async def main():
    async with AsyncChimeSDKIdentityClient() as chime_sdk_identity:
        # Example: paginate over list_app_instance_admins
        async for item in chime_sdk_identity.iter_list_app_instance_admins():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_chime_sdk_identity import AsyncChimeSDKIdentityClient
from capo_chime_sdk_identity.error import BadRequestException


async def main():
    async with AsyncChimeSDKIdentityClient() as chime_sdk_identity:
        try:
            await chime_sdk_identity.create_app_instance()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_chime_sdk_identity import AsyncChimeSDKIdentityClient


async def main():
    async with AsyncChimeSDKIdentityClient() as chime_sdk_identity:
        # Default: 3 attempts for every operation
        response = await chime_sdk_identity.create_app_instance()

        # Override per operation
        response = await chime_sdk_identity.create_app_instance(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await chime_sdk_identity.create_app_instance(config_overrides={"retry_max_attempts": 1})
```
