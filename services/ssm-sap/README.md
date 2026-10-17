# capo-ssm-sap: typed, async Python SDK for AWS SSM Sap

`capo-ssm-sap` is a typed Python SDK for AWS SSM Sap. It has an async client, `AsyncSsmSapClient`, for asyncio and trio, and a sync client, `SsmSapClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/ssm-sap/](https://capo-sdk.dev/services/ssm-sap/)

## Installation

```
pip install capo-ssm-sap
```

## Usage

```python
from capo_ssm_sap import AsyncSsmSapClient


async def main():
    async with AsyncSsmSapClient() as ssm_sap:
        # Example: call the delete_resource_permission operation
        response = await ssm_sap.delete_resource_permission()
        print(response["policy"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_ssm_sap import AsyncSsmSapClient


async def main():
    async with AsyncSsmSapClient() as ssm_sap:
        # Example: paginate over list_applications
        async for item in ssm_sap.iter_list_applications():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_ssm_sap import AsyncSsmSapClient
from capo_ssm_sap.error import InternalServerException


async def main():
    async with AsyncSsmSapClient() as ssm_sap:
        try:
            await ssm_sap.delete_resource_permission()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_ssm_sap import AsyncSsmSapClient


async def main():
    async with AsyncSsmSapClient() as ssm_sap:
        # Default: 3 attempts for every operation
        response = await ssm_sap.delete_resource_permission()

        # Override per operation
        response = await ssm_sap.delete_resource_permission(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await ssm_sap.delete_resource_permission(config_overrides={"retry_max_attempts": 1})
```
