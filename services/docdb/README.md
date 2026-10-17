# capo-docdb: typed, async Python SDK for AWS Docdb

`capo-docdb` is a typed Python SDK for AWS Docdb. It has an async client, `AsyncDocDBClient`, for asyncio and trio, and a sync client, `DocDBClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/docdb/](https://capo-sdk.dev/services/docdb/)

## Installation

```
pip install capo-docdb
```

## Usage

```python
from capo_docdb import AsyncDocDBClient


async def main():
    async with AsyncDocDBClient() as doc_db:
        # Example: call the add_source_identifier_to_subscription operation
        response = await doc_db.add_source_identifier_to_subscription()
        print(response["event_subscription"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_docdb import AsyncDocDBClient


async def main():
    async with AsyncDocDBClient() as doc_db:
        # Example: paginate over describe_certificates
        async for item in doc_db.iter_describe_certificates():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_docdb import AsyncDocDBClient
from capo_docdb.error import SourceNotFoundFault


async def main():
    async with AsyncDocDBClient() as doc_db:
        try:
            await doc_db.add_source_identifier_to_subscription()
        except SourceNotFoundFault as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_docdb import AsyncDocDBClient


async def main():
    async with AsyncDocDBClient() as doc_db:
        # Default: 3 attempts for every operation
        response = await doc_db.add_source_identifier_to_subscription()

        # Override per operation
        response = await doc_db.add_source_identifier_to_subscription(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await doc_db.add_source_identifier_to_subscription(config_overrides={"retry_max_attempts": 1})
```
