# capo-accessanalyzer: typed, async Python SDK for AWS Accessanalyzer

`capo-accessanalyzer` is a typed Python SDK for AWS Accessanalyzer. It has an async client, `AsyncAccessAnalyzerClient`, for asyncio and trio, and a sync client, `AccessAnalyzerClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/accessanalyzer/](https://capo-sdk.dev/services/accessanalyzer/)

## Installation

```
pip install capo-accessanalyzer
```

## Usage

```python
from capo_accessanalyzer import AsyncAccessAnalyzerClient


async def main():
    async with AsyncAccessAnalyzerClient() as access_analyzer:
        # Example: call the apply_archive_rule operation
        response = await access_analyzer.apply_archive_rule()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_accessanalyzer import AsyncAccessAnalyzerClient


async def main():
    async with AsyncAccessAnalyzerClient() as access_analyzer:
        # Example: paginate over get_finding_recommendation
        async for item in access_analyzer.iter_get_finding_recommendation():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_accessanalyzer import AsyncAccessAnalyzerClient
from capo_accessanalyzer.error import AccessDeniedException


async def main():
    async with AsyncAccessAnalyzerClient() as access_analyzer:
        try:
            await access_analyzer.apply_archive_rule()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_accessanalyzer import AsyncAccessAnalyzerClient


async def main():
    async with AsyncAccessAnalyzerClient() as access_analyzer:
        # Default: 3 attempts for every operation
        response = await access_analyzer.apply_archive_rule()

        # Override per operation
        response = await access_analyzer.apply_archive_rule(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await access_analyzer.apply_archive_rule(config_overrides={"retry_max_attempts": 1})
```
