"""Core S3 operations against RustFS (free) and AWS (paid).

Every class runs once per backend and, for the async source, once per anyio
backend; ``ry`` generates the sync twins.
"""

from __future__ import annotations

import gzip
import itertools
import json
import os
import sys
import time

import anyio
import pytest
from capo_s3 import AsyncS3Client, Credentials, S3Client
from capo_s3.errors import (
    BucketAlreadyOwnedByYou,
    NoSuchBucket,
    NoSuchKey,
    NoSuchUpload,
    NotFound,
    ServiceError,
    UnknownServiceError,
)
from capo_s3.types.checksum_algorithm import ChecksumAlgorithm
from zapros import AsyncClient, Client

from tests.conftest import (
    AWS_REGION,
    agather,
    aread_body,
    crc32_b64,
    create_bucket_kwargs,
    gather,
    make_async_s3_client,
    make_s3_client,
    read_body,
    unique_name,
)

DATA = b"hello capo " * 100
MiB = 1024 * 1024
CHECKSUM_ALGORITHMS = ["CRC32", "CRC32C", "SHA1", "SHA256", "CRC64NVME"]


# ---------------------------------------------------------------------------
# buckets
# ---------------------------------------------------------------------------


class TestAsyncBuckets:  # unasync: generate
    async def test_head_list_and_location(self, async_s3: AsyncS3Client, bucket: str, s3_backend: str):
        await async_s3.head_bucket(bucket)
        assert bucket in [b["name"] for b in (await async_s3.list_buckets()).get("buckets", [])]
        assert bucket in [b["name"] async for b in async_s3.iter_list_buckets()]
        location = await async_s3.get_bucket_location(bucket)
        if s3_backend == "aws":
            assert location.get("location_constraint") == AWS_REGION

    async def test_wait_until_bucket_exists(self, async_s3: AsyncS3Client, bucket: str):
        await async_s3.wait_until_bucket_exists(bucket, max_wait_time=30)

    async def test_duplicate_create_raises(self, async_s3: AsyncS3Client, bucket: str, s3_backend: str):
        if s3_backend == "rustfs":
            pytest.skip("RustFS treats a duplicate create_bucket as idempotent")
        with pytest.raises(BucketAlreadyOwnedByYou):
            await async_s3.create_bucket(bucket, **create_bucket_kwargs(s3_backend))

    async def test_head_missing_bucket_raises_not_found(self, async_s3: AsyncS3Client):
        with pytest.raises(NotFound):
            await async_s3.head_bucket(unique_name("capotest-missing"))

    async def test_tagging_roundtrip(self, async_s3: AsyncS3Client, bucket: str):
        await async_s3.put_bucket_tagging(bucket, tagging={"tag_set": [{"key": "purpose", "value": "capo-test"}]})
        assert (await async_s3.get_bucket_tagging(bucket))["tag_set"] == [{"key": "purpose", "value": "capo-test"}]
        await async_s3.delete_bucket_tagging(bucket)

    async def test_policy_roundtrip(self, async_s3: AsyncS3Client, bucket: str):
        # A Deny-only policy is not "public", so AWS accepts it under the default public access block.
        policy = json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Deny",
                        "Principal": "*",
                        "Action": "s3:PutObject",
                        "Resource": f"arn:aws:s3:::{bucket}/private/*",
                    }
                ],
            }
        )
        await async_s3.put_bucket_policy(bucket, policy=policy)
        assert "Deny" in (await async_s3.get_bucket_policy(bucket))["policy"]
        await async_s3.delete_bucket_policy(bucket)
        with pytest.raises(ServiceError) as info:
            await async_s3.get_bucket_policy(bucket)
        assert info.value.code == "NoSuchBucketPolicy"

    async def test_versioning(self, async_s3: AsyncS3Client, bucket: str):
        await async_s3.put_bucket_versioning(bucket, versioning_configuration={"status": "Enabled"})
        for _ in range(10):  # AWS applies it asynchronously
            if (await async_s3.get_bucket_versioning(bucket)).get("status") == "Enabled":
                break
            await anyio.sleep(1)
        else:
            pytest.fail("versioning did not become Enabled")
        await async_s3.put_object(bucket, "ver.txt", body=b"v1")
        await async_s3.put_object(bucket, "ver.txt", body=b"v2")
        versions = (await async_s3.list_object_versions(bucket, prefix="ver.txt")).get("versions", [])
        assert len(versions) == 2
        old = next(v for v in versions if not v["is_latest"])
        assert await aread_body(async_s3.get_object(bucket, "ver.txt", version_id=old["version_id"])) == b"v1"
        assert await aread_body(async_s3.get_object(bucket, "ver.txt")) == b"v2"

    async def test_lifecycle_configuration(self, async_s3: AsyncS3Client, bucket: str):
        await async_s3.put_bucket_lifecycle_configuration(
            bucket,
            lifecycle_configuration={
                "rules": [
                    {"id": "expire", "status": "Enabled", "filter": {"prefix": "tmp/"}, "expiration": {"days": 1}},
                    {
                        "id": "abort-mpu",
                        "status": "Enabled",
                        "filter": {"prefix": "mpu/"},
                        "expiration": {"days": 2},
                        "abort_incomplete_multipart_upload": {"days_after_initiation": 1},
                    },
                ]
            },
        )
        got = (await async_s3.get_bucket_lifecycle_configuration(bucket)).get("rules", [])
        assert sorted(r["id"] for r in got) == ["abort-mpu", "expire"]
        abort = next(r for r in got if r["id"] == "abort-mpu")
        assert abort["abort_incomplete_multipart_upload"]["days_after_initiation"] == 1

    async def test_cors_roundtrip(self, async_s3: AsyncS3Client, bucket: str):
        await async_s3.put_bucket_cors(
            bucket, cors_configuration={"cors_rules": [{"allowed_methods": ["GET"], "allowed_origins": ["*"]}]}
        )
        assert (await async_s3.get_bucket_cors(bucket))["cors_rules"][0]["allowed_methods"] == ["GET"]
        await async_s3.delete_bucket_cors(bucket)

    async def test_read_only_configuration(self, async_s3: AsyncS3Client, bucket: str):
        assert "owner" in await async_s3.get_bucket_acl(bucket)
        await async_s3.get_bucket_notification_configuration(bucket)

