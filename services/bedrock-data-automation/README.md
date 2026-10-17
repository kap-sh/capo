# capo-bedrock-data-automation: typed, async Python SDK for AWS Bedrock Data Automation

`capo-bedrock-data-automation` is a typed Python SDK for AWS Bedrock Data Automation. It has an async client, `AsyncBedrockDataAutomationClient`, for asyncio and trio, and a sync client, `BedrockDataAutomationClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/bedrock-data-automation/](https://capo-sdk.dev/services/bedrock-data-automation/)

## Installation

```
pip install capo-bedrock-data-automation
```

## Usage

```python
from capo_bedrock_data_automation import AsyncBedrockDataAutomationClient


async def main():
    async with AsyncBedrockDataAutomationClient() as bedrock_data_automation:
        # Example: call the copy_blueprint_stage operation
        response = await bedrock_data_automation.copy_blueprint_stage()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_bedrock_data_automation import AsyncBedrockDataAutomationClient


async def main():
    async with AsyncBedrockDataAutomationClient() as bedrock_data_automation:
        # Example: paginate over list_data_automation_library_entities
        async for item in bedrock_data_automation.iter_list_data_automation_library_entities():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_bedrock_data_automation import AsyncBedrockDataAutomationClient
from capo_bedrock_data_automation.error import AccessDeniedException


async def main():
    async with AsyncBedrockDataAutomationClient() as bedrock_data_automation:
        try:
            await bedrock_data_automation.copy_blueprint_stage()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_bedrock_data_automation import AsyncBedrockDataAutomationClient


async def main():
    async with AsyncBedrockDataAutomationClient() as bedrock_data_automation:
        # Default: 3 attempts for every operation
        response = await bedrock_data_automation.copy_blueprint_stage()

        # Override per operation
        response = await bedrock_data_automation.copy_blueprint_stage(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await bedrock_data_automation.copy_blueprint_stage(config_overrides={"retry_max_attempts": 1})
```
