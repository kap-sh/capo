# capo-inspector-scan: typed, async Python SDK for AWS Inspector Scan

`capo-inspector-scan` is a typed Python SDK for AWS Inspector Scan. It has an async client, `AsyncInspectorScanClient`, for asyncio and trio, and a sync client, `InspectorScanClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/inspector-scan/](https://capo-sdk.dev/services/inspector-scan/)

## Installation

```
pip install capo-inspector-scan
```

## Usage

```python
from capo_inspector_scan import AsyncInspectorScanClient


async def main():
    async with AsyncInspectorScanClient() as inspector_scan:
        # Example: call the scan_sbom operation
        response = await inspector_scan.scan_sbom()
        print(response["sbom"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_inspector_scan import AsyncInspectorScanClient
from capo_inspector_scan.error import AccessDeniedException


async def main():
    async with AsyncInspectorScanClient() as inspector_scan:
        try:
            await inspector_scan.scan_sbom()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_inspector_scan import AsyncInspectorScanClient


async def main():
    async with AsyncInspectorScanClient() as inspector_scan:
        # Default: 3 attempts for every operation
        response = await inspector_scan.scan_sbom()

        # Override per operation
        response = await inspector_scan.scan_sbom(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await inspector_scan.scan_sbom(config_overrides={"retry_max_attempts": 1})
```
