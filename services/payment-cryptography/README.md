# capo-payment-cryptography: typed, async Python SDK for AWS Payment Cryptography

`capo-payment-cryptography` is a typed Python SDK for AWS Payment Cryptography. It has an async client, `AsyncPaymentCryptographyClient`, for asyncio and trio, and a sync client, `PaymentCryptographyClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/payment-cryptography/](https://capo-sdk.dev/services/payment-cryptography/)

## Installation

```
pip install capo-payment-cryptography
```

## Usage

```python
from capo_payment_cryptography import AsyncPaymentCryptographyClient


async def main():
    async with AsyncPaymentCryptographyClient() as payment_cryptography:
        # Example: call the associate_mpa_team operation
        response = await payment_cryptography.associate_mpa_team()
        print(response["mpa_team_association"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_payment_cryptography import AsyncPaymentCryptographyClient


async def main():
    async with AsyncPaymentCryptographyClient() as payment_cryptography:
        # Example: paginate over list_tags_for_resource
        async for item in payment_cryptography.iter_list_tags_for_resource():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_payment_cryptography import AsyncPaymentCryptographyClient
from capo_payment_cryptography.error import AccessDeniedException


async def main():
    async with AsyncPaymentCryptographyClient() as payment_cryptography:
        try:
            await payment_cryptography.associate_mpa_team()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_payment_cryptography import AsyncPaymentCryptographyClient


async def main():
    async with AsyncPaymentCryptographyClient() as payment_cryptography:
        # Default: 3 attempts for every operation
        response = await payment_cryptography.associate_mpa_team()

        # Override per operation
        response = await payment_cryptography.associate_mpa_team(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await payment_cryptography.associate_mpa_team(config_overrides={"retry_max_attempts": 1})
```
