# capo-kendra-ranking: typed, async Python SDK for AWS Kendra Ranking

`capo-kendra-ranking` is a typed Python SDK for AWS Kendra Ranking. It has an async client, `AsyncKendraRankingClient`, for asyncio and trio, and a sync client, `KendraRankingClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/kendra-ranking/](https://capo-sdk.dev/services/kendra-ranking/)

## Installation

```
pip install capo-kendra-ranking
```

## Usage

```python
from capo_kendra_ranking import AsyncKendraRankingClient


async def main():
    async with AsyncKendraRankingClient() as kendra_ranking:
        # Example: call the create_rescore_execution_plan operation
        response = await kendra_ranking.create_rescore_execution_plan()
        print(response["id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_kendra_ranking import AsyncKendraRankingClient


async def main():
    async with AsyncKendraRankingClient() as kendra_ranking:
        # Example: paginate over list_rescore_execution_plans
        async for item in kendra_ranking.iter_list_rescore_execution_plans():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_kendra_ranking import AsyncKendraRankingClient
from capo_kendra_ranking.error import AccessDeniedException


async def main():
    async with AsyncKendraRankingClient() as kendra_ranking:
        try:
            await kendra_ranking.create_rescore_execution_plan()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_kendra_ranking import AsyncKendraRankingClient


async def main():
    async with AsyncKendraRankingClient() as kendra_ranking:
        # Default: 3 attempts for every operation
        response = await kendra_ranking.create_rescore_execution_plan()

        # Override per operation
        response = await kendra_ranking.create_rescore_execution_plan(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await kendra_ranking.create_rescore_execution_plan(config_overrides={"retry_max_attempts": 1})
```
