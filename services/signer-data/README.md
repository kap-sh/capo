# capo-signer-data: typed, async Python SDK for AWS Signer Data

`capo-signer-data` is a typed Python SDK for AWS Signer Data. It has an async client, `AsyncSignerDataClient`, for asyncio and trio, and a sync client, `SignerDataClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/signer-data/](https://capo-sdk.dev/services/signer-data/)

## Installation

```
pip install capo-signer-data
```

## Usage

```python
from capo_signer_data import AsyncSignerDataClient


async def main():
    async with AsyncSignerDataClient() as signer_data:
        # Example: call the get_revocation_status operation
        response = await signer_data.get_revocation_status()
        print(response["revoked_entities"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_signer_data import AsyncSignerDataClient
from capo_signer_data.error import AccessDeniedException


async def main():
    async with AsyncSignerDataClient() as signer_data:
        try:
            await signer_data.get_revocation_status()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_signer_data import AsyncSignerDataClient


async def main():
    async with AsyncSignerDataClient() as signer_data:
        # Default: 3 attempts for every operation
        response = await signer_data.get_revocation_status()

        # Override per operation
        response = await signer_data.get_revocation_status(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await signer_data.get_revocation_status(config_overrides={"retry_max_attempts": 1})
```
