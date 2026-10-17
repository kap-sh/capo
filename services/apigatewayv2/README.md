# capo-apigatewayv2: typed, async Python SDK for AWS Apigatewayv2

`capo-apigatewayv2` is a typed Python SDK for AWS Apigatewayv2. It has an async client, `AsyncApiGatewayV2Client`, for asyncio and trio, and a sync client, `ApiGatewayV2Client`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/apigatewayv2/](https://capo-sdk.dev/services/apigatewayv2/)

## Installation

```
pip install capo-apigatewayv2
```

## Usage

```python
from capo_apigatewayv2 import AsyncApiGatewayV2Client


async def main():
    async with AsyncApiGatewayV2Client() as api_gateway_v2:
        # Example: call the create_api operation
        response = await api_gateway_v2.create_api()
        print(response["api_endpoint"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_apigatewayv2 import AsyncApiGatewayV2Client


async def main():
    async with AsyncApiGatewayV2Client() as api_gateway_v2:
        # Example: paginate over list_routing_rules
        async for item in api_gateway_v2.iter_list_routing_rules():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_apigatewayv2 import AsyncApiGatewayV2Client
from capo_apigatewayv2.error import BadRequestException


async def main():
    async with AsyncApiGatewayV2Client() as api_gateway_v2:
        try:
            await api_gateway_v2.create_api()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_apigatewayv2 import AsyncApiGatewayV2Client


async def main():
    async with AsyncApiGatewayV2Client() as api_gateway_v2:
        # Default: 3 attempts for every operation
        response = await api_gateway_v2.create_api()

        # Override per operation
        response = await api_gateway_v2.create_api(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await api_gateway_v2.create_api(config_overrides={"retry_max_attempts": 1})
```
