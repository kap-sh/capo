# Getting Started

## Installation

```
pip install capo-internetmonitor
```

## Usage

```python
from capo_internetmonitor import AsyncInternetMonitorClient


async def main():
    async with AsyncInternetMonitorClient() as internet_monitor:
        # Example: call the list_tags_for_resource operation
        response = await internet_monitor.list_tags_for_resource()
        print(response["tags"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_internetmonitor import AsyncInternetMonitorClient


async def main():
    async with AsyncInternetMonitorClient() as internet_monitor:
        # Example: paginate over list_internet_events
        async for item in internet_monitor.iter_list_internet_events():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_internetmonitor import AsyncInternetMonitorClient
from capo_internetmonitor.error import AccessDeniedException


async def main():
    async with AsyncInternetMonitorClient() as internet_monitor:
        try:
            await internet_monitor.list_tags_for_resource()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_internetmonitor import AsyncInternetMonitorClient


async def main():
    async with AsyncInternetMonitorClient() as internet_monitor:
        # Default: 3 attempts for every operation
        response = await internet_monitor.list_tags_for_resource()

        # Override per operation
        response = await internet_monitor.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await internet_monitor.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
