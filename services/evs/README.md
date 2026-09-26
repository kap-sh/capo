# Getting Started

## Installation

```
pip install capo-evs
```

## Usage

```python
from capo_evs import AsyncevsClient


async def main():
    async with AsyncevsClient() as evs:
        # Example: call the get_versions operation
        response = await evs.get_versions()
        print(response["vcf_versions"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_evs import AsyncevsClient


async def main():
    async with AsyncevsClient() as evs:
        # Example: paginate over list_environments
        async for item in evs.iter_list_environments():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_evs import AsyncevsClient
from capo_evs.error import InternalServerException


async def main():
    async with AsyncevsClient() as evs:
        try:
            await evs.get_versions()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_evs import AsyncevsClient


async def main():
    async with AsyncevsClient() as evs:
        # Default: 3 attempts for every operation
        response = await evs.get_versions()

        # Override per operation
        response = await evs.get_versions(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await evs.get_versions(config_overrides={"retry_max_attempts": 1})
```
