# capo-resource-groups-tagging-api: typed, async Python SDK for AWS Resource Groups Tagging API

`capo-resource-groups-tagging-api` is a typed Python SDK for AWS Resource Groups Tagging API. It has an async client, `AsyncResourceGroupsTaggingAPIClient`, for asyncio and trio, and a sync client, `ResourceGroupsTaggingAPIClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/resource-groups-tagging-api/](https://capo-sdk.dev/services/resource-groups-tagging-api/)

## Installation

```
pip install capo-resource-groups-tagging-api
```

## Usage

```python
from capo_resource_groups_tagging_api import AsyncResourceGroupsTaggingAPIClient


async def main():
    async with AsyncResourceGroupsTaggingAPIClient() as resource_groups_tagging_api:
        # Example: call the describe_report_creation operation
        response = await resource_groups_tagging_api.describe_report_creation()
        print(response["status"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_resource_groups_tagging_api import AsyncResourceGroupsTaggingAPIClient


async def main():
    async with AsyncResourceGroupsTaggingAPIClient() as resource_groups_tagging_api:
        # Example: paginate over get_compliance_summary
        async for item in resource_groups_tagging_api.iter_get_compliance_summary():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_resource_groups_tagging_api import AsyncResourceGroupsTaggingAPIClient
from capo_resource_groups_tagging_api.error import ConstraintViolationException


async def main():
    async with AsyncResourceGroupsTaggingAPIClient() as resource_groups_tagging_api:
        try:
            await resource_groups_tagging_api.describe_report_creation()
        except ConstraintViolationException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_resource_groups_tagging_api import AsyncResourceGroupsTaggingAPIClient


async def main():
    async with AsyncResourceGroupsTaggingAPIClient() as resource_groups_tagging_api:
        # Default: 3 attempts for every operation
        response = await resource_groups_tagging_api.describe_report_creation()

        # Override per operation
        response = await resource_groups_tagging_api.describe_report_creation(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await resource_groups_tagging_api.describe_report_creation(config_overrides={"retry_max_attempts": 1})
```
