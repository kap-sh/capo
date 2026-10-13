"""Generated from Smithy shape ``com.amazonaws.s3#GetObjectAnnotationOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3.types.checksum_crc32
    import capo_s3.types.checksum_crc32_c
    import capo_s3.types.checksum_crc64_nvme
    import capo_s3.types.checksum_md5
    import capo_s3.types.checksum_sha1
    import capo_s3.types.checksum_sha256
    import capo_s3.types.checksum_sha512
    import capo_s3.types.checksum_type
    import capo_s3.types.checksum_xxhash3
    import capo_s3.types.checksum_xxhash64
    import capo_s3.types.checksum_xxhash128
    import capo_s3.types.content_length
    import capo_s3.types.e_tag
    import capo_s3.types.last_modified
    import capo_s3.types.object_version_id
    import capo_s3.types.replication_status
    import capo_s3.types.request_charged
    import capo_s3.types.server_side_encryption
    import capo_s3.types.streaming_blob


class GetObjectAnnotationOutput(TypedDict, closed=True):
    annotation_payload: "capo_s3.types.streaming_blob.StreamingBlob"
    """<p>The annotation payload.</p>"""
    object_version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p>The version ID of the object that the annotation is attached to.</p>"""
    last_modified: NotRequired["capo_s3.types.last_modified.LastModified"]
    """<p>The date and time the annotation was last modified.</p>"""
    content_length: NotRequired["capo_s3.types.content_length.ContentLength"]
    """<p>The size of the annotation payload, in bytes.</p>"""
    e_tag: NotRequired["capo_s3.types.e_tag.ETag"]
    """<p>The entity tag of the annotation.</p>"""
    checksum_crc32: NotRequired["capo_s3.types.checksum_crc32.ChecksumCRC32"]
    """<p>The CRC32 checksum of the annotation payload.</p>"""
    checksum_crc32_c: NotRequired["capo_s3.types.checksum_crc32_c.ChecksumCRC32C"]
    """<p>The CRC32C checksum of the annotation payload.</p>"""
    checksum_crc64_nvme: NotRequired[
        "capo_s3.types.checksum_crc64_nvme.ChecksumCRC64NVME"
    ]
    """<p>The CRC64NVME checksum of the annotation payload.</p>"""
    checksum_sha1: NotRequired["capo_s3.types.checksum_sha1.ChecksumSHA1"]
    """<p>The SHA1 checksum of the annotation payload.</p>"""
    checksum_sha256: NotRequired["capo_s3.types.checksum_sha256.ChecksumSHA256"]
    """<p>The SHA256 checksum of the annotation payload.</p>"""
    checksum_sha512: NotRequired["capo_s3.types.checksum_sha512.ChecksumSHA512"]
    """<p>The SHA512 checksum of the annotation payload.</p>"""
    checksum_md5: NotRequired["capo_s3.types.checksum_md5.ChecksumMD5"]
    """<p>The MD5 checksum of the annotation payload.</p>"""
    checksum_xxhash64: NotRequired["capo_s3.types.checksum_xxhash64.ChecksumXXHASH64"]
    """<p>The XXHASH64 checksum of the annotation payload.</p>"""
    checksum_xxhash3: NotRequired["capo_s3.types.checksum_xxhash3.ChecksumXXHASH3"]
    """<p>The XXHASH3 checksum of the annotation payload.</p>"""
    checksum_xxhash128: NotRequired[
        "capo_s3.types.checksum_xxhash128.ChecksumXXHASH128"
    ]
    """<p>The XXHASH128 checksum of the annotation payload.</p>"""
    checksum_type: NotRequired["capo_s3.types.checksum_type.ChecksumType"]
    """<p>The type of checksum used.</p>"""
    server_side_encryption: NotRequired[
        "capo_s3.types.server_side_encryption.ServerSideEncryption"
    ]
    """<p>The server-side encryption algorithm used.</p>"""
    request_charged: NotRequired["capo_s3.types.request_charged.RequestCharged"]
    replication_status: NotRequired[
        "capo_s3.types.replication_status.ReplicationStatus"
    ]
    """<p>The replication status of the annotation. Possible values include <code>PENDING</code>, <code>COMPLETED</code>, <code>FAILED</code>, and <code>REPLICA</code>.</p>"""


def redact_sensitive(value: GetObjectAnnotationOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "annotation_payload" in value:
        out["annotation_payload"] = "*** Streaming Data Redacted ***"
    return out
