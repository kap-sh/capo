# capo-emr-containers: typed, async Python SDK for AWS EMR Containers

`capo-emr-containers` is a typed Python SDK for AWS EMR Containers. It has an async client, `AsyncEMRcontainersClient`, for asyncio and trio, and a sync client, `EMRcontainersClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/emr-containers/](https://capo-sdk.dev/services/emr-containers/)

## Installation

```
pip install capo-emr-containers
```

## Usage

```python
from capo_emr_containers import AsyncEMRcontainersClient


async def main():
    async with AsyncEMRcontainersClient() as em_rcontainers:
        # Example: call the cancel_job_run operation
        response = await em_rcontainers.cancel_job_run()
        print(response["id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_emr_containers import AsyncEMRcontainersClient


async def main():
    async with AsyncEMRcontainersClient() as em_rcontainers:
        # Example: paginate over list_job_runs
        async for item in em_rcontainers.iter_list_job_runs():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_emr_containers import AsyncEMRcontainersClient
from capo_emr_containers.error import InternalServerException


async def main():
    async with AsyncEMRcontainersClient() as em_rcontainers:
        try:
            await em_rcontainers.cancel_job_run()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_emr_containers import AsyncEMRcontainersClient


async def main():
    async with AsyncEMRcontainersClient() as em_rcontainers:
        # Default: 3 attempts for every operation
        response = await em_rcontainers.cancel_job_run()

        # Override per operation
        response = await em_rcontainers.cancel_job_run(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await em_rcontainers.cancel_job_run(config_overrides={"retry_max_attempts": 1})
```
