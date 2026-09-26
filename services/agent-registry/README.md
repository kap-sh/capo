# Getting Started

## Installation

```
pip install capo-agent-registry
```

## Usage

```python
from capo_agent_registry import AsyncAgentRegistryClient


async def main():
    async with AsyncAgentRegistryClient() as agent_registry:
        # Example: call the batch_get_discoverable_registry_record operation
        response = await agent_registry.batch_get_discoverable_registry_record()
        print(response["registry_records"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_agent_registry import AsyncAgentRegistryClient


async def main():
    async with AsyncAgentRegistryClient() as agent_registry:
        # Example: paginate over list_discoverable_registry_records
        async for item in agent_registry.iter_list_discoverable_registry_records():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_agent_registry import AsyncAgentRegistryClient
from capo_agent_registry.error import AccessDeniedException


async def main():
    async with AsyncAgentRegistryClient() as agent_registry:
        try:
            await agent_registry.batch_get_discoverable_registry_record()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_agent_registry import AsyncAgentRegistryClient


async def main():
    async with AsyncAgentRegistryClient() as agent_registry:
        # Default: 3 attempts for every operation
        response = await agent_registry.batch_get_discoverable_registry_record()

        # Override per operation
        response = await agent_registry.batch_get_discoverable_registry_record(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await agent_registry.batch_get_discoverable_registry_record(config_overrides={"retry_max_attempts": 1})
```
