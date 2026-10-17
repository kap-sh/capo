# capo-ec2-instance-connect: typed, async Python SDK for AWS EC2 Instance Connect

`capo-ec2-instance-connect` is a typed Python SDK for AWS EC2 Instance Connect. It has an async client, `AsyncEC2InstanceConnectClient`, for asyncio and trio, and a sync client, `EC2InstanceConnectClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/ec2-instance-connect/](https://capo-sdk.dev/services/ec2-instance-connect/)

## Installation

```
pip install capo-ec2-instance-connect
```

## Usage

```python
from capo_ec2_instance_connect import AsyncEC2InstanceConnectClient


async def main():
    async with AsyncEC2InstanceConnectClient() as ec2_instance_connect:
        # Example: call the send_serial_console_ssh_public_key operation
        response = await ec2_instance_connect.send_serial_console_ssh_public_key()
        print(response["request_id"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_ec2_instance_connect import AsyncEC2InstanceConnectClient
from capo_ec2_instance_connect.error import AuthException


async def main():
    async with AsyncEC2InstanceConnectClient() as ec2_instance_connect:
        try:
            await ec2_instance_connect.send_serial_console_ssh_public_key()
        except AuthException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_ec2_instance_connect import AsyncEC2InstanceConnectClient


async def main():
    async with AsyncEC2InstanceConnectClient() as ec2_instance_connect:
        # Default: 3 attempts for every operation
        response = await ec2_instance_connect.send_serial_console_ssh_public_key()

        # Override per operation
        response = await ec2_instance_connect.send_serial_console_ssh_public_key(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await ec2_instance_connect.send_serial_console_ssh_public_key(config_overrides={"retry_max_attempts": 1})
```
