# capo-invoicing: typed, async Python SDK for AWS Invoicing

`capo-invoicing` is a typed Python SDK for AWS Invoicing. It has an async client, `AsyncInvoicingClient`, for asyncio and trio, and a sync client, `InvoicingClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/invoicing/](https://capo-sdk.dev/services/invoicing/)

## Installation

```
pip install capo-invoicing
```

## Usage

```python
from capo_invoicing import AsyncInvoicingClient


async def main():
    async with AsyncInvoicingClient() as invoicing:
        # Example: call the batch_get_invoice_profile operation
        response = await invoicing.batch_get_invoice_profile()
        print(response["profiles"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_invoicing import AsyncInvoicingClient


async def main():
    async with AsyncInvoicingClient() as invoicing:
        # Example: paginate over list_invoice_summaries
        async for item in invoicing.iter_list_invoice_summaries():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_invoicing import AsyncInvoicingClient
from capo_invoicing.error import AccessDeniedException


async def main():
    async with AsyncInvoicingClient() as invoicing:
        try:
            await invoicing.batch_get_invoice_profile()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_invoicing import AsyncInvoicingClient


async def main():
    async with AsyncInvoicingClient() as invoicing:
        # Default: 3 attempts for every operation
        response = await invoicing.batch_get_invoice_profile()

        # Override per operation
        response = await invoicing.batch_get_invoice_profile(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await invoicing.batch_get_invoice_profile(config_overrides={"retry_max_attempts": 1})
```
