# capo-workspaces-instances: typed, async Python SDK for AWS Workspaces Instances

`capo-workspaces-instances` is a typed Python SDK for AWS Workspaces Instances. It has an async client, `AsyncWorkspacesInstancesClient`, for asyncio and trio, and a sync client, `WorkspacesInstancesClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/workspaces-instances/](https://capo-sdk.dev/services/workspaces-instances/)

## Installation

```
pip install capo-workspaces-instances
```

## Usage

```python
from capo_workspaces_instances import AsyncWorkspacesInstancesClient


async def main():
    async with AsyncWorkspacesInstancesClient() as workspaces_instances:
        # Example: call the associate_volume operation
        response = await workspaces_instances.associate_volume()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_workspaces_instances import AsyncWorkspacesInstancesClient


async def main():
    async with AsyncWorkspacesInstancesClient() as workspaces_instances:
        # Example: paginate over list_instance_types
        async for item in workspaces_instances.iter_list_instance_types():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_workspaces_instances import AsyncWorkspacesInstancesClient
from capo_workspaces_instances.error import AccessDeniedException


async def main():
    async with AsyncWorkspacesInstancesClient() as workspaces_instances:
        try:
            await workspaces_instances.associate_volume()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_workspaces_instances import AsyncWorkspacesInstancesClient


async def main():
    async with AsyncWorkspacesInstancesClient() as workspaces_instances:
        # Default: 3 attempts for every operation
        response = await workspaces_instances.associate_volume()

        # Override per operation
        response = await workspaces_instances.associate_volume(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await workspaces_instances.associate_volume(config_overrides={"retry_max_attempts": 1})
```
