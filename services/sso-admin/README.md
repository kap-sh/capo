# capo-sso-admin: typed, async Python SDK for AWS SSO Admin

`capo-sso-admin` is a typed Python SDK for AWS SSO Admin. It has an async client, `AsyncSSOAdminClient`, for asyncio and trio, and a sync client, `SSOAdminClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/sso-admin/](https://capo-sdk.dev/services/sso-admin/)

## Installation

```
pip install capo-sso-admin
```

## Usage

```python
from capo_sso_admin import AsyncSSOAdminClient


async def main():
    async with AsyncSSOAdminClient() as sso_admin:
        # Example: call the add_region operation
        response = await sso_admin.add_region()
        print(response["status"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_sso_admin import AsyncSSOAdminClient


async def main():
    async with AsyncSSOAdminClient() as sso_admin:
        # Example: paginate over list_account_assignment_creation_status
        async for item in sso_admin.iter_list_account_assignment_creation_status():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sso_admin import AsyncSSOAdminClient
from capo_sso_admin.error import AccessDeniedException


async def main():
    async with AsyncSSOAdminClient() as sso_admin:
        try:
            await sso_admin.add_region()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sso_admin import AsyncSSOAdminClient


async def main():
    async with AsyncSSOAdminClient() as sso_admin:
        # Default: 3 attempts for every operation
        response = await sso_admin.add_region()

        # Override per operation
        response = await sso_admin.add_region(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await sso_admin.add_region(config_overrides={"retry_max_attempts": 1})
```
