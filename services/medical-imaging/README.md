# capo-medical-imaging: typed, async Python SDK for AWS Medical Imaging

`capo-medical-imaging` is a typed Python SDK for AWS Medical Imaging. It has an async client, `AsyncMedicalImagingClient`, for asyncio and trio, and a sync client, `MedicalImagingClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/medical-imaging/](https://capo-sdk.dev/services/medical-imaging/)

## Installation

```
pip install capo-medical-imaging
```

## Usage

```python
from capo_medical_imaging import AsyncMedicalImagingClient


async def main():
    async with AsyncMedicalImagingClient() as medical_imaging:
        # Example: call the copy_image_set operation
        response = await medical_imaging.copy_image_set()
        print(response["datastore_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_medical_imaging import AsyncMedicalImagingClient


async def main():
    async with AsyncMedicalImagingClient() as medical_imaging:
        # Example: paginate over list_dicom_import_jobs
        async for item in medical_imaging.iter_list_dicom_import_jobs():
            print(item)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_medical_imaging import AsyncMedicalImagingClient


async def main():
    async with AsyncMedicalImagingClient() as medical_imaging:
        # Example: call get_image_frame and read the streaming response
        async with medical_imaging.get_image_frame() as response:
            async for chunk in response["image_frame_blob"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_medical_imaging import AsyncMedicalImagingClient
from capo_medical_imaging.error import AccessDeniedException


async def main():
    async with AsyncMedicalImagingClient() as medical_imaging:
        try:
            await medical_imaging.copy_image_set()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_medical_imaging import AsyncMedicalImagingClient


async def main():
    async with AsyncMedicalImagingClient() as medical_imaging:
        # Default: 3 attempts for every operation
        response = await medical_imaging.copy_image_set()

        # Override per operation
        response = await medical_imaging.copy_image_set(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await medical_imaging.copy_image_set(config_overrides={"retry_max_attempts": 1})
```
