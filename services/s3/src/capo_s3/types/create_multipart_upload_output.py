"""Generated from Smithy shape ``com.amazonaws.s3#CreateMultipartUploadOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.abort_date
    import capo_s3.types.abort_rule_id
    import capo_s3.types.bucket_key_enabled
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.checksum_type
    import capo_s3.types.multipart_upload_id
    import capo_s3.types.object_key
    import capo_s3.types.request_charged
    import capo_s3.types.server_side_encryption
    import capo_s3.types.sse_customer_algorithm
    import capo_s3.types.sse_customer_key_md5
    import capo_s3.types.ssekms_encryption_context
    import capo_s3.types.ssekms_key_id


class CreateMultipartUploadOutput(TypedDict, closed=True):
    abort_date: NotRequired["capo_s3.types.abort_date.AbortDate"]
    """<p>If the bucket has a lifecycle rule configured with an action to abort incomplete multipart uploads and the prefix in the lifecycle rule matches the object name in the request, the response includes this header. The header indicates when the initiated multipart upload becomes eligible for an abort operation. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config"> Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle Configuration</a> in the <i>Amazon S3 User Guide</i>.</p> <p>The response also includes the <code>x-amz-abort-rule-id</code> header that provides the ID of the lifecycle configuration rule that defines the abort action.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    abort_rule_id: NotRequired["capo_s3.types.abort_rule_id.AbortRuleId"]
    """<p>This header is returned along with the <code>x-amz-abort-date</code> header. It identifies the applicable lifecycle configuration rule that defines the action to abort incomplete multipart uploads.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    bucket: NotRequired["capo_s3.types.bucket_name.BucketName"]
    """<p>The name of the bucket to which the multipart upload was initiated. Does not return the access point ARN or access point alias if used.</p> <note> <p>Access points are not supported by directory buckets.</p> </note>"""
    key: NotRequired["capo_s3.types.object_key.ObjectKey"]
    """<p>Object key for which the multipart upload was initiated.</p>"""
    upload_id: NotRequired["capo_s3.types.multipart_upload_id.MultipartUploadId"]
    """<p>ID for the initiated multipart upload.</p>"""
    server_side_encryption: NotRequired[
        "capo_s3.types.server_side_encryption.ServerSideEncryption"
    ]
    """<p>The server-side encryption algorithm used when you store this object in Amazon S3 or Amazon FSx.</p> <note> <p>When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side encryption option is <code>aws:fsx</code>.</p> </note>"""
    sse_customer_algorithm: NotRequired[
        "capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm"
    ]
    """<p>If server-side encryption with a customer-provided encryption key was requested, the response will include this header to confirm the encryption algorithm that's used.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    sse_customer_key_md5: NotRequired[
        "capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5"
    ]
    """<p>If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide the round-trip message integrity verification of the customer-provided encryption key.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    ssekms_key_id: NotRequired["capo_s3.types.ssekms_key_id.SSEKMSKeyId"]
    """<p>If present, indicates the ID of the KMS key that was used for object encryption.</p>"""
    ssekms_encryption_context: NotRequired[
        "capo_s3.types.ssekms_encryption_context.SSEKMSEncryptionContext"
    ]
    """<p>If present, indicates the Amazon Web Services KMS Encryption Context to use for object encryption. The value of this header is a Base64 encoded string of a UTF-8 encoded JSON, which contains the encryption context as key-value pairs.</p>"""
    bucket_key_enabled: NotRequired["capo_s3.types.bucket_key_enabled.BucketKeyEnabled"]
    """<p>Indicates whether the multipart upload uses an S3 Bucket Key for server-side encryption with Key Management Service (KMS) keys (SSE-KMS).</p>"""
    request_charged: NotRequired["capo_s3.types.request_charged.RequestCharged"]
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>The algorithm that was used to create a checksum of the object.</p>"""
    checksum_type: NotRequired["capo_s3.types.checksum_type.ChecksumType"]
    """<p> Indicates the checksum type that you want Amazon S3 to use to calculate the object’s checksum value. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateMultipartUploadOutput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "bucket" in value:
        SubElement(el, "Bucket").text = str(value["bucket"])
    if "key" in value:
        SubElement(el, "Key").text = str(value["key"])
    if "upload_id" in value:
        SubElement(el, "UploadId").text = str(value["upload_id"])


def deserialize_xml(el: Element) -> CreateMultipartUploadOutput:
    out: CreateMultipartUploadOutput = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_upload_id = el.find("UploadId")
    if child_upload_id is not None:
        out["upload_id"] = str(child_upload_id.text or "")
    return out