class TestBuckets:  # unasync: generated
    def test_head_list_and_location(self, s3: S3Client, bucket: str, s3_backend: str):
        s3.head_bucket(bucket)
        assert bucket in [b["name"] for b in (s3.list_buckets()).get("buckets", [])]
        assert bucket in [b["name"] for b in s3.iter_list_buckets()]
        location = s3.get_bucket_location(bucket)
        if s3_backend == "aws":
            assert location.get("location_constraint") == AWS_REGION

    def test_wait_until_bucket_exists(self, s3: S3Client, bucket: str):
        s3.wait_until_bucket_exists(bucket, max_wait_time=30)

    def test_duplicate_create_raises(self, s3: S3Client, bucket: str, s3_backend: str):
        if s3_backend == "rustfs":
            pytest.skip("RustFS treats a duplicate create_bucket as idempotent")
        with pytest.raises(BucketAlreadyOwnedByYou):
            s3.create_bucket(bucket, **create_bucket_kwargs(s3_backend))

    def test_head_missing_bucket_raises_not_found(self, s3: S3Client):
        with pytest.raises(NotFound):
            s3.head_bucket(unique_name("capotest-missing"))

    def test_tagging_roundtrip(self, s3: S3Client, bucket: str):
        s3.put_bucket_tagging(bucket, tagging={"tag_set": [{"key": "purpose", "value": "capo-test"}]})
        assert (s3.get_bucket_tagging(bucket))["tag_set"] == [{"key": "purpose", "value": "capo-test"}]
        s3.delete_bucket_tagging(bucket)

    def test_policy_roundtrip(self, s3: S3Client, bucket: str):
        # A Deny-only policy is not "public", so AWS accepts it under the default public access block.
        policy = json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Deny",
                        "Principal": "*",
                        "Action": "s3:PutObject",
                        "Resource": f"arn:aws:s3:::{bucket}/private/*",
                    }
                ],
            }
        )
        s3.put_bucket_policy(bucket, policy=policy)
        assert "Deny" in (s3.get_bucket_policy(bucket))["policy"]
        s3.delete_bucket_policy(bucket)
        with pytest.raises(ServiceError) as info:
            s3.get_bucket_policy(bucket)
        assert info.value.code == "NoSuchBucketPolicy"

    def test_versioning(self, s3: S3Client, bucket: str):
        s3.put_bucket_versioning(bucket, versioning_configuration={"status": "Enabled"})
        for _ in range(10):  # AWS applies it asynchronously
            if (s3.get_bucket_versioning(bucket)).get("status") == "Enabled":
                break
            time.sleep(1)
        else:
            pytest.fail("versioning did not become Enabled")
        s3.put_object(bucket, "ver.txt", body=b"v1")
        s3.put_object(bucket, "ver.txt", body=b"v2")
        versions = (s3.list_object_versions(bucket, prefix="ver.txt")).get("versions", [])
        assert len(versions) == 2
        old = next(v for v in versions if not v["is_latest"])
        assert read_body(s3.get_object(bucket, "ver.txt", version_id=old["version_id"])) == b"v1"
        assert read_body(s3.get_object(bucket, "ver.txt")) == b"v2"

    def test_lifecycle_configuration(self, s3: S3Client, bucket: str):
        s3.put_bucket_lifecycle_configuration(
            bucket,
            lifecycle_configuration={
                "rules": [
                    {"id": "expire", "status": "Enabled", "filter": {"prefix": "tmp/"}, "expiration": {"days": 1}},
                    {
                        "id": "abort-mpu",
                        "status": "Enabled",
                        "filter": {"prefix": "mpu/"},
                        "expiration": {"days": 2},
                        "abort_incomplete_multipart_upload": {"days_after_initiation": 1},
                    },
                ]
            },
        )
        got = (s3.get_bucket_lifecycle_configuration(bucket)).get("rules", [])
        assert sorted(r["id"] for r in got) == ["abort-mpu", "expire"]
        abort = next(r for r in got if r["id"] == "abort-mpu")
        assert abort["abort_incomplete_multipart_upload"]["days_after_initiation"] == 1

    def test_cors_roundtrip(self, s3: S3Client, bucket: str):
        s3.put_bucket_cors(
            bucket, cors_configuration={"cors_rules": [{"allowed_methods": ["GET"], "allowed_origins": ["*"]}]}
        )
        assert (s3.get_bucket_cors(bucket))["cors_rules"][0]["allowed_methods"] == ["GET"]
        s3.delete_bucket_cors(bucket)

    def test_read_only_configuration(self, s3: S3Client, bucket: str):
        assert "owner" in s3.get_bucket_acl(bucket)
        s3.get_bucket_notification_configuration(bucket)


