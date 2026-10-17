# capo-codedeploy: typed, async Python SDK for AWS Codedeploy

`capo-codedeploy` is a typed Python SDK for AWS Codedeploy. It has an async client, `AsyncCodeDeployClient`, for asyncio and trio, and a sync client, `CodeDeployClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/codedeploy/](https://capo-sdk.dev/services/codedeploy/)

## Installation

```
pip install capo-codedeploy
```

## Usage

```python
from capo_codedeploy import AsyncCodeDeployClient


async def main():
    async with AsyncCodeDeployClient() as code_deploy:
        # Example: call the add_tags_to_on_premises_instances operation
        response = await code_deploy.add_tags_to_on_premises_instances()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_codedeploy import AsyncCodeDeployClient


async def main():
    async with AsyncCodeDeployClient() as code_deploy:
        # Example: paginate over list_application_revisions
        async for item in code_deploy.iter_list_application_revisions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_codedeploy import AsyncCodeDeployClient
from capo_codedeploy.error import InstanceLimitExceededException


async def main():
    async with AsyncCodeDeployClient() as code_deploy:
        try:
            await code_deploy.add_tags_to_on_premises_instances()
        except InstanceLimitExceededException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_codedeploy import AsyncCodeDeployClient


async def main():
    async with AsyncCodeDeployClient() as code_deploy:
        # Default: 3 attempts for every operation
        response = await code_deploy.add_tags_to_on_premises_instances()

        # Override per operation
        response = await code_deploy.add_tags_to_on_premises_instances(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await code_deploy.add_tags_to_on_premises_instances(config_overrides={"retry_max_attempts": 1})
```
