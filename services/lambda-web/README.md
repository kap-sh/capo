# Getting Started

## Installation

```
pip install capo-lambda-web
```

## Usage

```python
from capo_lambda_web import AsyncLambdaWebClient


async def main():
    async with AsyncLambdaWebClient() as lambda_web:
        # Example: call the get_web_account_settings operation
        response = await lambda_web.get_web_account_settings()
        print(response["account_quotas"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_lambda_web import AsyncLambdaWebClient
from capo_lambda_web.error import AccessDeniedException


async def main():
    async with AsyncLambdaWebClient() as lambda_web:
        try:
            await lambda_web.get_web_account_settings()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_lambda_web import AsyncLambdaWebClient


async def main():
    async with AsyncLambdaWebClient() as lambda_web:
        # Default: 3 attempts for every operation
        response = await lambda_web.get_web_account_settings()

        # Override per operation
        response = await lambda_web.get_web_account_settings(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await lambda_web.get_web_account_settings(config_overrides={"retry_max_attempts": 1})
```
