"""Generated from Smithy shape ``com.amazonaws.s3#PutObjectAnnotationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.annotation_name
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.checksum_crc32
    import capo_s3.types.checksum_crc32_c
    import capo_s3.types.checksum_crc64_nvme
    import capo_s3.types.checksum_md5
    import capo_s3.types.checksum_sha1
    import capo_s3.types.checksum_sha256
    import capo_s3.types.checksum_sha512
    import capo_s3.types.checksum_xxhash3
    import capo_s3.types.checksum_xxhash64
    import capo_s3.types.checksum_xxhash128
    import capo_s3.types.content_md5
    import capo_s3.types.object_if_match
    import capo_s3.types.object_key
    import capo_s3.types.object_version_id
    import capo_s3.types.request_payer
    import capo_s3.types.streaming_blob


class PutObjectAnnotationRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket that contains the object.</p>"""
    key: "capo_s3.types.object_key.ObjectKey"
    """<p>The object key.</p>"""
    version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p>The version ID of the object to attach the annotation to.</p>"""
    annotation_name: "capo_s3.types.annotation_name.AnnotationName"
    """<p>The name of the annotation.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 512 bytes.</p>"""
    annotation_payload: "capo_s3.types.streaming_blob.StreamingBlob"
    """<p>The annotation payload. Must be between 1 byte and 1 MiB in size, and must be valid UTF-8 encoded text. If the payload contains invalid UTF-8 bytes, the request fails with HTTP 415 (Unsupported Media Type). To store binary data, encode the payload using Base64 before uploading.</p>"""
    object_if_match: NotRequired["capo_s3.types.object_if_match.ObjectIfMatch"]
    """<p>If specified, the operation only succeeds if the object's ETag matches the provided value.</p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>The checksum algorithm to use. Supported values: <code>CRC32</code>, <code>CRC32C</code>, <code>CRC64NVME</code>, <code>SHA1</code>, <code>SHA256</code>, <code>SHA512</code>, <code>MD5</code>, <code>XXHASH64</code>, <code>XXHASH3</code>, <code>XXHASH128</code>.</p>"""
    checksum_crc32: NotRequired["capo_s3.types.checksum_crc32.ChecksumCRC32"]
    """<p>Base64-encoded CRC32 checksum of the annotation payload.</p>"""
    checksum_crc32_c: NotRequired["capo_s3.types.checksum_crc32_c.ChecksumCRC32C"]
    """<p>Base64-encoded CRC32C checksum of the annotation payload.</p>"""
    checksum_crc64_nvme: NotRequired[
        "capo_s3.types.checksum_crc64_nvme.ChecksumCRC64NVME"
    ]
    """<p>Base64-encoded CRC64NVME checksum of the annotation payload.</p>"""
    checksum_sha1: NotRequired["capo_s3.types.checksum_sha1.ChecksumSHA1"]
    """<p>Base64-encoded SHA1 checksum of the annotation payload.</p>"""
    checksum_sha256: NotRequired["capo_s3.types.checksum_sha256.ChecksumSHA256"]
    """<p>Base64-encoded SHA256 checksum of the annotation payload.</p>"""
    checksum_sha512: NotRequired["capo_s3.types.checksum_sha512.ChecksumSHA512"]
    """<p>Base64-encoded SHA512 checksum of the annotation payload.</p>"""
    checksum_md5: NotRequired["capo_s3.types.checksum_md5.ChecksumMD5"]
    """<p>Base64-encoded MD5 checksum of the annotation payload.</p>"""
    checksum_xxhash64: NotRequired["capo_s3.types.checksum_xxhash64.ChecksumXXHASH64"]
    """<p>Base64-encoded XXHASH64 checksum of the annotation payload.</p>"""
    checksum_xxhash3: NotRequired["capo_s3.types.checksum_xxhash3.ChecksumXXHASH3"]
    """<p>Base64-encoded XXHASH3 checksum of the annotation payload.</p>"""
    checksum_xxhash128: NotRequired[
        "capo_s3.types.checksum_xxhash128.ChecksumXXHASH128"
    ]
    """<p>Base64-encoded XXHASH128 checksum of the annotation payload.</p>"""
    content_md5: NotRequired["capo_s3.types.content_md5.ContentMD5"]
    """<p>Base64-encoded MD5 digest of the message.</p>"""
    request_payer: NotRequired["capo_s3.types.request_payer.RequestPayer"]
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the bucket is owned by a different account, the request fails with an HTTP 403 (Access Denied) error.</p>"""


def redact_sensitive(value: PutObjectAnnotationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "annotation_payload" in value:
        out["annotation_payload"] = "*** Streaming Data Redacted ***"
    return out
