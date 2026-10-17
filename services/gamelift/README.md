# capo-gamelift: typed, async Python SDK for AWS Gamelift

`capo-gamelift` is a typed Python SDK for AWS Gamelift. It has an async client, `AsyncGameLiftClient`, for asyncio and trio, and a sync client, `GameLiftClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/gamelift/](https://capo-sdk.dev/services/gamelift/)

## Installation

```
pip install capo-gamelift
```

## Usage

```python
from capo_gamelift import AsyncGameLiftClient


async def main():
    async with AsyncGameLiftClient() as game_lift:
        # Example: call the accept_match operation
        response = await game_lift.accept_match()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_gamelift import AsyncGameLiftClient


async def main():
    async with AsyncGameLiftClient() as game_lift:
        # Example: paginate over describe_fleet_attributes
        async for item in game_lift.iter_describe_fleet_attributes():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_gamelift import AsyncGameLiftClient
from capo_gamelift.error import InternalServiceException


async def main():
    async with AsyncGameLiftClient() as game_lift:
        try:
            await game_lift.accept_match()
        except InternalServiceException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_gamelift import AsyncGameLiftClient


async def main():
    async with AsyncGameLiftClient() as game_lift:
        # Default: 3 attempts for every operation
        response = await game_lift.accept_match()

        # Override per operation
        response = await game_lift.accept_match(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await game_lift.accept_match(config_overrides={"retry_max_attempts": 1})
```
