# capo-sagemaker-featurestore-runtime: typed, async Python SDK for AWS Sagemaker Featurestore Runtime

`capo-sagemaker-featurestore-runtime` is a typed Python SDK for AWS Sagemaker Featurestore Runtime. It has an async client, `AsyncSageMakerFeatureStoreRuntimeClient`, for asyncio and trio, and a sync client, `SageMakerFeatureStoreRuntimeClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/sagemaker-featurestore-runtime/](https://capo-sdk.dev/services/sagemaker-featurestore-runtime/)

## Installation

```
pip install capo-sagemaker-featurestore-runtime
```

## Usage

```python
from capo_sagemaker_featurestore_runtime import AsyncSageMakerFeatureStoreRuntimeClient


async def main():
    async with AsyncSageMakerFeatureStoreRuntimeClient() as sage_maker_feature_store_runtime:
        # Example: call the batch_get_record operation
        response = await sage_maker_feature_store_runtime.batch_get_record()
        print(response["records"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_sagemaker_featurestore_runtime import AsyncSageMakerFeatureStoreRuntimeClient


async def main():
    async with AsyncSageMakerFeatureStoreRuntimeClient() as sage_maker_feature_store_runtime:
        # Example: paginate over list_records
        async for item in sage_maker_feature_store_runtime.iter_list_records():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sagemaker_featurestore_runtime import AsyncSageMakerFeatureStoreRuntimeClient
from capo_sagemaker_featurestore_runtime.error import AccessForbidden


async def main():
    async with AsyncSageMakerFeatureStoreRuntimeClient() as sage_maker_feature_store_runtime:
        try:
            await sage_maker_feature_store_runtime.batch_get_record()
        except AccessForbidden as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sagemaker_featurestore_runtime import AsyncSageMakerFeatureStoreRuntimeClient


async def main():
    async with AsyncSageMakerFeatureStoreRuntimeClient() as sage_maker_feature_store_runtime:
        # Default: 3 attempts for every operation
        response = await sage_maker_feature_store_runtime.batch_get_record()

        # Override per operation
        response = await sage_maker_feature_store_runtime.batch_get_record(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await sage_maker_feature_store_runtime.batch_get_record(config_overrides={"retry_max_attempts": 1})
```
