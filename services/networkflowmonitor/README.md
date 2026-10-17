# capo-networkflowmonitor: typed, async Python SDK for AWS Networkflowmonitor

`capo-networkflowmonitor` is a typed Python SDK for AWS Networkflowmonitor. It has an async client, `AsyncNetworkFlowMonitorClient`, for asyncio and trio, and a sync client, `NetworkFlowMonitorClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/networkflowmonitor/](https://capo-sdk.dev/services/networkflowmonitor/)

## Installation

```
pip install capo-networkflowmonitor
```

## Usage

```python
from capo_networkflowmonitor import AsyncNetworkFlowMonitorClient


async def main():
    async with AsyncNetworkFlowMonitorClient() as network_flow_monitor:
        # Example: call the list_tags_for_resource operation
        response = await network_flow_monitor.list_tags_for_resource()
        print(response["tags"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_networkflowmonitor import AsyncNetworkFlowMonitorClient


async def main():
    async with AsyncNetworkFlowMonitorClient() as network_flow_monitor:
        # Example: paginate over list_monitors
        async for item in network_flow_monitor.iter_list_monitors():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_networkflowmonitor import AsyncNetworkFlowMonitorClient
from capo_networkflowmonitor.error import AccessDeniedException


async def main():
    async with AsyncNetworkFlowMonitorClient() as network_flow_monitor:
        try:
            await network_flow_monitor.list_tags_for_resource()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_networkflowmonitor import AsyncNetworkFlowMonitorClient


async def main():
    async with AsyncNetworkFlowMonitorClient() as network_flow_monitor:
        # Default: 3 attempts for every operation
        response = await network_flow_monitor.list_tags_for_resource()

        # Override per operation
        response = await network_flow_monitor.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await network_flow_monitor.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
