# capo-application-signals: typed, async Python SDK for AWS Application Signals

`capo-application-signals` is a typed Python SDK for AWS Application Signals. It has an async client, `AsyncApplicationSignalsClient`, for asyncio and trio, and a sync client, `ApplicationSignalsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/application-signals/](https://capo-sdk.dev/services/application-signals/)

## Installation

```
pip install capo-application-signals
```

## Usage

```python
from capo_application_signals import AsyncApplicationSignalsClient


async def main():
    async with AsyncApplicationSignalsClient() as application_signals:
        # Example: call the batch_delete_instrumentation_configurations operation
        response = await application_signals.batch_delete_instrumentation_configurations()
        print(response["deleted_count"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_application_signals import AsyncApplicationSignalsClient


async def main():
    async with AsyncApplicationSignalsClient() as application_signals:
        # Example: paginate over get_instrumentation_configuration_status
        async for item in application_signals.iter_get_instrumentation_configuration_status():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_application_signals import AsyncApplicationSignalsClient
from capo_application_signals.error import ThrottlingException


async def main():
    async with AsyncApplicationSignalsClient() as application_signals:
        try:
            await application_signals.batch_delete_instrumentation_configurations()
        except ThrottlingException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_application_signals import AsyncApplicationSignalsClient


async def main():
    async with AsyncApplicationSignalsClient() as application_signals:
        # Default: 3 attempts for every operation
        response = await application_signals.batch_delete_instrumentation_configurations()

        # Override per operation
        response = await application_signals.batch_delete_instrumentation_configurations(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await application_signals.batch_delete_instrumentation_configurations(config_overrides={"retry_max_attempts": 1})
```
