# Getting Started

## Installation

```
pip install capo-lambda-microvms
```

## Usage

```python
from capo_lambda_microvms import AsyncLambdaMicrovmsClient


async def main():
    async with AsyncLambdaMicrovmsClient() as lambda_microvms:
        # Example: call the create_microvm_image operation
        response = await lambda_microvms.create_microvm_image()
        print(response["image_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_lambda_microvms import AsyncLambdaMicrovmsClient


async def main():
    async with AsyncLambdaMicrovmsClient() as lambda_microvms:
        # Example: paginate over list_managed_microvm_images
        async for item in lambda_microvms.iter_list_managed_microvm_images():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_lambda_microvms import AsyncLambdaMicrovmsClient
from capo_lambda_microvms.error import AccessDeniedException


async def main():
    async with AsyncLambdaMicrovmsClient() as lambda_microvms:
        try:
            await lambda_microvms.create_microvm_image()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_lambda_microvms import AsyncLambdaMicrovmsClient


async def main():
    async with AsyncLambdaMicrovmsClient() as lambda_microvms:
        # Default: 3 attempts for every operation
        response = await lambda_microvms.create_microvm_image()

        # Override per operation
        response = await lambda_microvms.create_microvm_image(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await lambda_microvms.create_microvm_image(config_overrides={"retry_max_attempts": 1})
```