# ---------------------------------------------------------------------------
# objects
# ---------------------------------------------------------------------------


class TestAsyncObjects:  # unasync: generate
    async def test_put_get_head_roundtrip(self, async_s3: AsyncS3Client, bucket: str):
        await async_s3.put_object(bucket, "a.txt", body=DATA)
        assert await aread_body(async_s3.get_object(bucket, "a.txt")) == DATA
        assert (await async_s3.head_object(bucket, "a.txt"))["content_length"] == len(DATA)

    async def test_content_type_and_metadata(self, async_s3: AsyncS3Client, bucket: str):
        await async_s3.put_object(bucket, "meta.txt", body=b"x", content_type="text/plain", metadata={"foo": "bar"})
        head = await async_s3.head_object(bucket, "meta.txt")
        assert head.get("content_type") == "text/plain"
        assert head.get("metadata") == {"foo": "bar"}

    async def test_range_get(self, async_s3: AsyncS3Client, bucket: str):
        await async_s3.put_object(bucket, "a.txt", body=DATA)
        assert await aread_body(async_s3.get_object(bucket, "a.txt", range="bytes=0-4")) == DATA[:5]

    async def test_key_with_special_characters(self, async_s3: AsyncS3Client, bucket: str):
        key = "dir with space/ünï+code &=.txt"
        await async_s3.put_object(bucket, key, body=b"k")
        assert await aread_body(async_s3.get_object(bucket, key)) == b"k"
        listed = (await async_s3.list_objects_v2(bucket, prefix="dir with space/")).get("contents", [])
        assert [o["key"] for o in listed] == [key]

    async def test_copy_object(self, async_s3: AsyncS3Client, bucket: str):
        await async_s3.put_object(bucket, "a.txt", body=DATA)
        await async_s3.copy_object(bucket, f"{bucket}/a.txt", "copy.txt")
        assert await aread_body(async_s3.get_object(bucket, "copy.txt")) == DATA

    async def test_copy_missing_source_raises(self, async_s3: AsyncS3Client, bucket: str):
        with pytest.raises(ServiceError) as info:
            await async_s3.copy_object(bucket, f"{bucket}/does-not-exist", "copy.txt")
        assert info.value.code == "NoSuchKey"

    @pytest.mark.skipif(sys.platform == "emscripten", reason="fetch transparently decodes Content-Encoding")
    async def test_content_encoding_is_not_decoded(self, async_s3: AsyncS3Client, bucket: str):
        gz = gzip.compress(b"compressed payload " * 50)
        await async_s3.put_object(bucket, "blob.gz", body=gz, content_encoding="gzip")
        assert await aread_body(async_s3.get_object(bucket, "blob.gz")) == gz
        assert (await async_s3.head_object(bucket, "blob.gz")).get("content_encoding") == "gzip"

    async def test_object_tagging(self, async_s3: AsyncS3Client, bucket: str):
        await async_s3.put_object(bucket, "a.txt", body=b"x")
        await async_s3.put_object_tagging(bucket, "a.txt", tagging={"tag_set": [{"key": "k", "value": "v"}]})
        assert (await async_s3.get_object_tagging(bucket, "a.txt"))["tag_set"] == [{"key": "k", "value": "v"}]
        await async_s3.delete_object_tagging(bucket, "a.txt")
        assert (await async_s3.get_object_tagging(bucket, "a.txt"))["tag_set"] == []

    async def test_get_object_attributes(self, async_s3: AsyncS3Client, bucket: str):
        await async_s3.put_object(bucket, "a.txt", body=DATA)
        attrs = await async_s3.get_object_attributes(bucket, "a.txt", object_attributes=["ObjectSize", "ETag"])
        assert attrs.get("object_size") == len(DATA)
        assert attrs.get("e_tag")

    async def test_streaming_put_from_iterator(self, async_s3: AsyncS3Client, bucket: str):
        async def chunks():
            yield b"ab"
            yield b"cd"

        await async_s3.put_object(bucket, "stream.bin", body=chunks(), content_length=4)
        assert await aread_body(async_s3.get_object(bucket, "stream.bin")) == b"abcd"

    async def test_checksum_algorithm_on_bytes(self, async_s3: AsyncS3Client, bucket: str):
        out = await async_s3.put_object(bucket, "crc.bin", body=DATA, checksum_algorithm="CRC32")
        assert out.get("checksum_crc32") == crc32_b64(DATA)
        async with async_s3.get_object(bucket, "crc.bin", checksum_mode="ENABLED") as obj:
            assert obj.get("checksum_crc32") == crc32_b64(DATA)
            assert b"".join([c async for c in obj["body"]]) == DATA

    @pytest.mark.parametrize("algorithm", [None, *CHECKSUM_ALGORITHMS])
    async def test_delete_objects(self, async_s3: AsyncS3Client, bucket: str, algorithm: ChecksumAlgorithm | None):
        # DeleteObjects is requestChecksumRequired: the SDK must add an integrity header on its own.
        keys = [f"d/{i}" for i in range(3)]
        for key in keys:
            await async_s3.put_object(bucket, key, body=b"x")
        if algorithm is None:
            out = await async_s3.delete_objects(bucket, delete={"objects": [{"key": k} for k in keys]})
        else:
            out = await async_s3.delete_objects(
                bucket, delete={"objects": [{"key": k} for k in keys]}, checksum_algorithm=algorithm
            )
        assert sorted(d["key"] for d in out.get("deleted", [])) == keys
        assert not out.get("errors")
        assert (await async_s3.list_objects_v2(bucket, prefix="d/")).get("contents", []) == []

    async def test_missing_object_errors(self, async_s3: AsyncS3Client, bucket: str):
        with pytest.raises(NoSuchKey):
            await aread_body(async_s3.get_object(bucket, "nope.txt"))
        with pytest.raises(NotFound):
            await async_s3.head_object(bucket, "nope.txt")

    async def test_wait_until_object_exists(self, async_s3: AsyncS3Client, bucket: str):
        await async_s3.put_object(bucket, "a.txt", body=b"x")
        await async_s3.wait_until_object_exists(bucket, "a.txt", max_wait_time=10)

    async def test_concurrent_puts(self, async_s3: AsyncS3Client, bucket: str):
        counter = itertools.count()

        async def put() -> None:
            await async_s3.put_object(bucket, f"c/{next(counter)}", body=b"x")

        await agather(put, 10)
        assert len((await async_s3.list_objects_v2(bucket, prefix="c/")).get("contents", [])) == 10

