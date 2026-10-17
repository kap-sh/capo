# capo-securityagent: typed, async Python SDK for AWS Securityagent

`capo-securityagent` is a typed Python SDK for AWS Securityagent. It has an async client, `AsyncSecurityAgentClient`, for asyncio and trio, and a sync client, `SecurityAgentClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/securityagent/](https://capo-sdk.dev/services/securityagent/)

## Installation

```
pip install capo-securityagent
```

## Usage

```python
from capo_securityagent import AsyncSecurityAgentClient


async def main():
    async with AsyncSecurityAgentClient() as security_agent:
        # Example: call the add_artifact operation
        response = await security_agent.add_artifact()
        print(response["artifact_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_securityagent import AsyncSecurityAgentClient


async def main():
    async with AsyncSecurityAgentClient() as security_agent:
        # Example: paginate over list_actor_messages
        async for item in security_agent.iter_list_actor_messages():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_securityagent import AsyncSecurityAgentClient
from capo_securityagent.error import AccessDeniedException


async def main():
    async with AsyncSecurityAgentClient() as security_agent:
        try:
            await security_agent.add_artifact()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_securityagent import AsyncSecurityAgentClient


async def main():
    async with AsyncSecurityAgentClient() as security_agent:
        # Default: 3 attempts for every operation
        response = await security_agent.add_artifact()

        # Override per operation
        response = await security_agent.add_artifact(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await security_agent.add_artifact(config_overrides={"retry_max_attempts": 1})
```
