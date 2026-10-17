# capo-route-53-domains: typed, async Python SDK for AWS Route 53 Domains

`capo-route-53-domains` is a typed Python SDK for AWS Route 53 Domains. It has an async client, `AsyncRoute53DomainsClient`, for asyncio and trio, and a sync client, `Route53DomainsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/route-53-domains/](https://capo-sdk.dev/services/route-53-domains/)

## Installation

```
pip install capo-route-53-domains
```

## Usage

```python
from capo_route_53_domains import AsyncRoute53DomainsClient


async def main():
    async with AsyncRoute53DomainsClient() as route53_domains:
        # Example: call the accept_domain_transfer_from_another_aws_account operation
        response = await route53_domains.accept_domain_transfer_from_another_aws_account()
        print(response["operation_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_route_53_domains import AsyncRoute53DomainsClient


async def main():
    async with AsyncRoute53DomainsClient() as route53_domains:
        # Example: paginate over list_domains
        async for item in route53_domains.iter_list_domains():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_route_53_domains import AsyncRoute53DomainsClient
from capo_route_53_domains.error import DomainLimitExceeded


async def main():
    async with AsyncRoute53DomainsClient() as route53_domains:
        try:
            await route53_domains.accept_domain_transfer_from_another_aws_account()
        except DomainLimitExceeded as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_route_53_domains import AsyncRoute53DomainsClient


async def main():
    async with AsyncRoute53DomainsClient() as route53_domains:
        # Default: 3 attempts for every operation
        response = await route53_domains.accept_domain_transfer_from_another_aws_account()

        # Override per operation
        response = await route53_domains.accept_domain_transfer_from_another_aws_account(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await route53_domains.accept_domain_transfer_from_another_aws_account(config_overrides={"retry_max_attempts": 1})
```