class TestObjects:  # unasync: generated
    def test_put_get_head_roundtrip(self, s3: S3Client, bucket: str):
        s3.put_object(bucket, "a.txt", body=DATA)
        assert read_body(s3.get_object(bucket, "a.txt")) == DATA
        assert (s3.head_object(bucket, "a.txt"))["content_length"] == len(DATA)

    def test_content_type_and_metadata(self, s3: S3Client, bucket: str):
        s3.put_object(bucket, "meta.txt", body=b"x", content_type="text/plain", metadata={"foo": "bar"})
        head = s3.head_object(bucket, "meta.txt")
        assert head.get("content_type") == "text/plain"
        assert head.get("metadata") == {"foo": "bar"}

    def test_range_get(self, s3: S3Client, bucket: str):
        s3.put_object(bucket, "a.txt", body=DATA)
        assert read_body(s3.get_object(bucket, "a.txt", range="bytes=0-4")) == DATA[:5]

    def test_key_with_special_characters(self, s3: S3Client, bucket: str):
        key = "dir with space/ünï+code &=.txt"
        s3.put_object(bucket, key, body=b"k")
        assert read_body(s3.get_object(bucket, key)) == b"k"
        listed = (s3.list_objects_v2(bucket, prefix="dir with space/")).get("contents", [])
        assert [o["key"] for o in listed] == [key]

    def test_copy_object(self, s3: S3Client, bucket: str):
        s3.put_object(bucket, "a.txt", body=DATA)
        s3.copy_object(bucket, f"{bucket}/a.txt", "copy.txt")
        assert read_body(s3.get_object(bucket, "copy.txt")) == DATA

    def test_copy_missing_source_raises(self, s3: S3Client, bucket: str):
        with pytest.raises(ServiceError) as info:
            s3.copy_object(bucket, f"{bucket}/does-not-exist", "copy.txt")
        assert info.value.code == "NoSuchKey"

    @pytest.mark.skipif(sys.platform == "emscripten", reason="fetch transparently decodes Content-Encoding")
    def test_content_encoding_is_not_decoded(self, s3: S3Client, bucket: str):
        gz = gzip.compress(b"compressed payload " * 50)
        s3.put_object(bucket, "blob.gz", body=gz, content_encoding="gzip")
        assert read_body(s3.get_object(bucket, "blob.gz")) == gz
        assert (s3.head_object(bucket, "blob.gz")).get("content_encoding") == "gzip"

    def test_object_tagging(self, s3: S3Client, bucket: str):
        s3.put_object(bucket, "a.txt", body=b"x")
        s3.put_object_tagging(bucket, "a.txt", tagging={"tag_set": [{"key": "k", "value": "v"}]})
        assert (s3.get_object_tagging(bucket, "a.txt"))["tag_set"] == [{"key": "k", "value": "v"}]
        s3.delete_object_tagging(bucket, "a.txt")
        assert (s3.get_object_tagging(bucket, "a.txt"))["tag_set"] == []

    def test_get_object_attributes(self, s3: S3Client, bucket: str):
        s3.put_object(bucket, "a.txt", body=DATA)
        attrs = s3.get_object_attributes(bucket, "a.txt", object_attributes=["ObjectSize", "ETag"])
        assert attrs.get("object_size") == len(DATA)
        assert attrs.get("e_tag")

    def test_streaming_put_from_iterator(self, s3: S3Client, bucket: str):
        def chunks():
            yield b"ab"
            yield b"cd"

        s3.put_object(bucket, "stream.bin", body=chunks(), content_length=4)
        assert read_body(s3.get_object(bucket, "stream.bin")) == b"abcd"

    def test_checksum_algorithm_on_bytes(self, s3: S3Client, bucket: str):
        out = s3.put_object(bucket, "crc.bin", body=DATA, checksum_algorithm="CRC32")
        assert out.get("checksum_crc32") == crc32_b64(DATA)
        with s3.get_object(bucket, "crc.bin", checksum_mode="ENABLED") as obj:
            assert obj.get("checksum_crc32") == crc32_b64(DATA)
            assert b"".join([c for c in obj["body"]]) == DATA

    @pytest.mark.parametrize("algorithm", [None, *CHECKSUM_ALGORITHMS])
    def test_delete_objects(self, s3: S3Client, bucket: str, algorithm: ChecksumAlgorithm | None):
        # DeleteObjects is requestChecksumRequired: the SDK must add an integrity header on its own.
        keys = [f"d/{i}" for i in range(3)]
        for key in keys:
            s3.put_object(bucket, key, body=b"x")
        if algorithm is None:
            out = s3.delete_objects(bucket, delete={"objects": [{"key": k} for k in keys]})
        else:
            out = s3.delete_objects(
                bucket, delete={"objects": [{"key": k} for k in keys]}, checksum_algorithm=algorithm
            )
        assert sorted(d["key"] for d in out.get("deleted", [])) == keys
        assert not out.get("errors")
        assert (s3.list_objects_v2(bucket, prefix="d/")).get("contents", []) == []

    def test_missing_object_errors(self, s3: S3Client, bucket: str):
        with pytest.raises(NoSuchKey):
            read_body(s3.get_object(bucket, "nope.txt"))
        with pytest.raises(NotFound):
            s3.head_object(bucket, "nope.txt")

    def test_wait_until_object_exists(self, s3: S3Client, bucket: str):
        s3.put_object(bucket, "a.txt", body=b"x")
        s3.wait_until_object_exists(bucket, "a.txt", max_wait_time=10)

    def test_concurrent_puts(self, s3: S3Client, bucket: str):
        counter = itertools.count()

        def put() -> None:
            s3.put_object(bucket, f"c/{next(counter)}", body=b"x")

        gather(put, 10)
        assert len((s3.list_objects_v2(bucket, prefix="c/")).get("contents", [])) == 10


