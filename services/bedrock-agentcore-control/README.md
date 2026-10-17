# capo-bedrock-agentcore-control: typed, async Python SDK for AWS Bedrock Agentcore Control

`capo-bedrock-agentcore-control` is a typed Python SDK for AWS Bedrock Agentcore Control. It has an async client, `AsyncBedrockAgentCoreControlClient`, for asyncio and trio, and a sync client, `BedrockAgentCoreControlClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/bedrock-agentcore-control/](https://capo-sdk.dev/services/bedrock-agentcore-control/)

## Installation

```
pip install capo-bedrock-agentcore-control
```

## Usage

```python
from capo_bedrock_agentcore_control import AsyncBedrockAgentCoreControlClient


async def main():
    async with AsyncBedrockAgentCoreControlClient() as bedrock_agent_core_control:
        # Example: call the delete_resource_policy operation
        response = await bedrock_agent_core_control.delete_resource_policy()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_bedrock_agentcore_control import AsyncBedrockAgentCoreControlClient


async def main():
    async with AsyncBedrockAgentCoreControlClient() as bedrock_agent_core_control:
        # Example: paginate over list_agent_runtime_endpoints
        async for item in bedrock_agent_core_control.iter_list_agent_runtime_endpoints():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_bedrock_agentcore_control import AsyncBedrockAgentCoreControlClient
from capo_bedrock_agentcore_control.error import AccessDeniedException


async def main():
    async with AsyncBedrockAgentCoreControlClient() as bedrock_agent_core_control:
        try:
            await bedrock_agent_core_control.delete_resource_policy()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_bedrock_agentcore_control import AsyncBedrockAgentCoreControlClient


async def main():
    async with AsyncBedrockAgentCoreControlClient() as bedrock_agent_core_control:
        # Default: 3 attempts for every operation
        response = await bedrock_agent_core_control.delete_resource_policy()

        # Override per operation
        response = await bedrock_agent_core_control.delete_resource_policy(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await bedrock_agent_core_control.delete_resource_policy(config_overrides={"retry_max_attempts": 1})
```
