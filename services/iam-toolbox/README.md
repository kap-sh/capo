# capo-iam-toolbox: typed, async Python SDK for AWS IAM Toolbox

`capo-iam-toolbox` is a typed Python SDK for AWS IAM Toolbox. It has an async client, `AsyncIAMToolboxClient`, for asyncio and trio, and a sync client, `IAMToolboxClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/iam-toolbox/](https://capo-sdk.dev/services/iam-toolbox/)

## Installation

```
pip install capo-iam-toolbox
```

## Usage

```python
from capo_iam_toolbox import AsyncIAMToolboxClient


async def main():
    async with AsyncIAMToolboxClient() as iam_toolbox:
        # Example: call the get_request_authorization_details operation
        response = await iam_toolbox.get_request_authorization_details()
        print(response["request_context"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_iam_toolbox import AsyncIAMToolboxClient


async def main():
    async with AsyncIAMToolboxClient() as iam_toolbox:
        # Example: paginate over get_request_authorization_details
        async for item in iam_toolbox.iter_get_request_authorization_details():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_iam_toolbox import AsyncIAMToolboxClient
from capo_iam_toolbox.error import AccessDeniedException


async def main():
    async with AsyncIAMToolboxClient() as iam_toolbox:
        try:
            await iam_toolbox.get_request_authorization_details()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_iam_toolbox import AsyncIAMToolboxClient


async def main():
    async with AsyncIAMToolboxClient() as iam_toolbox:
        # Default: 3 attempts for every operation
        response = await iam_toolbox.get_request_authorization_details()

        # Override per operation
        response = await iam_toolbox.get_request_authorization_details(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await iam_toolbox.get_request_authorization_details(config_overrides={"retry_max_attempts": 1})
```
