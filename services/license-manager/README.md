# capo-license-manager: typed, async Python SDK for AWS License Manager

`capo-license-manager` is a typed Python SDK for AWS License Manager. It has an async client, `AsyncLicenseManagerClient`, for asyncio and trio, and a sync client, `LicenseManagerClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/license-manager/](https://capo-sdk.dev/services/license-manager/)

## Installation

```
pip install capo-license-manager
```

## Usage

```python
from capo_license_manager import AsyncLicenseManagerClient


async def main():
    async with AsyncLicenseManagerClient() as license_manager:
        # Example: call the accept_grant operation
        response = await license_manager.accept_grant()
        print(response["grant_arn"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_license_manager import AsyncLicenseManagerClient
from capo_license_manager.error import AccessDeniedException


async def main():
    async with AsyncLicenseManagerClient() as license_manager:
        try:
            await license_manager.accept_grant()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_license_manager import AsyncLicenseManagerClient


async def main():
    async with AsyncLicenseManagerClient() as license_manager:
        # Default: 3 attempts for every operation
        response = await license_manager.accept_grant()

        # Override per operation
        response = await license_manager.accept_grant(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await license_manager.accept_grant(config_overrides={"retry_max_attempts": 1})
```