# ---------------------------------------------------------------------------
# listing
# ---------------------------------------------------------------------------


@pytest.fixture
def listed_bucket(s3: S3Client, bucket: str) -> str:
    for i in range(7):
        s3.put_object(bucket, f"list/{i:02d}.txt", body=b"x")
    s3.put_object(bucket, "other/x.txt", body=b"x")
    return bucket


class TestAsyncListing:  # unasync: generate
    async def test_list_objects_v1_and_v2(self, async_s3: AsyncS3Client, listed_bucket: str):
        v1 = (await async_s3.list_objects(listed_bucket, prefix="list/")).get("contents", [])
        v2 = (await async_s3.list_objects_v2(listed_bucket, prefix="list/")).get("contents", [])
        assert [o["key"] for o in v1] == [o["key"] for o in v2] == [f"list/{i:02d}.txt" for i in range(7)]

    async def test_manual_pagination(self, async_s3: AsyncS3Client, listed_bucket: str):
        keys, token, pages = [], None, 0
        while True:
            out = await async_s3.list_objects_v2(listed_bucket, prefix="list/", max_keys=3, continuation_token=token)
            keys += [o["key"] for o in out.get("contents", [])]
            pages += 1
            if not out.get("is_truncated"):
                break
            token = out["next_continuation_token"]
        assert pages == 3
        assert keys == [f"list/{i:02d}.txt" for i in range(7)]

    async def test_iter_list_objects_v2_yields_pages(self, async_s3: AsyncS3Client, listed_bucket: str):
        pages = []
        async for page in async_s3.iter_list_objects_v2(listed_bucket, prefix="list/", max_keys=3):
            pages.append(page)
            assert len(pages) <= 10, "paginator does not terminate"
        assert [len(p.get("contents", [])) for p in pages] == [3, 3, 1]

    async def test_delimiter_common_prefixes(self, async_s3: AsyncS3Client, listed_bucket: str):
        out = await async_s3.list_objects_v2(listed_bucket, delimiter="/")
        assert sorted(p["prefix"] for p in out.get("common_prefixes", [])) == ["list/", "other/"]
        assert out.get("contents", []) == []

