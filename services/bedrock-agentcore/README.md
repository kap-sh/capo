# capo-bedrock-agentcore: typed, async Python SDK for AWS Bedrock Agentcore

`capo-bedrock-agentcore` is a typed Python SDK for AWS Bedrock Agentcore. It has an async client, `AsyncBedrockAgentCoreClient`, for asyncio and trio, and a sync client, `BedrockAgentCoreClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/bedrock-agentcore/](https://capo-sdk.dev/services/bedrock-agentcore/)

## Installation

```
pip install capo-bedrock-agentcore
```

## Usage

```python
from capo_bedrock_agentcore import AsyncBedrockAgentCoreClient


async def main():
    async with AsyncBedrockAgentCoreClient() as bedrock_agent_core:
        # Example: call the complete_resource_token_auth operation
        response = await bedrock_agent_core.complete_resource_token_auth()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_bedrock_agentcore import AsyncBedrockAgentCoreClient


async def main():
    async with AsyncBedrockAgentCoreClient() as bedrock_agent_core:
        # Example: paginate over list_ab_tests
        async for item in bedrock_agent_core.iter_list_ab_tests():
            print(item)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_bedrock_agentcore import AsyncBedrockAgentCoreClient


async def main():
    async with AsyncBedrockAgentCoreClient() as bedrock_agent_core:
        # Example: call invoke_agent_runtime and read the streaming response
        async with bedrock_agent_core.invoke_agent_runtime() as response:
            async for chunk in response["response"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_bedrock_agentcore import AsyncBedrockAgentCoreClient
from capo_bedrock_agentcore.error import AccessDeniedException


async def main():
    async with AsyncBedrockAgentCoreClient() as bedrock_agent_core:
        try:
            await bedrock_agent_core.complete_resource_token_auth()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_bedrock_agentcore import AsyncBedrockAgentCoreClient


async def main():
    async with AsyncBedrockAgentCoreClient() as bedrock_agent_core:
        # Default: 3 attempts for every operation
        response = await bedrock_agent_core.complete_resource_token_auth()

        # Override per operation
        response = await bedrock_agent_core.complete_resource_token_auth(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await bedrock_agent_core.complete_resource_token_auth(config_overrides={"retry_max_attempts": 1})
```
