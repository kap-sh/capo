# capo-auditmanager: typed, async Python SDK for AWS Auditmanager

`capo-auditmanager` is a typed Python SDK for AWS Auditmanager. It has an async client, `AsyncAuditManagerClient`, for asyncio and trio, and a sync client, `AuditManagerClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/auditmanager/](https://capo-sdk.dev/services/auditmanager/)

## Installation

```
pip install capo-auditmanager
```

## Usage

```python
from capo_auditmanager import AsyncAuditManagerClient


async def main():
    async with AsyncAuditManagerClient() as audit_manager:
        # Example: call the associate_assessment_report_evidence_folder operation
        response = await audit_manager.associate_assessment_report_evidence_folder()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_auditmanager import AsyncAuditManagerClient


async def main():
    async with AsyncAuditManagerClient() as audit_manager:
        # Example: paginate over get_change_logs
        async for item in audit_manager.iter_get_change_logs():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_auditmanager import AsyncAuditManagerClient
from capo_auditmanager.error import AccessDeniedException


async def main():
    async with AsyncAuditManagerClient() as audit_manager:
        try:
            await audit_manager.associate_assessment_report_evidence_folder()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_auditmanager import AsyncAuditManagerClient


async def main():
    async with AsyncAuditManagerClient() as audit_manager:
        # Default: 3 attempts for every operation
        response = await audit_manager.associate_assessment_report_evidence_folder()

        # Override per operation
        response = await audit_manager.associate_assessment_report_evidence_folder(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await audit_manager.associate_assessment_report_evidence_folder(config_overrides={"retry_max_attempts": 1})
```
