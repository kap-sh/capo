# capo-application-discovery-service: typed, async Python SDK for AWS Application Discovery Service

`capo-application-discovery-service` is a typed Python SDK for AWS Application Discovery Service. It has an async client, `AsyncApplicationDiscoveryServiceClient`, for asyncio and trio, and a sync client, `ApplicationDiscoveryServiceClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/application-discovery-service/](https://capo-sdk.dev/services/application-discovery-service/)

## Installation

```
pip install capo-application-discovery-service
```

## Usage

```python
from capo_application_discovery_service import AsyncApplicationDiscoveryServiceClient


async def main():
    async with AsyncApplicationDiscoveryServiceClient() as application_discovery_service:
        # Example: call the associate_configuration_items_to_application operation
        response = await application_discovery_service.associate_configuration_items_to_application()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_application_discovery_service import AsyncApplicationDiscoveryServiceClient


async def main():
    async with AsyncApplicationDiscoveryServiceClient() as application_discovery_service:
        # Example: paginate over describe_agents
        async for item in application_discovery_service.iter_describe_agents():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_application_discovery_service import AsyncApplicationDiscoveryServiceClient
from capo_application_discovery_service.error import AuthorizationErrorException


async def main():
    async with AsyncApplicationDiscoveryServiceClient() as application_discovery_service:
        try:
            await application_discovery_service.associate_configuration_items_to_application()
        except AuthorizationErrorException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_application_discovery_service import AsyncApplicationDiscoveryServiceClient


async def main():
    async with AsyncApplicationDiscoveryServiceClient() as application_discovery_service:
        # Default: 3 attempts for every operation
        response = await application_discovery_service.associate_configuration_items_to_application()

        # Override per operation
        response = await application_discovery_service.associate_configuration_items_to_application(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await application_discovery_service.associate_configuration_items_to_application(config_overrides={"retry_max_attempts": 1})
```
