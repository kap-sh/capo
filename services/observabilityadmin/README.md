# capo-observabilityadmin: typed, async Python SDK for AWS Observabilityadmin

`capo-observabilityadmin` is a typed Python SDK for AWS Observabilityadmin. It has an async client, `AsyncObservabilityAdminClient`, for asyncio and trio, and a sync client, `ObservabilityAdminClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/observabilityadmin/](https://capo-sdk.dev/services/observabilityadmin/)

## Installation

```
pip install capo-observabilityadmin
```

## Usage

```python
from capo_observabilityadmin import AsyncObservabilityAdminClient


async def main():
    async with AsyncObservabilityAdminClient() as observability_admin:
        # Example: call the create_centralization_rule_for_organization operation
        response = await observability_admin.create_centralization_rule_for_organization()
        print(response["rule_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_observabilityadmin import AsyncObservabilityAdminClient


async def main():
    async with AsyncObservabilityAdminClient() as observability_admin:
        # Example: paginate over list_centralization_rules_for_organization
        async for item in observability_admin.iter_list_centralization_rules_for_organization():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_observabilityadmin import AsyncObservabilityAdminClient
from capo_observabilityadmin.error import AccessDeniedException


async def main():
    async with AsyncObservabilityAdminClient() as observability_admin:
        try:
            await observability_admin.create_centralization_rule_for_organization()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_observabilityadmin import AsyncObservabilityAdminClient


async def main():
    async with AsyncObservabilityAdminClient() as observability_admin:
        # Default: 3 attempts for every operation
        response = await observability_admin.create_centralization_rule_for_organization()

        # Override per operation
        response = await observability_admin.create_centralization_rule_for_organization(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await observability_admin.create_centralization_rule_for_organization(config_overrides={"retry_max_attempts": 1})
```
