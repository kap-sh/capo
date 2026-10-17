# capo-rds-data: typed, async Python SDK for AWS RDS Data

`capo-rds-data` is a typed Python SDK for AWS RDS Data. It has an async client, `AsyncRDSDataClient`, for asyncio and trio, and a sync client, `RDSDataClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/rds-data/](https://capo-sdk.dev/services/rds-data/)

## Installation

```
pip install capo-rds-data
```

## Usage

```python
from capo_rds_data import AsyncRDSDataClient


async def main():
    async with AsyncRDSDataClient() as rds_data:
        # Example: call the batch_execute_statement operation
        response = await rds_data.batch_execute_statement()
        print(response["update_results"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_rds_data import AsyncRDSDataClient
from capo_rds_data.error import AccessDeniedException


async def main():
    async with AsyncRDSDataClient() as rds_data:
        try:
            await rds_data.batch_execute_statement()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_rds_data import AsyncRDSDataClient


async def main():
    async with AsyncRDSDataClient() as rds_data:
        # Default: 3 attempts for every operation
        response = await rds_data.batch_execute_statement()

        # Override per operation
        response = await rds_data.batch_execute_statement(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await rds_data.batch_execute_statement(config_overrides={"retry_max_attempts": 1})
```
