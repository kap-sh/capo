# capo-cognito-identity-provider: typed, async Python SDK for AWS Cognito Identity Provider

`capo-cognito-identity-provider` is a typed Python SDK for AWS Cognito Identity Provider. It has an async client, `AsyncCognitoIdentityProviderClient`, for asyncio and trio, and a sync client, `CognitoIdentityProviderClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cognito-identity-provider/](https://capo-sdk.dev/services/cognito-identity-provider/)

## Installation

```
pip install capo-cognito-identity-provider
```

## Usage

```python
from capo_cognito_identity_provider import AsyncCognitoIdentityProviderClient


async def main():
    async with AsyncCognitoIdentityProviderClient() as cognito_identity_provider:
        # Example: call the add_custom_attributes operation
        response = await cognito_identity_provider.add_custom_attributes()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_cognito_identity_provider import AsyncCognitoIdentityProviderClient


async def main():
    async with AsyncCognitoIdentityProviderClient() as cognito_identity_provider:
        # Example: paginate over admin_list_groups_for_user
        async for item in cognito_identity_provider.iter_admin_list_groups_for_user():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cognito_identity_provider import AsyncCognitoIdentityProviderClient
from capo_cognito_identity_provider.error import InternalErrorException


async def main():
    async with AsyncCognitoIdentityProviderClient() as cognito_identity_provider:
        try:
            await cognito_identity_provider.add_custom_attributes()
        except InternalErrorException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cognito_identity_provider import AsyncCognitoIdentityProviderClient


async def main():
    async with AsyncCognitoIdentityProviderClient() as cognito_identity_provider:
        # Default: 3 attempts for every operation
        response = await cognito_identity_provider.add_custom_attributes()

        # Override per operation
        response = await cognito_identity_provider.add_custom_attributes(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cognito_identity_provider.add_custom_attributes(config_overrides={"retry_max_attempts": 1})
```
