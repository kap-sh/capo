# capo-connectcampaigns: typed, async Python SDK for AWS Connectcampaigns

`capo-connectcampaigns` is a typed Python SDK for AWS Connectcampaigns. It has an async client, `AsyncConnectCampaignsClient`, for asyncio and trio, and a sync client, `ConnectCampaignsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/connectcampaigns/](https://capo-sdk.dev/services/connectcampaigns/)

## Installation

```
pip install capo-connectcampaigns
```

## Usage

```python
from capo_connectcampaigns import AsyncConnectCampaignsClient


async def main():
    async with AsyncConnectCampaignsClient() as connect_campaigns:
        # Example: call the create_campaign operation
        response = await connect_campaigns.create_campaign()
        print(response["id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_connectcampaigns import AsyncConnectCampaignsClient


async def main():
    async with AsyncConnectCampaignsClient() as connect_campaigns:
        # Example: paginate over list_campaigns
        async for item in connect_campaigns.iter_list_campaigns():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_connectcampaigns import AsyncConnectCampaignsClient
from capo_connectcampaigns.error import AccessDeniedException


async def main():
    async with AsyncConnectCampaignsClient() as connect_campaigns:
        try:
            await connect_campaigns.create_campaign()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_connectcampaigns import AsyncConnectCampaignsClient


async def main():
    async with AsyncConnectCampaignsClient() as connect_campaigns:
        # Default: 3 attempts for every operation
        response = await connect_campaigns.create_campaign()

        # Override per operation
        response = await connect_campaigns.create_campaign(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await connect_campaigns.create_campaign(config_overrides={"retry_max_attempts": 1})
```
