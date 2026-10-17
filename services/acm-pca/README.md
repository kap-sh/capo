# capo-acm-pca: typed, async Python SDK for AWS ACM Pca

`capo-acm-pca` is a typed Python SDK for AWS ACM Pca. It has an async client, `AsyncACMPCAClient`, for asyncio and trio, and a sync client, `ACMPCAClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/acm-pca/](https://capo-sdk.dev/services/acm-pca/)

## Installation

```
pip install capo-acm-pca
```

## Usage

```python
from capo_acm_pca import AsyncACMPCAClient


async def main():
    async with AsyncACMPCAClient() as acmpca:
        # Example: call the create_certificate_authority operation
        response = await acmpca.create_certificate_authority()
        print(response["certificate_authority_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_acm_pca import AsyncACMPCAClient


async def main():
    async with AsyncACMPCAClient() as acmpca:
        # Example: paginate over list_certificate_authorities
        async for item in acmpca.iter_list_certificate_authorities():
            print(item)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_until_` prefixed method.

```python
from capo_acm_pca import AsyncACMPCAClient


async def main():
    async with AsyncACMPCAClient() as acmpca:
        # Example: wait for certificate_issued
        await acmpca.wait_until_certificate_issued(max_wait_time=300)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_acm_pca import AsyncACMPCAClient
from capo_acm_pca.error import InvalidArgsException


async def main():
    async with AsyncACMPCAClient() as acmpca:
        try:
            await acmpca.create_certificate_authority()
        except InvalidArgsException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_acm_pca import AsyncACMPCAClient


async def main():
    async with AsyncACMPCAClient() as acmpca:
        # Default: 3 attempts for every operation
        response = await acmpca.create_certificate_authority()

        # Override per operation
        response = await acmpca.create_certificate_authority(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await acmpca.create_certificate_authority(config_overrides={"retry_max_attempts": 1})
```
