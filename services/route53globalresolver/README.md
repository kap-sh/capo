# capo-route53globalresolver: typed, async Python SDK for AWS Route53Globalresolver

`capo-route53globalresolver` is a typed Python SDK for AWS Route53Globalresolver. It has an async client, `AsyncRoute53GlobalResolverClient`, for asyncio and trio, and a sync client, `Route53GlobalResolverClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/route53globalresolver/](https://capo-sdk.dev/services/route53globalresolver/)

## Installation

```
pip install capo-route53globalresolver
```

## Usage

```python
from capo_route53globalresolver import AsyncRoute53GlobalResolverClient


async def main():
    async with AsyncRoute53GlobalResolverClient() as route53_global_resolver:
        # Example: call the disassociate_hosted_zone operation
        response = await route53_global_resolver.disassociate_hosted_zone()
        print(response["id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_route53globalresolver import AsyncRoute53GlobalResolverClient


async def main():
    async with AsyncRoute53GlobalResolverClient() as route53_global_resolver:
        # Example: paginate over list_shared_dns_views
        async for item in route53_global_resolver.iter_list_shared_dns_views():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_route53globalresolver import AsyncRoute53GlobalResolverClient
from capo_route53globalresolver.error import AccessDeniedException


async def main():
    async with AsyncRoute53GlobalResolverClient() as route53_global_resolver:
        try:
            await route53_global_resolver.disassociate_hosted_zone()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_route53globalresolver import AsyncRoute53GlobalResolverClient


async def main():
    async with AsyncRoute53GlobalResolverClient() as route53_global_resolver:
        # Default: 3 attempts for every operation
        response = await route53_global_resolver.disassociate_hosted_zone()

        # Override per operation
        response = await route53_global_resolver.disassociate_hosted_zone(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await route53_global_resolver.disassociate_hosted_zone(config_overrides={"retry_max_attempts": 1})
```
