# capo-elasticache: typed, async Python SDK for AWS Elasticache

`capo-elasticache` is a typed Python SDK for AWS Elasticache. It has an async client, `AsyncElastiCacheClient`, for asyncio and trio, and a sync client, `ElastiCacheClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/elasticache/](https://capo-sdk.dev/services/elasticache/)

## Installation

```
pip install capo-elasticache
```

## Usage

```python
from capo_elasticache import AsyncElastiCacheClient


async def main():
    async with AsyncElastiCacheClient() as elasti_cache:
        # Example: call the add_tags_to_resource operation
        response = await elasti_cache.add_tags_to_resource()
        print(response["tag_list"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_elasticache import AsyncElastiCacheClient


async def main():
    async with AsyncElastiCacheClient() as elasti_cache:
        # Example: paginate over describe_cache_clusters
        async for item in elasti_cache.iter_describe_cache_clusters():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_elasticache import AsyncElastiCacheClient
from capo_elasticache.error import CacheClusterNotFoundFault


async def main():
    async with AsyncElastiCacheClient() as elasti_cache:
        try:
            await elasti_cache.add_tags_to_resource()
        except CacheClusterNotFoundFault as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_elasticache import AsyncElastiCacheClient


async def main():
    async with AsyncElastiCacheClient() as elasti_cache:
        # Default: 3 attempts for every operation
        response = await elasti_cache.add_tags_to_resource()

        # Override per operation
        response = await elasti_cache.add_tags_to_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await elasti_cache.add_tags_to_resource(config_overrides={"retry_max_attempts": 1})
```
