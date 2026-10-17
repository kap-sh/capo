# capo-rekognition: typed, async Python SDK for AWS Rekognition

`capo-rekognition` is a typed Python SDK for AWS Rekognition. It has an async client, `AsyncRekognitionClient`, for asyncio and trio, and a sync client, `RekognitionClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/rekognition/](https://capo-sdk.dev/services/rekognition/)

## Installation

```
pip install capo-rekognition
```

## Usage

```python
from capo_rekognition import AsyncRekognitionClient


async def main():
    async with AsyncRekognitionClient() as rekognition:
        # Example: call the associate_faces operation
        response = await rekognition.associate_faces()
        print(response["associated_faces"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_rekognition import AsyncRekognitionClient


async def main():
    async with AsyncRekognitionClient() as rekognition:
        # Example: paginate over describe_projects
        async for item in rekognition.iter_describe_projects():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_rekognition import AsyncRekognitionClient
from capo_rekognition.error import AccessDeniedException


async def main():
    async with AsyncRekognitionClient() as rekognition:
        try:
            await rekognition.associate_faces()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_rekognition import AsyncRekognitionClient


async def main():
    async with AsyncRekognitionClient() as rekognition:
        # Default: 3 attempts for every operation
        response = await rekognition.associate_faces()

        # Override per operation
        response = await rekognition.associate_faces(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await rekognition.associate_faces(config_overrides={"retry_max_attempts": 1})
```
