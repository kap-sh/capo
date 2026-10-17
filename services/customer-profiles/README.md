# capo-customer-profiles: typed, async Python SDK for AWS Customer Profiles

`capo-customer-profiles` is a typed Python SDK for AWS Customer Profiles. It has an async client, `AsyncCustomerProfilesClient`, for asyncio and trio, and a sync client, `CustomerProfilesClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/customer-profiles/](https://capo-sdk.dev/services/customer-profiles/)

## Installation

```
pip install capo-customer-profiles
```

## Usage

```python
from capo_customer_profiles import AsyncCustomerProfilesClient


async def main():
    async with AsyncCustomerProfilesClient() as customer_profiles:
        # Example: call the add_profile_key operation
        response = await customer_profiles.add_profile_key()
        print(response["key_name"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_customer_profiles import AsyncCustomerProfilesClient


async def main():
    async with AsyncCustomerProfilesClient() as customer_profiles:
        # Example: paginate over get_similar_profiles
        async for item in customer_profiles.iter_get_similar_profiles():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_customer_profiles import AsyncCustomerProfilesClient
from capo_customer_profiles.error import AccessDeniedException


async def main():
    async with AsyncCustomerProfilesClient() as customer_profiles:
        try:
            await customer_profiles.add_profile_key()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_customer_profiles import AsyncCustomerProfilesClient


async def main():
    async with AsyncCustomerProfilesClient() as customer_profiles:
        # Default: 3 attempts for every operation
        response = await customer_profiles.add_profile_key()

        # Override per operation
        response = await customer_profiles.add_profile_key(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await customer_profiles.add_profile_key(config_overrides={"retry_max_attempts": 1})
```
