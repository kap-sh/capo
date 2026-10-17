# capo-route53profiles: typed, async Python SDK for AWS Route53Profiles

`capo-route53profiles` is a typed Python SDK for AWS Route53Profiles. It has an async client, `AsyncRoute53ProfilesClient`, for asyncio and trio, and a sync client, `Route53ProfilesClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/route53profiles/](https://capo-sdk.dev/services/route53profiles/)

## Installation

```
pip install capo-route53profiles
```

## Usage

```python
from capo_route53profiles import AsyncRoute53ProfilesClient


async def main():
    async with AsyncRoute53ProfilesClient() as route53_profiles:
        # Example: call the associate_profile operation
        response = await route53_profiles.associate_profile()
        print(response["profile_association"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_route53profiles import AsyncRoute53ProfilesClient


async def main():
    async with AsyncRoute53ProfilesClient() as route53_profiles:
        # Example: paginate over list_profile_associations
        async for item in route53_profiles.iter_list_profile_associations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_route53profiles import AsyncRoute53ProfilesClient
from capo_route53profiles.error import AccessDeniedException


async def main():
    async with AsyncRoute53ProfilesClient() as route53_profiles:
        try:
            await route53_profiles.associate_profile()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_route53profiles import AsyncRoute53ProfilesClient


async def main():
    async with AsyncRoute53ProfilesClient() as route53_profiles:
        # Default: 3 attempts for every operation
        response = await route53_profiles.associate_profile()

        # Override per operation
        response = await route53_profiles.associate_profile(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await route53_profiles.associate_profile(config_overrides={"retry_max_attempts": 1})
```
