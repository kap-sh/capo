# capo-elastic-load-balancing-v2: typed, async Python SDK for AWS Elastic Load Balancing V2

`capo-elastic-load-balancing-v2` is a typed Python SDK for AWS Elastic Load Balancing V2. It has an async client, `AsyncElasticLoadBalancingv2Client`, for asyncio and trio, and a sync client, `ElasticLoadBalancingv2Client`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/elastic-load-balancing-v2/](https://capo-sdk.dev/services/elastic-load-balancing-v2/)

## Installation

```
pip install capo-elastic-load-balancing-v2
```

## Usage

```python
from capo_elastic_load_balancing_v2 import AsyncElasticLoadBalancingv2Client


async def main():
    async with AsyncElasticLoadBalancingv2Client() as elastic_load_balancingv2:
        # Example: call the add_listener_certificates operation
        response = await elastic_load_balancingv2.add_listener_certificates()
        print(response["certificates"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_elastic_load_balancing_v2 import AsyncElasticLoadBalancingv2Client


async def main():
    async with AsyncElasticLoadBalancingv2Client() as elastic_load_balancingv2:
        # Example: paginate over describe_account_limits
        async for item in elastic_load_balancingv2.iter_describe_account_limits():
            print(item)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_until_` prefixed method.

```python
from capo_elastic_load_balancing_v2 import AsyncElasticLoadBalancingv2Client


async def main():
    async with AsyncElasticLoadBalancingv2Client() as elastic_load_balancingv2:
        # Example: wait for load_balancer_exists
        await elastic_load_balancingv2.wait_until_load_balancer_exists(max_wait_time=300)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_elastic_load_balancing_v2 import AsyncElasticLoadBalancingv2Client
from capo_elastic_load_balancing_v2.error import CertificateNotFoundException


async def main():
    async with AsyncElasticLoadBalancingv2Client() as elastic_load_balancingv2:
        try:
            await elastic_load_balancingv2.add_listener_certificates()
        except CertificateNotFoundException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_elastic_load_balancing_v2 import AsyncElasticLoadBalancingv2Client


async def main():
    async with AsyncElasticLoadBalancingv2Client() as elastic_load_balancingv2:
        # Default: 3 attempts for every operation
        response = await elastic_load_balancingv2.add_listener_certificates()

        # Override per operation
        response = await elastic_load_balancingv2.add_listener_certificates(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await elastic_load_balancingv2.add_listener_certificates(config_overrides={"retry_max_attempts": 1})
```
