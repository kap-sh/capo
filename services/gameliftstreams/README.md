# Getting Started

## Installation

```
pip install capo-gameliftstreams
```

## Usage

```python
from capo_gameliftstreams import AsyncGameLiftStreamsClient


async def main():
    async with AsyncGameLiftStreamsClient() as game_lift_streams:
        # Example: call the add_stream_group_locations operation
        response = await game_lift_streams.add_stream_group_locations()
        print(response["identifier"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_gameliftstreams import AsyncGameLiftStreamsClient


async def main():
    async with AsyncGameLiftStreamsClient() as game_lift_streams:
        # Example: paginate over list_stream_sessions
        async for item in game_lift_streams.iter_list_stream_sessions():
            print(item)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_until_` prefixed method.

```python
from capo_gameliftstreams import AsyncGameLiftStreamsClient


async def main():
    async with AsyncGameLiftStreamsClient() as game_lift_streams:
        # Example: wait for application_deleted
        await game_lift_streams.wait_until_application_deleted(max_wait_time=300)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_gameliftstreams import AsyncGameLiftStreamsClient
from capo_gameliftstreams.error import AccessDeniedException


async def main():
    async with AsyncGameLiftStreamsClient() as game_lift_streams:
        try:
            await game_lift_streams.add_stream_group_locations()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_gameliftstreams import AsyncGameLiftStreamsClient


async def main():
    async with AsyncGameLiftStreamsClient() as game_lift_streams:
        # Default: 3 attempts for every operation
        response = await game_lift_streams.add_stream_group_locations()

        # Override per operation
        response = await game_lift_streams.add_stream_group_locations(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await game_lift_streams.add_stream_group_locations(config_overrides={"retry_max_attempts": 1})
```
