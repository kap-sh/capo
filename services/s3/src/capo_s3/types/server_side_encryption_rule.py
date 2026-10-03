"""Generated from Smithy shape ``com.amazonaws.s3#ServerSideEncryptionRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.blocked_encryption_types
    import capo_s3.types.bucket_key_enabled
    import capo_s3.types.server_side_encryption_by_default


class ServerSideEncryptionRule(TypedDict, closed=True):
    apply_server_side_encryption_by_default: NotRequired[
        "capo_s3.types.server_side_encryption_by_default.ServerSideEncryptionByDefault"
    ]
    """<p>Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT Object request doesn't specify any server-side encryption, this default encryption will be applied.</p>"""
    bucket_key_enabled: NotRequired["capo_s3.types.bucket_key_enabled.BucketKeyEnabled"]
    """<p>Specifies whether Amazon S3 should use an S3 Bucket Key with server-side encryption using KMS (SSE-KMS) for new objects in the bucket. Existing objects are not affected. Setting the <code>BucketKeyEnabled</code> element to <code>true</code> causes Amazon S3 to use an S3 Bucket Key. </p> <note> <ul> <li> <p> <b>General purpose buckets</b> - By default, S3 Bucket Key is not enabled. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html">Amazon S3 Bucket Keys</a> in the <i>Amazon S3 User Guide</i>.</p> </li> <li> <p> <b>Directory buckets</b> - S3 Bucket Keys are always enabled for <code>GET</code> and <code>PUT</code> operations in a directory bucket and can’t be disabled. S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html">CopyObject</a>, <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html">UploadPartCopy</a>, <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops">the Copy operation in Batch Operations</a>, or <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job">the import jobs</a>. In this case, Amazon S3 makes a call to KMS every time a copy request is made for a KMS-encrypted object.</p> </li> </ul> </note>"""
    blocked_encryption_types: NotRequired[
        "capo_s3.types.blocked_encryption_types.BlockedEncryptionTypes"
    ]
    """<p>A bucket-level setting for Amazon S3 general purpose buckets used to prevent the upload of new objects encrypted with the specified server-side encryption type. For example, blocking an encryption type will block <code>PutObject</code>, <code>CopyObject</code>, <code>PostObject</code>, multipart upload, and replication requests to the bucket for objects with the specified encryption type. However, you can continue to read and list any pre-existing objects already encrypted with the specified encryption type. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/blocking-unblocking-s3-c-encryption-gpb.html">Blocking or unblocking SSE-C for a general purpose bucket</a>.</p> <note> <p>Currently, this parameter only supports blocking or unblocking server-side encryption with customer-provided keys (SSE-C). For more information about SSE-C, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html">Using server-side encryption with customer-provided keys (SSE-C)</a>.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: ServerSideEncryptionRule, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "apply_server_side_encryption_by_default" in value:
        import capo_s3.types.server_side_encryption_by_default

        capo_s3.types.server_side_encryption_by_default.serialize_xml(
            value["apply_server_side_encryption_by_default"],
            el,
            "ApplyServerSideEncryptionByDefault",
        )
    if "bucket_key_enabled" in value:
        SubElement(el, "BucketKeyEnabled").text = (
            "true" if value["bucket_key_enabled"] else "false"
        )
    if "blocked_encryption_types" in value:
        import capo_s3.types.blocked_encryption_types

        capo_s3.types.blocked_encryption_types.serialize_xml(
            value["blocked_encryption_types"], el, "BlockedEncryptionTypes"
        )


def deserialize_xml(el: Element) -> ServerSideEncryptionRule:
    out: ServerSideEncryptionRule = {}  # type: ignore[typeddict-item]
    child_apply_server_side_encryption_by_default = el.find(
        "ApplyServerSideEncryptionByDefault"
    )
    if child_apply_server_side_encryption_by_default is not None:
        import capo_s3.types.server_side_encryption_by_default

        out["apply_server_side_encryption_by_default"] = (
            capo_s3.types.server_side_encryption_by_default.deserialize_xml(
                child_apply_server_side_encryption_by_default
            )
        )
    child_bucket_key_enabled = el.find("BucketKeyEnabled")
    if child_bucket_key_enabled is not None:
        out["bucket_key_enabled"] = (
            child_bucket_key_enabled.text or ""
        ).lower() == "true"
    child_blocked_encryption_types = el.find("BlockedEncryptionTypes")
    if child_blocked_encryption_types is not None:
        import capo_s3.types.blocked_encryption_types

        out["blocked_encryption_types"] = (
            capo_s3.types.blocked_encryption_types.deserialize_xml(
                child_blocked_encryption_types
            )
        )
    return out
