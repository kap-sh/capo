# capo-serverlessapplicationrepository: typed, async Python SDK for AWS Serverlessapplicationrepository

`capo-serverlessapplicationrepository` is a typed Python SDK for AWS Serverlessapplicationrepository. It has an async client, `AsyncServerlessApplicationRepositoryClient`, for asyncio and trio, and a sync client, `ServerlessApplicationRepositoryClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/serverlessapplicationrepository/](https://capo-sdk.dev/services/serverlessapplicationrepository/)

## Installation

```
pip install capo-serverlessapplicationrepository
```

## Usage

```python
from capo_serverlessapplicationrepository import AsyncServerlessApplicationRepositoryClient


async def main():
    async with AsyncServerlessApplicationRepositoryClient() as serverless_application_repository:
        # Example: call the create_application operation
        response = await serverless_application_repository.create_application()
        print(response["application_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_serverlessapplicationrepository import AsyncServerlessApplicationRepositoryClient


async def main():
    async with AsyncServerlessApplicationRepositoryClient() as serverless_application_repository:
        # Example: paginate over list_application_dependencies
        async for item in serverless_application_repository.iter_list_application_dependencies():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_serverlessapplicationrepository import AsyncServerlessApplicationRepositoryClient
from capo_serverlessapplicationrepository.error import BadRequestException


async def main():
    async with AsyncServerlessApplicationRepositoryClient() as serverless_application_repository:
        try:
            await serverless_application_repository.create_application()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_serverlessapplicationrepository import AsyncServerlessApplicationRepositoryClient


async def main():
    async with AsyncServerlessApplicationRepositoryClient() as serverless_application_repository:
        # Default: 3 attempts for every operation
        response = await serverless_application_repository.create_application()

        # Override per operation
        response = await serverless_application_repository.create_application(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await serverless_application_repository.create_application(config_overrides={"retry_max_attempts": 1})
```
