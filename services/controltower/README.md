# Getting Started

## Installation

```
pip install capo-controltower
```

## Usage

```python
from capo_controltower import AsyncControlTowerClient


async def main():
    async with AsyncControlTowerClient() as control_tower:
        # Example: call the disable_control operation
        response = await control_tower.disable_control()
        print(response["operation_identifier"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_controltower import AsyncControlTowerClient


async def main():
    async with AsyncControlTowerClient() as control_tower:
        # Example: paginate over list_baselines
        async for item in control_tower.iter_list_baselines():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_controltower import AsyncControlTowerClient
from capo_controltower.error import AccessDeniedException


async def main():
    async with AsyncControlTowerClient() as control_tower:
        try:
            await control_tower.disable_control()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_controltower import AsyncControlTowerClient


async def main():
    async with AsyncControlTowerClient() as control_tower:
        # Default: 3 attempts for every operation
        response = await control_tower.disable_control()

        # Override per operation
        response = await control_tower.disable_control(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await control_tower.disable_control(config_overrides={"retry_max_attempts": 1})
```
