# capo-codecommit: typed, async Python SDK for AWS Codecommit

`capo-codecommit` is a typed Python SDK for AWS Codecommit. It has an async client, `AsyncCodeCommitClient`, for asyncio and trio, and a sync client, `CodeCommitClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/codecommit/](https://capo-sdk.dev/services/codecommit/)

## Installation

```
pip install capo-codecommit
```

## Usage

```python
from capo_codecommit import AsyncCodeCommitClient


async def main():
    async with AsyncCodeCommitClient() as code_commit:
        # Example: call the associate_approval_rule_template_with_repository operation
        response = await code_commit.associate_approval_rule_template_with_repository()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_codecommit import AsyncCodeCommitClient


async def main():
    async with AsyncCodeCommitClient() as code_commit:
        # Example: paginate over describe_merge_conflicts
        async for item in code_commit.iter_describe_merge_conflicts():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_codecommit import AsyncCodeCommitClient
from capo_codecommit.error import ApprovalRuleTemplateDoesNotExistException


async def main():
    async with AsyncCodeCommitClient() as code_commit:
        try:
            await code_commit.associate_approval_rule_template_with_repository()
        except ApprovalRuleTemplateDoesNotExistException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_codecommit import AsyncCodeCommitClient


async def main():
    async with AsyncCodeCommitClient() as code_commit:
        # Default: 3 attempts for every operation
        response = await code_commit.associate_approval_rule_template_with_repository()

        # Override per operation
        response = await code_commit.associate_approval_rule_template_with_repository(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await code_commit.associate_approval_rule_template_with_repository(config_overrides={"retry_max_attempts": 1})
```
