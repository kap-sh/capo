# capo-nova-act: typed, async Python SDK for AWS Nova Act

`capo-nova-act` is a typed Python SDK for AWS Nova Act. It has an async client, `AsyncNovaActClient`, for asyncio and trio, and a sync client, `NovaActClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/nova-act/](https://capo-sdk.dev/services/nova-act/)

## Installation

```
pip install capo-nova-act
```

## Usage

```python
from capo_nova_act import AsyncNovaActClient


async def main():
    async with AsyncNovaActClient() as nova_act:
        # Example: call the create_act operation
        response = await nova_act.create_act()
        print(response["act_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_nova_act import AsyncNovaActClient


async def main():
    async with AsyncNovaActClient() as nova_act:
        # Example: paginate over list_acts
        async for item in nova_act.iter_list_acts():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_nova_act import AsyncNovaActClient
from capo_nova_act.error import AccessDeniedException


async def main():
    async with AsyncNovaActClient() as nova_act:
        try:
            await nova_act.create_act()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_nova_act import AsyncNovaActClient


async def main():
    async with AsyncNovaActClient() as nova_act:
        # Default: 3 attempts for every operation
        response = await nova_act.create_act()

        # Override per operation
        response = await nova_act.create_act(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await nova_act.create_act(config_overrides={"retry_max_attempts": 1})
```