class TestListing:  # unasync: generated
    def test_list_objects_v1_and_v2(self, s3: S3Client, listed_bucket: str):
        v1 = (s3.list_objects(listed_bucket, prefix="list/")).get("contents", [])
        v2 = (s3.list_objects_v2(listed_bucket, prefix="list/")).get("contents", [])
        assert [o["key"] for o in v1] == [o["key"] for o in v2] == [f"list/{i:02d}.txt" for i in range(7)]

    def test_manual_pagination(self, s3: S3Client, listed_bucket: str):
        keys, token, pages = [], None, 0
        while True:
            out = s3.list_objects_v2(listed_bucket, prefix="list/", max_keys=3, continuation_token=token)
            keys += [o["key"] for o in out.get("contents", [])]
            pages += 1
            if not out.get("is_truncated"):
                break
            token = out["next_continuation_token"]
        assert pages == 3
        assert keys == [f"list/{i:02d}.txt" for i in range(7)]

    def test_iter_list_objects_v2_yields_pages(self, s3: S3Client, listed_bucket: str):
        pages = []
        for page in s3.iter_list_objects_v2(listed_bucket, prefix="list/", max_keys=3):
            pages.append(page)
            assert len(pages) <= 10, "paginator does not terminate"
        assert [len(p.get("contents", [])) for p in pages] == [3, 3, 1]

    def test_delimiter_common_prefixes(self, s3: S3Client, listed_bucket: str):
        out = s3.list_objects_v2(listed_bucket, delimiter="/")
        assert sorted(p["prefix"] for p in out.get("common_prefixes", [])) == ["list/", "other/"]
        assert out.get("contents", []) == []


# ---------------------------------------------------------------------------
# multipart
# ---------------------------------------------------------------------------


class TestAsyncMultipart:  # unasync: generate
    async def test_upload_parts_and_complete(self, async_s3: AsyncS3Client, bucket: str):
        p1, p2 = os.urandom(5 * MiB), b"B" * 1024
        uid = (await async_s3.create_multipart_upload(bucket, "mp.bin"))["upload_id"]
        e1 = (await async_s3.upload_part(bucket, "mp.bin", 1, uid, body=p1))["e_tag"]
        e2 = (await async_s3.upload_part(bucket, "mp.bin", 2, uid, body=p2))["e_tag"]
        listed = (await async_s3.list_parts(bucket, "mp.bin", uid)).get("parts", [])
        assert [p["part_number"] for p in listed] == [1, 2]
        await async_s3.complete_multipart_upload(
            bucket,
            "mp.bin",
            uid,
            multipart_upload={"parts": [{"part_number": 1, "e_tag": e1}, {"part_number": 2, "e_tag": e2}]},
        )
        assert await aread_body(async_s3.get_object(bucket, "mp.bin")) == p1 + p2

    async def test_iter_list_parts_terminates(self, async_s3: AsyncS3Client, bucket: str):
        # Regression: the paginator used to loop forever on a single page.
        uid = (await async_s3.create_multipart_upload(bucket, "parts.bin"))["upload_id"]
        for n in (1, 2, 3):
            await async_s3.upload_part(bucket, "parts.bin", n, uid, body=b"p" * 10)
        for max_parts in (None, 1):
            got = []
            async for part in async_s3.iter_list_parts(bucket, "parts.bin", uid, max_parts=max_parts):
                got.append(part["part_number"])
                assert len(got) <= 10, "paginator does not terminate"
            assert got == [1, 2, 3]

    async def test_upload_part_copy_list_and_abort(self, async_s3: AsyncS3Client, bucket: str):
        await async_s3.put_object(bucket, "src.bin", body=b"S" * 1024)
        uid = (await async_s3.create_multipart_upload(bucket, "mp2.bin"))["upload_id"]
        out = await async_s3.upload_part_copy(bucket, f"{bucket}/src.bin", "mp2.bin", 1, uid)
        assert out["copy_part_result"]["e_tag"]
        uploads = (await async_s3.list_multipart_uploads(bucket)).get("uploads", [])
        assert uid in [u["upload_id"] for u in uploads]
        await async_s3.abort_multipart_upload(bucket, "mp2.bin", uid)
        uploads = (await async_s3.list_multipart_uploads(bucket)).get("uploads", [])
        assert uid not in [u["upload_id"] for u in uploads]

    async def test_complete_with_wrong_etag_raises(self, async_s3: AsyncS3Client, bucket: str):
        uid = (await async_s3.create_multipart_upload(bucket, "bad.bin"))["upload_id"]
        await async_s3.upload_part(bucket, "bad.bin", 1, uid, body=b"z")
        with pytest.raises(ServiceError) as info:
            await async_s3.complete_multipart_upload(
                bucket,
                "bad.bin",
                uid,
                multipart_upload={"parts": [{"part_number": 1, "e_tag": '"00000000000000000000000000000000"'}]},
            )
        assert info.value.code == "InvalidPart"

    async def test_abort_unknown_upload_raises(self, async_s3: AsyncS3Client, bucket: str):
        with pytest.raises(NoSuchUpload):
            await async_s3.abort_multipart_upload(bucket, "x", "bogus")

