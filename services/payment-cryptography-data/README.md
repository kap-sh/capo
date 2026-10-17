# capo-payment-cryptography-data: typed, async Python SDK for AWS Payment Cryptography Data

`capo-payment-cryptography-data` is a typed Python SDK for AWS Payment Cryptography Data. It has an async client, `AsyncPaymentCryptographyDataClient`, for asyncio and trio, and a sync client, `PaymentCryptographyDataClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/payment-cryptography-data/](https://capo-sdk.dev/services/payment-cryptography-data/)

## Installation

```
pip install capo-payment-cryptography-data
```

## Usage

```python
from capo_payment_cryptography_data import AsyncPaymentCryptographyDataClient


async def main():
    async with AsyncPaymentCryptographyDataClient() as payment_cryptography_data:
        # Example: call the decrypt_data operation
        response = await payment_cryptography_data.decrypt_data()
        print(response["key_arn"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_payment_cryptography_data import AsyncPaymentCryptographyDataClient
from capo_payment_cryptography_data.error import AccessDeniedException


async def main():
    async with AsyncPaymentCryptographyDataClient() as payment_cryptography_data:
        try:
            await payment_cryptography_data.decrypt_data()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_payment_cryptography_data import AsyncPaymentCryptographyDataClient


async def main():
    async with AsyncPaymentCryptographyDataClient() as payment_cryptography_data:
        # Default: 3 attempts for every operation
        response = await payment_cryptography_data.decrypt_data()

        # Override per operation
        response = await payment_cryptography_data.decrypt_data(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await payment_cryptography_data.decrypt_data(config_overrides={"retry_max_attempts": 1})
```
