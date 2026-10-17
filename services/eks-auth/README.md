# capo-eks-auth: typed, async Python SDK for AWS EKS Auth

`capo-eks-auth` is a typed Python SDK for AWS EKS Auth. It has an async client, `AsyncEKSAuthClient`, for asyncio and trio, and a sync client, `EKSAuthClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/eks-auth/](https://capo-sdk.dev/services/eks-auth/)

## Installation

```
pip install capo-eks-auth
```

## Usage

```python
from capo_eks_auth import AsyncEKSAuthClient


async def main():
    async with AsyncEKSAuthClient() as eks_auth:
        # Example: call the assume_role_for_pod_identity operation
        response = await eks_auth.assume_role_for_pod_identity()
        print(response["subject"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_eks_auth import AsyncEKSAuthClient
from capo_eks_auth.error import AccessDeniedException


async def main():
    async with AsyncEKSAuthClient() as eks_auth:
        try:
            await eks_auth.assume_role_for_pod_identity()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_eks_auth import AsyncEKSAuthClient


async def main():
    async with AsyncEKSAuthClient() as eks_auth:
        # Default: 3 attempts for every operation
        response = await eks_auth.assume_role_for_pod_identity()

        # Override per operation
        response = await eks_auth.assume_role_for_pod_identity(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await eks_auth.assume_role_for_pod_identity(config_overrides={"retry_max_attempts": 1})
```
