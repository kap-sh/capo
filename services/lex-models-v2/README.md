# capo-lex-models-v2: typed, async Python SDK for AWS Lex Models V2

`capo-lex-models-v2` is a typed Python SDK for AWS Lex Models V2. It has an async client, `AsyncLexModelsV2Client`, for asyncio and trio, and a sync client, `LexModelsV2Client`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/lex-models-v2/](https://capo-sdk.dev/services/lex-models-v2/)

## Installation

```
pip install capo-lex-models-v2
```

## Usage

```python
from capo_lex_models_v2 import AsyncLexModelsV2Client


async def main():
    async with AsyncLexModelsV2Client() as lex_models_v2:
        # Example: call the batch_create_custom_vocabulary_item operation
        response = await lex_models_v2.batch_create_custom_vocabulary_item()
        print(response["bot_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_lex_models_v2 import AsyncLexModelsV2Client


async def main():
    async with AsyncLexModelsV2Client() as lex_models_v2:
        # Example: paginate over describe_bot_analyzer_recommendation
        async for item in lex_models_v2.iter_describe_bot_analyzer_recommendation():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_lex_models_v2 import AsyncLexModelsV2Client
from capo_lex_models_v2.error import InternalServerException


async def main():
    async with AsyncLexModelsV2Client() as lex_models_v2:
        try:
            await lex_models_v2.batch_create_custom_vocabulary_item()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_lex_models_v2 import AsyncLexModelsV2Client


async def main():
    async with AsyncLexModelsV2Client() as lex_models_v2:
        # Default: 3 attempts for every operation
        response = await lex_models_v2.batch_create_custom_vocabulary_item()

        # Override per operation
        response = await lex_models_v2.batch_create_custom_vocabulary_item(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await lex_models_v2.batch_create_custom_vocabulary_item(config_overrides={"retry_max_attempts": 1})
```
