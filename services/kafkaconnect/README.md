# capo-kafkaconnect: typed, async Python SDK for AWS Kafkaconnect

`capo-kafkaconnect` is a typed Python SDK for AWS Kafkaconnect. It has an async client, `AsyncKafkaConnectClient`, for asyncio and trio, and a sync client, `KafkaConnectClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/kafkaconnect/](https://capo-sdk.dev/services/kafkaconnect/)

## Installation

```
pip install capo-kafkaconnect
```

## Usage

```python
from capo_kafkaconnect import AsyncKafkaConnectClient


async def main():
    async with AsyncKafkaConnectClient() as kafka_connect:
        # Example: call the create_connector operation
        response = await kafka_connect.create_connector()
        print(response["connector_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_kafkaconnect import AsyncKafkaConnectClient


async def main():
    async with AsyncKafkaConnectClient() as kafka_connect:
        # Example: paginate over list_connector_operations
        async for item in kafka_connect.iter_list_connector_operations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_kafkaconnect import AsyncKafkaConnectClient
from capo_kafkaconnect.error import BadRequestException


async def main():
    async with AsyncKafkaConnectClient() as kafka_connect:
        try:
            await kafka_connect.create_connector()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_kafkaconnect import AsyncKafkaConnectClient


async def main():
    async with AsyncKafkaConnectClient() as kafka_connect:
        # Default: 3 attempts for every operation
        response = await kafka_connect.create_connector()

        # Override per operation
        response = await kafka_connect.create_connector(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await kafka_connect.create_connector(config_overrides={"retry_max_attempts": 1})
```
