# capo-dynamodb: typed, async Python SDK for Amazon DynamoDB

`capo-dynamodb` is a typed Python SDK for Amazon DynamoDB. It has an async client, `AsyncDynamoDBClient`, for asyncio and trio, and a sync client, `DynamoDBClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/dynamodb/](https://capo-sdk.dev/services/dynamodb/)

## Installation

```
pip install capo-dynamodb
```

## Usage

```python
from capo_dynamodb import AsyncDynamoDBClient


async def main():
    async with AsyncDynamoDBClient() as dynamo_db:
        # Example: call the batch_execute_statement operation
        response = await dynamo_db.batch_execute_statement()
        print(response["responses"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_dynamodb import AsyncDynamoDBClient


async def main():
    async with AsyncDynamoDBClient() as dynamo_db:
        # Example: paginate over list_contributor_insights
        async for item in dynamo_db.iter_list_contributor_insights():
            print(item)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_until_` prefixed method.

```python
from capo_dynamodb import AsyncDynamoDBClient


async def main():
    async with AsyncDynamoDBClient() as dynamo_db:
        # Example: wait for table_not_exists
        await dynamo_db.wait_until_table_not_exists(max_wait_time=300)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_dynamodb import AsyncDynamoDBClient
from capo_dynamodb.error import InternalServerError


async def main():
    async with AsyncDynamoDBClient() as dynamo_db:
        try:
            await dynamo_db.batch_execute_statement()
        except InternalServerError as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_dynamodb import AsyncDynamoDBClient


async def main():
    async with AsyncDynamoDBClient() as dynamo_db:
        # Default: 3 attempts for every operation
        response = await dynamo_db.batch_execute_statement()

        # Override per operation
        response = await dynamo_db.batch_execute_statement(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await dynamo_db.batch_execute_statement(config_overrides={"retry_max_attempts": 1})
```
