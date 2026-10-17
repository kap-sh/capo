# capo-apigatewaymanagementapi: typed, async Python SDK for AWS Apigatewaymanagementapi

`capo-apigatewaymanagementapi` is a typed Python SDK for AWS Apigatewaymanagementapi. It has an async client, `AsyncApiGatewayManagementApiClient`, for asyncio and trio, and a sync client, `ApiGatewayManagementApiClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/apigatewaymanagementapi/](https://capo-sdk.dev/services/apigatewaymanagementapi/)

## Installation

```
pip install capo-apigatewaymanagementapi
```

## Usage

```python
from capo_apigatewaymanagementapi import AsyncApiGatewayManagementApiClient


async def main():
    async with AsyncApiGatewayManagementApiClient() as api_gateway_management_api:
        # Example: call the delete_connection operation
        response = await api_gateway_management_api.delete_connection()
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_apigatewaymanagementapi import AsyncApiGatewayManagementApiClient
from capo_apigatewaymanagementapi.error import ForbiddenException


async def main():
    async with AsyncApiGatewayManagementApiClient() as api_gateway_management_api:
        try:
            await api_gateway_management_api.delete_connection()
        except ForbiddenException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_apigatewaymanagementapi import AsyncApiGatewayManagementApiClient


async def main():
    async with AsyncApiGatewayManagementApiClient() as api_gateway_management_api:
        # Default: 3 attempts for every operation
        response = await api_gateway_management_api.delete_connection()

        # Override per operation
        response = await api_gateway_management_api.delete_connection(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await api_gateway_management_api.delete_connection(config_overrides={"retry_max_attempts": 1})
```
