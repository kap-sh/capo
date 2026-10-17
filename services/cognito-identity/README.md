# capo-cognito-identity: typed, async Python SDK for AWS Cognito Identity

`capo-cognito-identity` is a typed Python SDK for AWS Cognito Identity. It has an async client, `AsyncCognitoIdentityClient`, for asyncio and trio, and a sync client, `CognitoIdentityClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cognito-identity/](https://capo-sdk.dev/services/cognito-identity/)

## Installation

```
pip install capo-cognito-identity
```

## Usage

```python
from capo_cognito_identity import AsyncCognitoIdentityClient


async def main():
    async with AsyncCognitoIdentityClient() as cognito_identity:
        # Example: call the create_identity_pool operation
        response = await cognito_identity.create_identity_pool()
        print(response["identity_pool_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_cognito_identity import AsyncCognitoIdentityClient


async def main():
    async with AsyncCognitoIdentityClient() as cognito_identity:
        # Example: paginate over list_identity_pools
        async for item in cognito_identity.iter_list_identity_pools():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cognito_identity import AsyncCognitoIdentityClient
from capo_cognito_identity.error import InternalErrorException


async def main():
    async with AsyncCognitoIdentityClient() as cognito_identity:
        try:
            await cognito_identity.create_identity_pool()
        except InternalErrorException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cognito_identity import AsyncCognitoIdentityClient


async def main():
    async with AsyncCognitoIdentityClient() as cognito_identity:
        # Default: 3 attempts for every operation
        response = await cognito_identity.create_identity_pool()

        # Override per operation
        response = await cognito_identity.create_identity_pool(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cognito_identity.create_identity_pool(config_overrides={"retry_max_attempts": 1})
```
