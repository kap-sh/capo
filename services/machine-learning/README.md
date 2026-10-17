# capo-machine-learning: typed, async Python SDK for AWS Machine Learning

`capo-machine-learning` is a typed Python SDK for AWS Machine Learning. It has an async client, `AsyncMachineLearningClient`, for asyncio and trio, and a sync client, `MachineLearningClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/machine-learning/](https://capo-sdk.dev/services/machine-learning/)

## Installation

```
pip install capo-machine-learning
```

## Usage

```python
from capo_machine_learning import AsyncMachineLearningClient


async def main():
    async with AsyncMachineLearningClient() as machine_learning:
        # Example: call the add_tags operation
        response = await machine_learning.add_tags()
        print(response["resource_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_machine_learning import AsyncMachineLearningClient


async def main():
    async with AsyncMachineLearningClient() as machine_learning:
        # Example: paginate over describe_batch_predictions
        async for item in machine_learning.iter_describe_batch_predictions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_machine_learning import AsyncMachineLearningClient
from capo_machine_learning.error import InternalServerException


async def main():
    async with AsyncMachineLearningClient() as machine_learning:
        try:
            await machine_learning.add_tags()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_machine_learning import AsyncMachineLearningClient


async def main():
    async with AsyncMachineLearningClient() as machine_learning:
        # Default: 3 attempts for every operation
        response = await machine_learning.add_tags()

        # Override per operation
        response = await machine_learning.add_tags(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await machine_learning.add_tags(config_overrides={"retry_max_attempts": 1})
```
