# capo-elementalinference: typed, async Python SDK for AWS Elementalinference

`capo-elementalinference` is a typed Python SDK for AWS Elementalinference. It has an async client, `AsyncElementalInferenceClient`, for asyncio and trio, and a sync client, `ElementalInferenceClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/elementalinference/](https://capo-sdk.dev/services/elementalinference/)

## Installation

```
pip install capo-elementalinference
```

## Usage

```python
from capo_elementalinference import AsyncElementalInferenceClient


async def main():
    async with AsyncElementalInferenceClient() as elemental_inference:
        # Example: call the get_fixture operation
        response = await elemental_inference.get_fixture()
        print(response["fixture_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_elementalinference import AsyncElementalInferenceClient


async def main():
    async with AsyncElementalInferenceClient() as elemental_inference:
        # Example: paginate over search_fixtures
        async for item in elemental_inference.iter_search_fixtures():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_elementalinference import AsyncElementalInferenceClient
from capo_elementalinference.error import AccessDeniedException


async def main():
    async with AsyncElementalInferenceClient() as elemental_inference:
        try:
            await elemental_inference.get_fixture()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_elementalinference import AsyncElementalInferenceClient


async def main():
    async with AsyncElementalInferenceClient() as elemental_inference:
        # Default: 3 attempts for every operation
        response = await elemental_inference.get_fixture()

        # Override per operation
        response = await elemental_inference.get_fixture(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await elemental_inference.get_fixture(config_overrides={"retry_max_attempts": 1})
```
