# Getting Started

## Installation

```
pip install capo-network-security-manager
```

## Usage

```python
from capo_network_security_manager import AsyncNetworkSecurityManagerClient


async def main():
    async with AsyncNetworkSecurityManagerClient() as network_security_manager:
        # Example: call the delete_admin_account operation
        response = await network_security_manager.delete_admin_account()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_network_security_manager import AsyncNetworkSecurityManagerClient


async def main():
    async with AsyncNetworkSecurityManagerClient() as network_security_manager:
        # Example: paginate over list_admin_accounts
        async for item in network_security_manager.iter_list_admin_accounts():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_network_security_manager import AsyncNetworkSecurityManagerClient
from capo_network_security_manager.error import AccessDeniedException


async def main():
    async with AsyncNetworkSecurityManagerClient() as network_security_manager:
        try:
            await network_security_manager.delete_admin_account()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_network_security_manager import AsyncNetworkSecurityManagerClient


async def main():
    async with AsyncNetworkSecurityManagerClient() as network_security_manager:
        # Default: 3 attempts for every operation
        response = await network_security_manager.delete_admin_account()

        # Override per operation
        response = await network_security_manager.delete_admin_account(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await network_security_manager.delete_admin_account(config_overrides={"retry_max_attempts": 1})
```
