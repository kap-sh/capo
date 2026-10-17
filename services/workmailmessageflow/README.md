# capo-workmailmessageflow: typed, async Python SDK for AWS Workmailmessageflow

`capo-workmailmessageflow` is a typed Python SDK for AWS Workmailmessageflow. It has an async client, `AsyncWorkMailMessageFlowClient`, for asyncio and trio, and a sync client, `WorkMailMessageFlowClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/workmailmessageflow/](https://capo-sdk.dev/services/workmailmessageflow/)

## Installation

```
pip install capo-workmailmessageflow
```

## Usage

```python
from capo_workmailmessageflow import AsyncWorkMailMessageFlowClient


async def main():
    async with AsyncWorkMailMessageFlowClient() as work_mail_message_flow:
        # Example: call the get_raw_message_content operation
        response = await work_mail_message_flow.get_raw_message_content()
        print(response["message_content"])
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_workmailmessageflow import AsyncWorkMailMessageFlowClient


async def main():
    async with AsyncWorkMailMessageFlowClient() as work_mail_message_flow:
        # Example: call get_raw_message_content and read the streaming response
        async with work_mail_message_flow.get_raw_message_content() as response:
            async for chunk in response["message_content"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_workmailmessageflow import AsyncWorkMailMessageFlowClient
from capo_workmailmessageflow.error import ResourceNotFoundException


async def main():
    async with AsyncWorkMailMessageFlowClient() as work_mail_message_flow:
        try:
            await work_mail_message_flow.get_raw_message_content()
        except ResourceNotFoundException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_workmailmessageflow import AsyncWorkMailMessageFlowClient


async def main():
    async with AsyncWorkMailMessageFlowClient() as work_mail_message_flow:
        # Default: 3 attempts for every operation
        response = await work_mail_message_flow.get_raw_message_content()

        # Override per operation
        response = await work_mail_message_flow.get_raw_message_content(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await work_mail_message_flow.get_raw_message_content(config_overrides={"retry_max_attempts": 1})
```
