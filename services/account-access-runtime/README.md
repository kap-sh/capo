# capo-account-access-runtime: typed, async Python SDK for AWS Account Access Runtime

`capo-account-access-runtime` is a typed Python SDK for AWS Account Access Runtime. It has an async client, `AsyncAccountAccessRuntimeClient`, for asyncio and trio, and a sync client, `AccountAccessRuntimeClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/account-access-runtime/](https://capo-sdk.dev/services/account-access-runtime/)

## Installation

```
pip install capo-account-access-runtime
```

## Usage

```python
from capo_account_access_runtime import AsyncAccountAccessRuntimeClient


async def main():
    async with AsyncAccountAccessRuntimeClient() as account_access_runtime:
        # Example: call the get_role_credentials operation
        response = await account_access_runtime.get_role_credentials()
        print(response["credentials_details"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_account_access_runtime import AsyncAccountAccessRuntimeClient
from capo_account_access_runtime.error import AccessDeniedException


async def main():
    async with AsyncAccountAccessRuntimeClient() as account_access_runtime:
        try:
            await account_access_runtime.get_role_credentials()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

`retry_mode="adaptive"` (or `AWS_RETRY_MODE=adaptive`, or `retry_mode = adaptive` in the AWS profile) also slows the whole client down once the service starts throttling it, then speeds back up as requests succeed. The default is `standard`.

```python
from capo_account_access_runtime import AsyncAccountAccessRuntimeClient


async def main():
    async with AsyncAccountAccessRuntimeClient() as account_access_runtime:
        # Default: 3 attempts for every operation
        response = await account_access_runtime.get_role_credentials()

        # Override per operation
        response = await account_access_runtime.get_role_credentials(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await account_access_runtime.get_role_credentials(config_overrides={"retry_max_attempts": 1})
```
