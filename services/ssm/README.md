# capo-ssm: typed, async Python SDK for AWS SSM

`capo-ssm` is a typed Python SDK for AWS SSM. It has an async client, `AsyncSSMClient`, for asyncio and trio, and a sync client, `SSMClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/ssm/](https://capo-sdk.dev/services/ssm/)

## Installation

```
pip install capo-ssm
```

## Usage

```python
from capo_ssm import AsyncSSMClient


async def main():
    async with AsyncSSMClient() as ssm:
        # Example: call the add_tags_to_resource operation
        response = await ssm.add_tags_to_resource()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_ssm import AsyncSSMClient


async def main():
    async with AsyncSSMClient() as ssm:
        # Example: paginate over describe_activations
        async for item in ssm.iter_describe_activations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_ssm import AsyncSSMClient
from capo_ssm.error import InternalServerError


async def main():
    async with AsyncSSMClient() as ssm:
        try:
            await ssm.add_tags_to_resource()
        except InternalServerError as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_ssm import AsyncSSMClient


async def main():
    async with AsyncSSMClient() as ssm:
        # Default: 3 attempts for every operation
        response = await ssm.add_tags_to_resource()

        # Override per operation
        response = await ssm.add_tags_to_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await ssm.add_tags_to_resource(config_overrides={"retry_max_attempts": 1})
```
