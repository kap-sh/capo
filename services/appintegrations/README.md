# capo-appintegrations: typed, async Python SDK for AWS Appintegrations

`capo-appintegrations` is a typed Python SDK for AWS Appintegrations. It has an async client, `AsyncAppIntegrationsClient`, for asyncio and trio, and a sync client, `AppIntegrationsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/appintegrations/](https://capo-sdk.dev/services/appintegrations/)

## Installation

```
pip install capo-appintegrations
```

## Usage

```python
from capo_appintegrations import AsyncAppIntegrationsClient


async def main():
    async with AsyncAppIntegrationsClient() as app_integrations:
        # Example: call the create_application operation
        response = await app_integrations.create_application()
        print(response["arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_appintegrations import AsyncAppIntegrationsClient


async def main():
    async with AsyncAppIntegrationsClient() as app_integrations:
        # Example: paginate over list_application_associations
        async for item in app_integrations.iter_list_application_associations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_appintegrations import AsyncAppIntegrationsClient
from capo_appintegrations.error import AccessDeniedException


async def main():
    async with AsyncAppIntegrationsClient() as app_integrations:
        try:
            await app_integrations.create_application()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_appintegrations import AsyncAppIntegrationsClient


async def main():
    async with AsyncAppIntegrationsClient() as app_integrations:
        # Default: 3 attempts for every operation
        response = await app_integrations.create_application()

        # Override per operation
        response = await app_integrations.create_application(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await app_integrations.create_application(config_overrides={"retry_max_attempts": 1})
```
