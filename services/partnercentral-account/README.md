# capo-partnercentral-account: typed, async Python SDK for AWS Partnercentral Account

`capo-partnercentral-account` is a typed Python SDK for AWS Partnercentral Account. It has an async client, `AsyncPartnerCentralAccountClient`, for asyncio and trio, and a sync client, `PartnerCentralAccountClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/partnercentral-account/](https://capo-sdk.dev/services/partnercentral-account/)

## Installation

```
pip install capo-partnercentral-account
```

## Usage

```python
from capo_partnercentral_account import AsyncPartnerCentralAccountClient


async def main():
    async with AsyncPartnerCentralAccountClient() as partner_central_account:
        # Example: call the get_verification operation
        response = await partner_central_account.get_verification()
        print(response["verification_type"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_partnercentral_account import AsyncPartnerCentralAccountClient


async def main():
    async with AsyncPartnerCentralAccountClient() as partner_central_account:
        # Example: paginate over list_connection_invitations
        async for item in partner_central_account.iter_list_connection_invitations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_partnercentral_account import AsyncPartnerCentralAccountClient
from capo_partnercentral_account.error import AccessDeniedException


async def main():
    async with AsyncPartnerCentralAccountClient() as partner_central_account:
        try:
            await partner_central_account.get_verification()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_partnercentral_account import AsyncPartnerCentralAccountClient


async def main():
    async with AsyncPartnerCentralAccountClient() as partner_central_account:
        # Default: 3 attempts for every operation
        response = await partner_central_account.get_verification()

        # Override per operation
        response = await partner_central_account.get_verification(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await partner_central_account.get_verification(config_overrides={"retry_max_attempts": 1})
```
