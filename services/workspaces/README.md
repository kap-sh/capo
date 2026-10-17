# capo-workspaces: typed, async Python SDK for AWS Workspaces

`capo-workspaces` is a typed Python SDK for AWS Workspaces. It has an async client, `AsyncWorkSpacesClient`, for asyncio and trio, and a sync client, `WorkSpacesClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/workspaces/](https://capo-sdk.dev/services/workspaces/)

## Installation

```
pip install capo-workspaces
```

## Usage

```python
from capo_workspaces import AsyncWorkSpacesClient


async def main():
    async with AsyncWorkSpacesClient() as work_spaces:
        # Example: call the accept_account_link_invitation operation
        response = await work_spaces.accept_account_link_invitation()
        print(response["account_link"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_workspaces import AsyncWorkSpacesClient


async def main():
    async with AsyncWorkSpacesClient() as work_spaces:
        # Example: paginate over describe_application_associations
        async for item in work_spaces.iter_describe_application_associations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_workspaces import AsyncWorkSpacesClient
from capo_workspaces.error import AccessDeniedException


async def main():
    async with AsyncWorkSpacesClient() as work_spaces:
        try:
            await work_spaces.accept_account_link_invitation()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_workspaces import AsyncWorkSpacesClient


async def main():
    async with AsyncWorkSpacesClient() as work_spaces:
        # Default: 3 attempts for every operation
        response = await work_spaces.accept_account_link_invitation()

        # Override per operation
        response = await work_spaces.accept_account_link_invitation(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await work_spaces.accept_account_link_invitation(config_overrides={"retry_max_attempts": 1})
```
