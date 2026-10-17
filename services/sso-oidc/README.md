# capo-sso-oidc: typed, async Python SDK for AWS SSO Oidc

`capo-sso-oidc` is a typed Python SDK for AWS SSO Oidc. It has an async client, `AsyncSSOOIDCClient`, for asyncio and trio, and a sync client, `SSOOIDCClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/sso-oidc/](https://capo-sdk.dev/services/sso-oidc/)

## Installation

```
pip install capo-sso-oidc
```

## Usage

```python
from capo_sso_oidc import AsyncSSOOIDCClient


async def main():
    async with AsyncSSOOIDCClient() as ssooidc:
        # Example: call the create_token operation
        response = await ssooidc.create_token()
        print(response["access_token"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sso_oidc import AsyncSSOOIDCClient
from capo_sso_oidc.error import AccessDeniedException


async def main():
    async with AsyncSSOOIDCClient() as ssooidc:
        try:
            await ssooidc.create_token()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sso_oidc import AsyncSSOOIDCClient


async def main():
    async with AsyncSSOOIDCClient() as ssooidc:
        # Default: 3 attempts for every operation
        response = await ssooidc.create_token()

        # Override per operation
        response = await ssooidc.create_token(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await ssooidc.create_token(config_overrides={"retry_max_attempts": 1})
```
