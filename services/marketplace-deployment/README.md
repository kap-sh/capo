# capo-marketplace-deployment: typed, async Python SDK for AWS Marketplace Deployment

`capo-marketplace-deployment` is a typed Python SDK for AWS Marketplace Deployment. It has an async client, `AsyncMarketplaceDeploymentClient`, for asyncio and trio, and a sync client, `MarketplaceDeploymentClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/marketplace-deployment/](https://capo-sdk.dev/services/marketplace-deployment/)

## Installation

```
pip install capo-marketplace-deployment
```

## Usage

```python
from capo_marketplace_deployment import AsyncMarketplaceDeploymentClient


async def main():
    async with AsyncMarketplaceDeploymentClient() as marketplace_deployment:
        # Example: call the list_tags_for_resource operation
        response = await marketplace_deployment.list_tags_for_resource()
        print(response["tags"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_marketplace_deployment import AsyncMarketplaceDeploymentClient
from capo_marketplace_deployment.error import AccessDeniedException


async def main():
    async with AsyncMarketplaceDeploymentClient() as marketplace_deployment:
        try:
            await marketplace_deployment.list_tags_for_resource()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_marketplace_deployment import AsyncMarketplaceDeploymentClient


async def main():
    async with AsyncMarketplaceDeploymentClient() as marketplace_deployment:
        # Default: 3 attempts for every operation
        response = await marketplace_deployment.list_tags_for_resource()

        # Override per operation
        response = await marketplace_deployment.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await marketplace_deployment.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
