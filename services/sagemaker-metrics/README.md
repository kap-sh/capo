# capo-sagemaker-metrics: typed, async Python SDK for AWS Sagemaker Metrics

`capo-sagemaker-metrics` is a typed Python SDK for AWS Sagemaker Metrics. It has an async client, `AsyncSageMakerMetricsClient`, for asyncio and trio, and a sync client, `SageMakerMetricsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/sagemaker-metrics/](https://capo-sdk.dev/services/sagemaker-metrics/)

## Installation

```
pip install capo-sagemaker-metrics
```

## Usage

```python
from capo_sagemaker_metrics import AsyncSageMakerMetricsClient


async def main():
    async with AsyncSageMakerMetricsClient() as sage_maker_metrics:
        # Example: call the batch_get_metrics operation
        response = await sage_maker_metrics.batch_get_metrics()
        print(response["metric_query_results"])
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sagemaker_metrics import AsyncSageMakerMetricsClient


async def main():
    async with AsyncSageMakerMetricsClient() as sage_maker_metrics:
        # Default: 3 attempts for every operation
        response = await sage_maker_metrics.batch_get_metrics()

        # Override per operation
        response = await sage_maker_metrics.batch_get_metrics(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await sage_maker_metrics.batch_get_metrics(config_overrides={"retry_max_attempts": 1})
```
