# capo-devops-guru: typed, async Python SDK for AWS Devops Guru

`capo-devops-guru` is a typed Python SDK for AWS Devops Guru. It has an async client, `AsyncDevOpsGuruClient`, for asyncio and trio, and a sync client, `DevOpsGuruClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/devops-guru/](https://capo-sdk.dev/services/devops-guru/)

## Installation

```
pip install capo-devops-guru
```

## Usage

```python
from capo_devops_guru import AsyncDevOpsGuruClient


async def main():
    async with AsyncDevOpsGuruClient() as dev_ops_guru:
        # Example: call the add_notification_channel operation
        response = await dev_ops_guru.add_notification_channel()
        print(response["id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_devops_guru import AsyncDevOpsGuruClient


async def main():
    async with AsyncDevOpsGuruClient() as dev_ops_guru:
        # Example: paginate over describe_organization_resource_collection_health
        async for item in dev_ops_guru.iter_describe_organization_resource_collection_health():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_devops_guru import AsyncDevOpsGuruClient
from capo_devops_guru.error import AccessDeniedException


async def main():
    async with AsyncDevOpsGuruClient() as dev_ops_guru:
        try:
            await dev_ops_guru.add_notification_channel()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_devops_guru import AsyncDevOpsGuruClient


async def main():
    async with AsyncDevOpsGuruClient() as dev_ops_guru:
        # Default: 3 attempts for every operation
        response = await dev_ops_guru.add_notification_channel()

        # Override per operation
        response = await dev_ops_guru.add_notification_channel(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await dev_ops_guru.add_notification_channel(config_overrides={"retry_max_attempts": 1})
```
