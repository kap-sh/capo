# Getting Started

## Installation

```
pip install capo-iot-managed-integrations
```

## Usage

```python
from capo_iot_managed_integrations import AsyncIoTManagedIntegrationsClient


async def main():
    async with AsyncIoTManagedIntegrationsClient() as io_t_managed_integrations:
        # Example: call the get_custom_endpoint operation
        response = await io_t_managed_integrations.get_custom_endpoint()
        print(response["endpoint_address"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_iot_managed_integrations import AsyncIoTManagedIntegrationsClient


async def main():
    async with AsyncIoTManagedIntegrationsClient() as io_t_managed_integrations:
        # Example: paginate over list_account_associations
        async for item in io_t_managed_integrations.iter_list_account_associations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_iot_managed_integrations import AsyncIoTManagedIntegrationsClient
from capo_iot_managed_integrations.error import AccessDeniedException


async def main():
    async with AsyncIoTManagedIntegrationsClient() as io_t_managed_integrations:
        try:
            await io_t_managed_integrations.get_custom_endpoint()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_iot_managed_integrations import AsyncIoTManagedIntegrationsClient


async def main():
    async with AsyncIoTManagedIntegrationsClient() as io_t_managed_integrations:
        # Default: 3 attempts for every operation
        response = await io_t_managed_integrations.get_custom_endpoint()

        # Override per operation
        response = await io_t_managed_integrations.get_custom_endpoint(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await io_t_managed_integrations.get_custom_endpoint(config_overrides={"retry_max_attempts": 1})
```
