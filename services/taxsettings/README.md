# capo-taxsettings: typed, async Python SDK for AWS Taxsettings

`capo-taxsettings` is a typed Python SDK for AWS Taxsettings. It has an async client, `AsyncTaxSettingsClient`, for asyncio and trio, and a sync client, `TaxSettingsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/taxsettings/](https://capo-sdk.dev/services/taxsettings/)

## Installation

```
pip install capo-taxsettings
```

## Usage

```python
from capo_taxsettings import AsyncTaxSettingsClient


async def main():
    async with AsyncTaxSettingsClient() as tax_settings:
        # Example: call the batch_delete_tax_registration operation
        response = await tax_settings.batch_delete_tax_registration()
        print(response["errors"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_taxsettings import AsyncTaxSettingsClient


async def main():
    async with AsyncTaxSettingsClient() as tax_settings:
        # Example: paginate over list_supplemental_tax_registrations
        async for item in tax_settings.iter_list_supplemental_tax_registrations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_taxsettings import AsyncTaxSettingsClient
from capo_taxsettings.error import ConflictException


async def main():
    async with AsyncTaxSettingsClient() as tax_settings:
        try:
            await tax_settings.batch_delete_tax_registration()
        except ConflictException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_taxsettings import AsyncTaxSettingsClient


async def main():
    async with AsyncTaxSettingsClient() as tax_settings:
        # Default: 3 attempts for every operation
        response = await tax_settings.batch_delete_tax_registration()

        # Override per operation
        response = await tax_settings.batch_delete_tax_registration(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await tax_settings.batch_delete_tax_registration(config_overrides={"retry_max_attempts": 1})
```
