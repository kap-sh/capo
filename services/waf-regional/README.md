# capo-waf-regional: typed, async Python SDK for AWS WAF Regional

`capo-waf-regional` is a typed Python SDK for AWS WAF Regional. It has an async client, `AsyncWAFRegionalClient`, for asyncio and trio, and a sync client, `WAFRegionalClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/waf-regional/](https://capo-sdk.dev/services/waf-regional/)

## Installation

```
pip install capo-waf-regional
```

## Usage

```python
from capo_waf_regional import AsyncWAFRegionalClient


async def main():
    async with AsyncWAFRegionalClient() as waf_regional:
        # Example: call the associate_web_acl operation
        response = await waf_regional.associate_web_acl()
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_waf_regional import AsyncWAFRegionalClient
from capo_waf_regional.error import WAFInternalErrorException


async def main():
    async with AsyncWAFRegionalClient() as waf_regional:
        try:
            await waf_regional.associate_web_acl()
        except WAFInternalErrorException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_waf_regional import AsyncWAFRegionalClient


async def main():
    async with AsyncWAFRegionalClient() as waf_regional:
        # Default: 3 attempts for every operation
        response = await waf_regional.associate_web_acl()

        # Override per operation
        response = await waf_regional.associate_web_acl(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await waf_regional.associate_web_acl(config_overrides={"retry_max_attempts": 1})
```
