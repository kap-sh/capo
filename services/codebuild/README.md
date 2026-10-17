# capo-codebuild: typed, async Python SDK for AWS Codebuild

`capo-codebuild` is a typed Python SDK for AWS Codebuild. It has an async client, `AsyncCodeBuildClient`, for asyncio and trio, and a sync client, `CodeBuildClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/codebuild/](https://capo-sdk.dev/services/codebuild/)

## Installation

```
pip install capo-codebuild
```

## Usage

```python
from capo_codebuild import AsyncCodeBuildClient


async def main():
    async with AsyncCodeBuildClient() as code_build:
        # Example: call the batch_delete_builds operation
        response = await code_build.batch_delete_builds()
        print(response["builds_deleted"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_codebuild import AsyncCodeBuildClient


async def main():
    async with AsyncCodeBuildClient() as code_build:
        # Example: paginate over describe_code_coverages
        async for item in code_build.iter_describe_code_coverages():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_codebuild import AsyncCodeBuildClient
from capo_codebuild.error import InvalidInputException


async def main():
    async with AsyncCodeBuildClient() as code_build:
        try:
            await code_build.batch_delete_builds()
        except InvalidInputException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_codebuild import AsyncCodeBuildClient


async def main():
    async with AsyncCodeBuildClient() as code_build:
        # Default: 3 attempts for every operation
        response = await code_build.batch_delete_builds()

        # Override per operation
        response = await code_build.batch_delete_builds(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await code_build.batch_delete_builds(config_overrides={"retry_max_attempts": 1})
```
