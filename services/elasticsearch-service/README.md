# capo-elasticsearch-service: typed, async Python SDK for AWS Elasticsearch Service

`capo-elasticsearch-service` is a typed Python SDK for AWS Elasticsearch Service. It has an async client, `AsyncElasticsearchServiceClient`, for asyncio and trio, and a sync client, `ElasticsearchServiceClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/elasticsearch-service/](https://capo-sdk.dev/services/elasticsearch-service/)

## Installation

```
pip install capo-elasticsearch-service
```

## Usage

```python
from capo_elasticsearch_service import AsyncElasticsearchServiceClient


async def main():
    async with AsyncElasticsearchServiceClient() as elasticsearch_service:
        # Example: call the accept_inbound_cross_cluster_search_connection operation
        response = await elasticsearch_service.accept_inbound_cross_cluster_search_connection()
        print(response["cross_cluster_search_connection"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_elasticsearch_service import AsyncElasticsearchServiceClient


async def main():
    async with AsyncElasticsearchServiceClient() as elasticsearch_service:
        # Example: paginate over describe_domain_auto_tunes
        async for item in elasticsearch_service.iter_describe_domain_auto_tunes():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_elasticsearch_service import AsyncElasticsearchServiceClient
from capo_elasticsearch_service.error import DisabledOperationException


async def main():
    async with AsyncElasticsearchServiceClient() as elasticsearch_service:
        try:
            await elasticsearch_service.accept_inbound_cross_cluster_search_connection()
        except DisabledOperationException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_elasticsearch_service import AsyncElasticsearchServiceClient


async def main():
    async with AsyncElasticsearchServiceClient() as elasticsearch_service:
        # Default: 3 attempts for every operation
        response = await elasticsearch_service.accept_inbound_cross_cluster_search_connection()

        # Override per operation
        response = await elasticsearch_service.accept_inbound_cross_cluster_search_connection(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await elasticsearch_service.accept_inbound_cross_cluster_search_connection(config_overrides={"retry_max_attempts": 1})
```
