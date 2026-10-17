# capo-route53resolver: typed, async Python SDK for AWS Route53Resolver

`capo-route53resolver` is a typed Python SDK for AWS Route53Resolver. It has an async client, `AsyncRoute53ResolverClient`, for asyncio and trio, and a sync client, `Route53ResolverClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/route53resolver/](https://capo-sdk.dev/services/route53resolver/)

## Installation

```
pip install capo-route53resolver
```

## Usage

```python
from capo_route53resolver import AsyncRoute53ResolverClient


async def main():
    async with AsyncRoute53ResolverClient() as route53_resolver:
        # Example: call the associate_firewall_rule_group operation
        response = await route53_resolver.associate_firewall_rule_group()
        print(response["firewall_rule_group_association"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_route53resolver import AsyncRoute53ResolverClient


async def main():
    async with AsyncRoute53ResolverClient() as route53_resolver:
        # Example: paginate over list_firewall_configs
        async for item in route53_resolver.iter_list_firewall_configs():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_route53resolver import AsyncRoute53ResolverClient
from capo_route53resolver.error import AccessDeniedException


async def main():
    async with AsyncRoute53ResolverClient() as route53_resolver:
        try:
            await route53_resolver.associate_firewall_rule_group()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_route53resolver import AsyncRoute53ResolverClient


async def main():
    async with AsyncRoute53ResolverClient() as route53_resolver:
        # Default: 3 attempts for every operation
        response = await route53_resolver.associate_firewall_rule_group()

        # Override per operation
        response = await route53_resolver.associate_firewall_rule_group(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await route53_resolver.associate_firewall_rule_group(config_overrides={"retry_max_attempts": 1})
```
