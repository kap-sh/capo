# capo-amplifyuibuilder: typed, async Python SDK for AWS Amplifyuibuilder

`capo-amplifyuibuilder` is a typed Python SDK for AWS Amplifyuibuilder. It has an async client, `AsyncAmplifyUIBuilderClient`, for asyncio and trio, and a sync client, `AmplifyUIBuilderClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/amplifyuibuilder/](https://capo-sdk.dev/services/amplifyuibuilder/)

## Installation

```
pip install capo-amplifyuibuilder
```

## Usage

```python
from capo_amplifyuibuilder import AsyncAmplifyUIBuilderClient


async def main():
    async with AsyncAmplifyUIBuilderClient() as amplify_ui_builder:
        # Example: call the exchange_code_for_token operation
        response = await amplify_ui_builder.exchange_code_for_token()
        print(response["access_token"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_amplifyuibuilder import AsyncAmplifyUIBuilderClient


async def main():
    async with AsyncAmplifyUIBuilderClient() as amplify_ui_builder:
        # Example: paginate over list_codegen_jobs
        async for item in amplify_ui_builder.iter_list_codegen_jobs():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_amplifyuibuilder import AsyncAmplifyUIBuilderClient
from capo_amplifyuibuilder.error import InvalidParameterException


async def main():
    async with AsyncAmplifyUIBuilderClient() as amplify_ui_builder:
        try:
            await amplify_ui_builder.exchange_code_for_token()
        except InvalidParameterException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_amplifyuibuilder import AsyncAmplifyUIBuilderClient


async def main():
    async with AsyncAmplifyUIBuilderClient() as amplify_ui_builder:
        # Default: 3 attempts for every operation
        response = await amplify_ui_builder.exchange_code_for_token()

        # Override per operation
        response = await amplify_ui_builder.exchange_code_for_token(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await amplify_ui_builder.exchange_code_for_token(config_overrides={"retry_max_attempts": 1})
```
