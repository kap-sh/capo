# capo-signer: typed, async Python SDK for AWS Signer

`capo-signer` is a typed Python SDK for AWS Signer. It has an async client, `AsyncsignerClient`, for asyncio and trio, and a sync client, `signerClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/signer/](https://capo-sdk.dev/services/signer/)

## Installation

```
pip install capo-signer
```

## Usage

```python
from capo_signer import AsyncsignerClient


async def main():
    async with AsyncsignerClient() as signer:
        # Example: call the add_profile_permission operation
        response = await signer.add_profile_permission()
        print(response["revision_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_signer import AsyncsignerClient


async def main():
    async with AsyncsignerClient() as signer:
        # Example: paginate over list_signing_jobs
        async for item in signer.iter_list_signing_jobs():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_signer import AsyncsignerClient
from capo_signer.error import AccessDeniedException


async def main():
    async with AsyncsignerClient() as signer:
        try:
            await signer.add_profile_permission()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_signer import AsyncsignerClient


async def main():
    async with AsyncsignerClient() as signer:
        # Default: 3 attempts for every operation
        response = await signer.add_profile_permission()

        # Override per operation
        response = await signer.add_profile_permission(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await signer.add_profile_permission(config_overrides={"retry_max_attempts": 1})
```
