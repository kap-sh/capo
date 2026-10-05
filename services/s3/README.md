# Getting Started

## Installation

```
pip install capo-s3
```

## Usage

```python
from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Upload an object
        await s3.put_object("my-bucket", "hello.txt", body=b"Hello, World!")

        # Download it
        async with s3.get_object("my-bucket", "hello.txt") as response:
            async for chunk in response["body"]:
                print(chunk)
```

```python
from capo_s3 import S3Client


def main():
    with S3Client() as s3:
        # The sync client: the same methods, without async and await
        s3.put_object("my-bucket", "hello.txt", body=b"Hello, World!")

        with s3.get_object("my-bucket", "hello.txt") as response:
            for chunk in response["body"]:
                print(chunk)
```

## RustFS

```python
from capo_s3 import AsyncS3Client, Credentials


async def main():
    async with AsyncS3Client(
        region="us-east-1",
        endpoint="http://localhost:9000",
        credentials=Credentials(access_key="<your-access-key>", secret_key="<your-secret-key>"),
        # RustFS wants the bucket in the path, not in the host name
        force_path_style=True,
    ) as s3:
        # The same client, talking to RustFS
        await s3.create_bucket("my-bucket")
        await s3.put_object("my-bucket", "hello.txt", body=b"Hello, RustFS!")
```

## Objects

```python
from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Upload with a content type and your own metadata
        await s3.put_object(
            "my-bucket",
            "report.json",
            body=b'{"total": 3}',
            content_type="application/json",
            metadata={"author": "me"},
        )

        # Size, type and metadata, without downloading the object
        head = await s3.head_object("my-bucket", "report.json")
        print(head.get("content_length"), head.get("content_type"), head.get("metadata"))

        # Copy an object, here into another bucket
        await s3.copy_object(bucket="other-bucket", key="report.json", copy_source="my-bucket/report.json")

        # Delete one object
        await s3.delete_object("my-bucket", "report.json")

        # Delete many in one request
        await s3.delete_objects("my-bucket", {"objects": [{"key": "a.txt"}, {"key": "b.txt"}]})
```

## Buckets

```python
from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Create a bucket; outside us-east-1 it has to name its region
        await s3.create_bucket(
            "my-bucket",
            create_bucket_configuration={"location_constraint": "eu-central-1"},
        )

        # Check that a bucket exists and that you may use it
        await s3.head_bucket("my-bucket")

        # Delete a bucket, which has to be empty
        await s3.delete_bucket("my-bucket")
```

## Uploading and Downloading Files

```python
from capo_s3 import AsyncS3Client, AsyncTransferManager


async def main():
    async with AsyncS3Client() as s3:
        manager = AsyncTransferManager(
            s3,
            # A file of 16 MiB or more goes up as a multipart upload, in parts of 8 MiB.
            # S3 needs every part but the last to be at least 5 MiB
            target_part_size_bytes=8 * 1024 * 1024,
            multipart_upload_threshold_bytes=16 * 1024 * 1024,
            # Download the parts the object was uploaded in; "range" downloads
            # byte ranges of target_part_size_bytes instead
            multipart_download_type="part",
        )

        # Upload a file
        await manager.upload("video.mp4", "my-bucket", "video.mp4")

        # Download it into another file
        await manager.download("my-bucket", "video.mp4", "copy.mp4")
```

```python
from capo_s3 import AsyncS3Client, AsyncTransferManager


async def main():
    async with AsyncS3Client() as s3:
        manager = AsyncTransferManager(
            s3,
            target_part_size_bytes=8 * 1024 * 1024,
            multipart_upload_threshold_bytes=16 * 1024 * 1024,
            multipart_download_type="part",
        )

        # upload takes the keywords of put_object
        await manager.upload(
            "video.mp4",
            "my-bucket",
            "video.mp4",
            content_type="video/mp4",
            checksum_algorithm="CRC32",
        )

        # download takes the keywords of get_object
        await manager.download("my-bucket", "video.mp4", "copy.mp4", version_id="3HL4kqtJlcpXroDTDmJ")

        # Bigger parts, for this upload only
        await manager.upload(
            "video.mp4",
            "my-bucket",
            "video.mp4",
            transfer_config_overrides={"target_part_size_bytes": 64 * 1024 * 1024},
        )

        # Byte ranges, for this download only
        await manager.download(
            "my-bucket",
            "video.mp4",
            "copy.mp4",
            transfer_config_overrides={"multipart_download_type": "range"},
        )
```

```python
from capo_s3 import AsyncS3Client, AsyncTransferManager


async def main():
    async with AsyncS3Client() as s3:
        manager = AsyncTransferManager(
            s3,
            target_part_size_bytes=8 * 1024 * 1024,
            multipart_upload_threshold_bytes=16 * 1024 * 1024,
            multipart_download_type="part",
        )

        # Upload with progress. Leaving the block before everything is sent,
        # or with an error, aborts the multipart upload
        async with manager.upload_iter("video.mp4", "my-bucket", "video.mp4") as upload:
            async for event in upload:
                print(f"{event.transferred_bytes} of {event.total_bytes} bytes sent")

        # Download into memory, with progress: each event has its data
        # and the offset it belongs at
        data = bytearray()
        async for event in manager.download_iter("my-bucket", "video.mp4"):
            data[event.offset : event.offset + len(event.data)] = event.data
            print(f"{event.transferred_bytes} of {event.total_bytes} bytes received")
```

