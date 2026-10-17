# capo-route53-recovery-readiness: typed, async Python SDK for AWS Route53 Recovery Readiness

`capo-route53-recovery-readiness` is a typed Python SDK for AWS Route53 Recovery Readiness. It has an async client, `AsyncRoute53RecoveryReadinessClient`, for asyncio and trio, and a sync client, `Route53RecoveryReadinessClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/route53-recovery-readiness/](https://capo-sdk.dev/services/route53-recovery-readiness/)

## Installation

```
pip install capo-route53-recovery-readiness
```

## Usage

```python
from capo_route53_recovery_readiness import AsyncRoute53RecoveryReadinessClient


async def main():
    async with AsyncRoute53RecoveryReadinessClient() as route53_recovery_readiness:
        # Example: call the create_cell operation
        response = await route53_recovery_readiness.create_cell()
        print(response["cell_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_route53_recovery_readiness import AsyncRoute53RecoveryReadinessClient


async def main():
    async with AsyncRoute53RecoveryReadinessClient() as route53_recovery_readiness:
        # Example: paginate over get_cell_readiness_summary
        async for item in route53_recovery_readiness.iter_get_cell_readiness_summary():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_route53_recovery_readiness import AsyncRoute53RecoveryReadinessClient
from capo_route53_recovery_readiness.error import AccessDeniedException


async def main():
    async with AsyncRoute53RecoveryReadinessClient() as route53_recovery_readiness:
        try:
            await route53_recovery_readiness.create_cell()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_route53_recovery_readiness import AsyncRoute53RecoveryReadinessClient


async def main():
    async with AsyncRoute53RecoveryReadinessClient() as route53_recovery_readiness:
        # Default: 3 attempts for every operation
        response = await route53_recovery_readiness.create_cell()

        # Override per operation
        response = await route53_recovery_readiness.create_cell(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await route53_recovery_readiness.create_cell(config_overrides={"retry_max_attempts": 1})
```
