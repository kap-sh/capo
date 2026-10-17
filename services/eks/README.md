# capo-eks: typed, async Python SDK for Amazon EKS

`capo-eks` is a typed Python SDK for Amazon EKS. It has an async client, `AsyncEKSClient`, for asyncio and trio, and a sync client, `EKSClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/eks/](https://capo-sdk.dev/services/eks/)

## Installation

```
pip install capo-eks
```

## Usage

```python
from capo_eks import AsyncEKSClient


async def main():
    async with AsyncEKSClient() as eks:
        # Example: call the activate_certificate_authority operation
        response = await eks.activate_certificate_authority()
        print(response["update"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_eks import AsyncEKSClient


async def main():
    async with AsyncEKSClient() as eks:
        # Example: paginate over describe_addon_versions
        async for item in eks.iter_describe_addon_versions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_eks import AsyncEKSClient
from capo_eks.error import InvalidParameterException


async def main():
    async with AsyncEKSClient() as eks:
        try:
            await eks.activate_certificate_authority()
        except InvalidParameterException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_eks import AsyncEKSClient


async def main():
    async with AsyncEKSClient() as eks:
        # Default: 3 attempts for every operation
        response = await eks.activate_certificate_authority()

        # Override per operation
        response = await eks.activate_certificate_authority(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await eks.activate_certificate_authority(config_overrides={"retry_max_attempts": 1})
```
