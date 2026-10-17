# capo-dynamodb-streams: typed, async Python SDK for AWS Dynamodb Streams

`capo-dynamodb-streams` is a typed Python SDK for AWS Dynamodb Streams. It has an async client, `AsyncDynamoDBStreamsClient`, for asyncio and trio, and a sync client, `DynamoDBStreamsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/dynamodb-streams/](https://capo-sdk.dev/services/dynamodb-streams/)

## Installation

```
pip install capo-dynamodb-streams
```

## Usage

```python
from capo_dynamodb_streams import AsyncDynamoDBStreamsClient


async def main():
    async with AsyncDynamoDBStreamsClient() as dynamo_db_streams:
        # Example: call the describe_stream operation
        response = await dynamo_db_streams.describe_stream()
        print(response["stream_description"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_dynamodb_streams import AsyncDynamoDBStreamsClient
from capo_dynamodb_streams.error import InternalServerError


async def main():
    async with AsyncDynamoDBStreamsClient() as dynamo_db_streams:
        try:
            await dynamo_db_streams.describe_stream()
        except InternalServerError as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_dynamodb_streams import AsyncDynamoDBStreamsClient


async def main():
    async with AsyncDynamoDBStreamsClient() as dynamo_db_streams:
        # Default: 3 attempts for every operation
        response = await dynamo_db_streams.describe_stream()

        # Override per operation
        response = await dynamo_db_streams.describe_stream(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await dynamo_db_streams.describe_stream(config_overrides={"retry_max_attempts": 1})
```