class TestMultipart:  # unasync: generated
    def test_upload_parts_and_complete(self, s3: S3Client, bucket: str):
        p1, p2 = os.urandom(5 * MiB), b"B" * 1024
        uid = (s3.create_multipart_upload(bucket, "mp.bin"))["upload_id"]
        e1 = (s3.upload_part(bucket, "mp.bin", 1, uid, body=p1))["e_tag"]
        e2 = (s3.upload_part(bucket, "mp.bin", 2, uid, body=p2))["e_tag"]
        listed = (s3.list_parts(bucket, "mp.bin", uid)).get("parts", [])
        assert [p["part_number"] for p in listed] == [1, 2]
        s3.complete_multipart_upload(
            bucket,
            "mp.bin",
            uid,
            multipart_upload={"parts": [{"part_number": 1, "e_tag": e1}, {"part_number": 2, "e_tag": e2}]},
        )
        assert read_body(s3.get_object(bucket, "mp.bin")) == p1 + p2

    def test_iter_list_parts_terminates(self, s3: S3Client, bucket: str):
        # Regression: the paginator used to loop forever on a single page.
        uid = (s3.create_multipart_upload(bucket, "parts.bin"))["upload_id"]
        for n in (1, 2, 3):
            s3.upload_part(bucket, "parts.bin", n, uid, body=b"p" * 10)
        for max_parts in (None, 1):
            got = []
            for part in s3.iter_list_parts(bucket, "parts.bin", uid, max_parts=max_parts):
                got.append(part["part_number"])
                assert len(got) <= 10, "paginator does not terminate"
            assert got == [1, 2, 3]

    def test_upload_part_copy_list_and_abort(self, s3: S3Client, bucket: str):
        s3.put_object(bucket, "src.bin", body=b"S" * 1024)
        uid = (s3.create_multipart_upload(bucket, "mp2.bin"))["upload_id"]
        out = s3.upload_part_copy(bucket, f"{bucket}/src.bin", "mp2.bin", 1, uid)
        assert out["copy_part_result"]["e_tag"]
        uploads = (s3.list_multipart_uploads(bucket)).get("uploads", [])
        assert uid in [u["upload_id"] for u in uploads]
        s3.abort_multipart_upload(bucket, "mp2.bin", uid)
        uploads = (s3.list_multipart_uploads(bucket)).get("uploads", [])
        assert uid not in [u["upload_id"] for u in uploads]

    def test_complete_with_wrong_etag_raises(self, s3: S3Client, bucket: str):
        uid = (s3.create_multipart_upload(bucket, "bad.bin"))["upload_id"]
        s3.upload_part(bucket, "bad.bin", 1, uid, body=b"z")
        with pytest.raises(ServiceError) as info:
            s3.complete_multipart_upload(
                bucket,
                "bad.bin",
                uid,
                multipart_upload={"parts": [{"part_number": 1, "e_tag": '"00000000000000000000000000000000"'}]},
            )
        assert info.value.code == "InvalidPart"

    def test_abort_unknown_upload_raises(self, s3: S3Client, bucket: str):
        with pytest.raises(NoSuchUpload):
            s3.abort_multipart_upload(bucket, "x", "bogus")


# ---------------------------------------------------------------------------
# presigned URLs, exercised with a plain HTTP client
# ---------------------------------------------------------------------------


class TestAsyncPresigned:  # unasync: generate
    async def test_get_and_head(self, async_s3: AsyncS3Client, bucket: str):
        await async_s3.put_object(bucket, "a.txt", body=DATA)
        async with AsyncClient() as http:
            response = await http.request("GET", await async_s3.presigned_get_object(bucket, "a.txt", 300))
            assert response.status == 200
            assert await response.aread() == DATA
            response = await http.request("HEAD", await async_s3.presigned_head_object(bucket, "a.txt", 300))
            assert response.status == 200

    async def test_put_and_delete(self, async_s3: AsyncS3Client, bucket: str):
        async with AsyncClient() as http:
            url = await async_s3.presigned_put_object(bucket, "p.txt", 300)
            response = await http.request("PUT", url, body=b"via-presign")
            assert response.status == 200
            assert await aread_body(async_s3.get_object(bucket, "p.txt")) == b"via-presign"
            response = await http.request("DELETE", await async_s3.presigned_delete_object(bucket, "p.txt", 300))
            assert response.status in (200, 204)
        with pytest.raises(NoSuchKey):
            await aread_body(async_s3.get_object(bucket, "p.txt"))

    async def test_upload_part(self, async_s3: AsyncS3Client, bucket: str):
        uid = (await async_s3.create_multipart_upload(bucket, "mp3.bin"))["upload_id"]
        async with AsyncClient() as http:
            url = await async_s3.presigned_upload_part(bucket, "mp3.bin", 1, uid, 300)
            response = await http.request("PUT", url, body=b"C" * 1024)
        assert response.status == 200
        etag = response.headers.get("etag")
        assert etag
        await async_s3.complete_multipart_upload(
            bucket, "mp3.bin", uid, multipart_upload={"parts": [{"part_number": 1, "e_tag": etag}]}
        )
        assert await aread_body(async_s3.get_object(bucket, "mp3.bin")) == b"C" * 1024

