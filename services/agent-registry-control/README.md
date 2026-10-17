# capo-agent-registry-control: typed, async Python SDK for AWS Agent Registry Control

`capo-agent-registry-control` is a typed Python SDK for AWS Agent Registry Control. It has an async client, `AsyncAgentRegistryControlClient`, for asyncio and trio, and a sync client, `AgentRegistryControlClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/agent-registry-control/](https://capo-sdk.dev/services/agent-registry-control/)

## Installation

```
pip install capo-agent-registry-control
```

## Usage

```python
from capo_agent_registry_control import AsyncAgentRegistryControlClient


async def main():
    async with AsyncAgentRegistryControlClient() as agent_registry_control:
        # Example: call the list_tags_for_resource operation
        response = await agent_registry_control.list_tags_for_resource()
        print(response["tags"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_agent_registry_control import AsyncAgentRegistryControlClient


async def main():
    async with AsyncAgentRegistryControlClient() as agent_registry_control:
        # Example: paginate over list_registry_records
        async for item in agent_registry_control.iter_list_registry_records():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_agent_registry_control import AsyncAgentRegistryControlClient
from capo_agent_registry_control.error import AccessDeniedException


async def main():
    async with AsyncAgentRegistryControlClient() as agent_registry_control:
        try:
            await agent_registry_control.list_tags_for_resource()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_agent_registry_control import AsyncAgentRegistryControlClient


async def main():
    async with AsyncAgentRegistryControlClient() as agent_registry_control:
        # Default: 3 attempts for every operation
        response = await agent_registry_control.list_tags_for_resource()

        # Override per operation
        response = await agent_registry_control.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await agent_registry_control.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