```python
from capo_s3 import S3Client, TransferManager


def main():
    with S3Client() as s3:
        # TransferManager does the same for the sync client
        manager = TransferManager(
            s3,
            target_part_size_bytes=8 * 1024 * 1024,
            multipart_upload_threshold_bytes=16 * 1024 * 1024,
            multipart_download_type="part",
        )

        manager.upload("video.mp4", "my-bucket", "video.mp4")
        manager.download("my-bucket", "video.mp4", "copy.mp4")
```

## Pagination

```python
from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Every bucket, however many pages that takes
        async for bucket in s3.iter_list_buckets():
            print(bucket.get("name"))

        # Every object under a prefix, a page at a time
        async for page in s3.iter_list_objects_v2("my-bucket", prefix="photos/"):
            for obj in page.get("contents", []):
                print(obj.get("key"), obj.get("size"))

        # The "folders" right under a prefix
        async for page in s3.iter_list_objects_v2("my-bucket", prefix="photos/", delimiter="/"):
            for folder in page.get("common_prefixes", []):
                print(folder.get("prefix"))

        # A single page, without the iterator
        page = await s3.list_objects_v2("my-bucket", max_keys=10)
        print(page.get("key_count"), page.get("is_truncated"))
```

## Streaming Bodies

```python
from capo_s3 import AsyncS3Client, Body


async def main():
    async with AsyncS3Client() as s3:
        # A file from disk: its length is read from the file, and it is opened
        # again on every retry. Body.from_path does the same for S3Client
        await s3.put_object("my-bucket", "hello.txt", body=Body.async_from_path("hello.txt"))

        # Your own chunks, with their total length. They can be sent only once,
        # so a request that fails after its body went out is not retried
        async def chunks():
            yield b"Hello, "
            yield b"World!"

        await s3.put_object("my-bucket", "hello.txt", body=chunks(), content_length=13)
```

```python
from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Read the whole object into memory
        async with s3.get_object("my-bucket", "hello.txt") as response:
            data = b"".join([chunk async for chunk in response["body"]])
        print(data)

        # Only its first hundred bytes
        async with s3.get_object("my-bucket", "hello.txt", range="bytes=0-99") as response:
            data = b"".join([chunk async for chunk in response["body"]])
        print(data)
```

## Waiters

```python
from capo_s3 import AsyncS3Client
from capo_s3.errors import WaiterTimeoutError


async def main():
    async with AsyncS3Client() as s3:
        # Create a bucket and wait until it is there
        await s3.create_bucket("my-bucket")
        await s3.wait_until_bucket_exists("my-bucket", max_wait_time=60)

        # Delete an object and wait until it is gone
        await s3.delete_object("my-bucket", "hello.txt")
        await s3.wait_until_object_not_exists("my-bucket", "hello.txt", max_wait_time=60)

        # After max_wait_time seconds the waiter gives up
        try:
            await s3.wait_until_object_exists("my-bucket", "hello.txt", max_wait_time=10)
        except WaiterTimeoutError:
            print("still not there")
```

## Presigned URLs

```python
from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Whoever has this URL can download the object, without credentials,
        # for the next ten minutes
        url = await s3.presigned_get_object("my-bucket", "hello.txt", expire_in=600)
        print(url)

        # The same, saved by the browser under another name
        url = await s3.presigned_get_object(
            "my-bucket",
            "hello.txt",
            expire_in=600,
            response_content_disposition='attachment; filename="greeting.txt"',
        )
        print(url)

        # A URL to upload to: PUT the bytes to it
        url = await s3.presigned_put_object("my-bucket", "upload.txt", expire_in=600)
        print(url)
```

## Error Handling

```python
from capo_s3 import AsyncS3Client
from capo_s3.errors import NoSuchKey, NotFound, ServiceError


async def main():
    async with AsyncS3Client() as s3:
        # An error the API describes has its own class
        try:
            async with s3.get_object("my-bucket", "missing.txt") as response:
                print(response.get("content_length"))
        except NoSuchKey as e:
            print(e.code, e.message)

        # Is the object there? head_object raises NotFound when it is not
        try:
            await s3.head_object("my-bucket", "missing.txt")
        except NotFound:
            print("no such object")

        # Any error S3 returns; one without a class of its own is an UnknownServiceError
        try:
            await s3.delete_bucket("my-bucket")
        except ServiceError as e:
            print(e.code, e.message)
```

## Retrying

```python
from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client(retry_max_attempts=5) as s3:
        # Throttling, server errors and network failures are retried. Every call
        # of this client gets five attempts instead of the default three
        await s3.head_object("my-bucket", "hello.txt")
```

```python
from capo_s3 import AsyncS3Client


async def main():
    async with AsyncS3Client() as s3:
        # Five attempts for this call
        await s3.head_object("my-bucket", "hello.txt", config_overrides={"retry_max_attempts": 5})

        # No retries for this call
        await s3.head_object("my-bucket", "hello.txt", config_overrides={"retry_max_attempts": 1})
```