class TestPresigned:  # unasync: generated
    def test_get_and_head(self, s3: S3Client, bucket: str):
        s3.put_object(bucket, "a.txt", body=DATA)
        with Client() as http:
            response = http.request("GET", s3.presigned_get_object(bucket, "a.txt", 300))
            assert response.status == 200
            assert response.read() == DATA
            response = http.request("HEAD", s3.presigned_head_object(bucket, "a.txt", 300))
            assert response.status == 200

    def test_put_and_delete(self, s3: S3Client, bucket: str):
        with Client() as http:
            url = s3.presigned_put_object(bucket, "p.txt", 300)
            response = http.request("PUT", url, body=b"via-presign")
            assert response.status == 200
            assert read_body(s3.get_object(bucket, "p.txt")) == b"via-presign"
            response = http.request("DELETE", s3.presigned_delete_object(bucket, "p.txt", 300))
            assert response.status in (200, 204)
        with pytest.raises(NoSuchKey):
            read_body(s3.get_object(bucket, "p.txt"))

    def test_upload_part(self, s3: S3Client, bucket: str):
        uid = (s3.create_multipart_upload(bucket, "mp3.bin"))["upload_id"]
        with Client() as http:
            url = s3.presigned_upload_part(bucket, "mp3.bin", 1, uid, 300)
            response = http.request("PUT", url, body=b"C" * 1024)
        assert response.status == 200
        etag = response.headers.get("etag")
        assert etag
        s3.complete_multipart_upload(
            bucket, "mp3.bin", uid, multipart_upload={"parts": [{"part_number": 1, "e_tag": etag}]}
        )
        assert read_body(s3.get_object(bucket, "mp3.bin")) == b"C" * 1024


# ---------------------------------------------------------------------------
# errors
# ---------------------------------------------------------------------------


class TestAsyncErrors:  # unasync: generate
    async def test_bad_credentials_raise(self, s3_backend: str):
        bad = Credentials(access_key="AKIAIOSFODNN7EXAMPLE", secret_key="bad")
        async with make_async_s3_client(s3_backend, credentials=bad) as client:
            with pytest.raises(ServiceError) as info:
                await client.list_buckets()
        assert info.value.code in ("InvalidAccessKeyId", "AccessDenied", "SignatureDoesNotMatch")

    # The SDK types exactly the errors the Smithy model declares on an operation. Codes the model does
    # not declare (DeleteBucket and GetObjectTagging declare none, PutObject not NoSuchBucket) surface as
    # UnknownServiceError with the wire code, never as the typed class another operation uses.
    async def test_undeclared_error_codes_are_untyped(self, async_s3: AsyncS3Client, bucket: str):
        missing = unique_name("capotest-missing")
        with pytest.raises(UnknownServiceError) as info:
            await async_s3.delete_bucket(missing)
        assert info.value.code == "NoSuchBucket"
        with pytest.raises(UnknownServiceError) as info:
            await async_s3.put_object(missing, "k", body=b"x")
        assert info.value.code == "NoSuchBucket"
        with pytest.raises(UnknownServiceError) as info:
            await async_s3.get_object_tagging(bucket, "nope.txt")
        assert info.value.code == "NoSuchKey"

    async def test_declared_error_codes_are_typed(self, async_s3: AsyncS3Client, bucket: str):
        with pytest.raises(NoSuchBucket):
            await async_s3.list_objects_v2(unique_name("capotest-missing"))
        with pytest.raises(NoSuchKey):
            await aread_body(async_s3.get_object(bucket, "nope.txt"))
        with pytest.raises(NotFound):
            await async_s3.head_object(bucket, "nope.txt")
        with pytest.raises(NoSuchUpload):
            await async_s3.abort_multipart_upload(bucket, "x", "bogus")

class TestErrors:  # unasync: generated
    def test_bad_credentials_raise(self, s3_backend: str):
        bad = Credentials(access_key="AKIAIOSFODNN7EXAMPLE", secret_key="bad")
        with make_s3_client(s3_backend, credentials=bad) as client:
            with pytest.raises(ServiceError) as info:
                client.list_buckets()
        assert info.value.code in ("InvalidAccessKeyId", "AccessDenied", "SignatureDoesNotMatch")

    # The SDK types exactly the errors the Smithy model declares on an operation. Codes the model does
    # not declare (DeleteBucket and GetObjectTagging declare none, PutObject not NoSuchBucket) surface as
    # UnknownServiceError with the wire code, never as the typed class another operation uses.
    def test_undeclared_error_codes_are_untyped(self, s3: S3Client, bucket: str):
        missing = unique_name("capotest-missing")
        with pytest.raises(UnknownServiceError) as info:
            s3.delete_bucket(missing)
        assert info.value.code == "NoSuchBucket"
        with pytest.raises(UnknownServiceError) as info:
            s3.put_object(missing, "k", body=b"x")
        assert info.value.code == "NoSuchBucket"
        with pytest.raises(UnknownServiceError) as info:
            s3.get_object_tagging(bucket, "nope.txt")
        assert info.value.code == "NoSuchKey"

    def test_declared_error_codes_are_typed(self, s3: S3Client, bucket: str):
        with pytest.raises(NoSuchBucket):
            s3.list_objects_v2(unique_name("capotest-missing"))
        with pytest.raises(NoSuchKey):
            read_body(s3.get_object(bucket, "nope.txt"))
        with pytest.raises(NotFound):
            s3.head_object(bucket, "nope.txt")
        with pytest.raises(NoSuchUpload):
            s3.abort_multipart_upload(bucket, "x", "bogus")
