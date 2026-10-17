# capo-ssm-incidents: typed, async Python SDK for AWS SSM Incidents

`capo-ssm-incidents` is a typed Python SDK for AWS SSM Incidents. It has an async client, `AsyncSSMIncidentsClient`, for asyncio and trio, and a sync client, `SSMIncidentsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/ssm-incidents/](https://capo-sdk.dev/services/ssm-incidents/)

## Installation

```
pip install capo-ssm-incidents
```

## Usage

```python
from capo_ssm_incidents import AsyncSSMIncidentsClient


async def main():
    async with AsyncSSMIncidentsClient() as ssm_incidents:
        # Example: call the batch_get_incident_findings operation
        response = await ssm_incidents.batch_get_incident_findings()
        print(response["findings"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_ssm_incidents import AsyncSSMIncidentsClient


async def main():
    async with AsyncSSMIncidentsClient() as ssm_incidents:
        # Example: paginate over get_resource_policies
        async for item in ssm_incidents.iter_get_resource_policies():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_ssm_incidents import AsyncSSMIncidentsClient
from capo_ssm_incidents.error import AccessDeniedException


async def main():
    async with AsyncSSMIncidentsClient() as ssm_incidents:
        try:
            await ssm_incidents.batch_get_incident_findings()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_ssm_incidents import AsyncSSMIncidentsClient


async def main():
    async with AsyncSSMIncidentsClient() as ssm_incidents:
        # Default: 3 attempts for every operation
        response = await ssm_incidents.batch_get_incident_findings()

        # Override per operation
        response = await ssm_incidents.batch_get_incident_findings(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await ssm_incidents.batch_get_incident_findings(config_overrides={"retry_max_attempts": 1})
```
