"""Generated from Smithy shape ``com.amazonaws.s3#SSEKMSEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.bucket_key_enabled
    import capo_s3.types.non_empty_kms_key_arn_string


class SSEKMSEncryption(TypedDict, closed=True):
    kms_key_arn: "capo_s3.types.non_empty_kms_key_arn_string.NonEmptyKmsKeyArnString"
    """<p> Specifies the Amazon Web Services KMS key Amazon Resource Name (ARN) to use for the updated server-side encryption type. Required if <code>ObjectEncryption</code> specifies <code>SSEKMS</code>. </p> <note> <p>You must specify the full Amazon Web Services KMS key ARN. The KMS key ID and KMS key alias aren't supported.</p> </note> <p>Pattern: (<code>arn:aws[-a-z0-9]*:kms:[-a-z0-9]*:[0-9]{12}:key/.+</code>)</p>"""
    bucket_key_enabled: NotRequired["capo_s3.types.bucket_key_enabled.BucketKeyEnabled"]
    """<p> Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with server-side encryption using Key Management Service (KMS) keys (SSE-KMS). If this value isn't specified, it defaults to <code>false</code>. Setting this value to <code>true</code> causes Amazon S3 to use an S3 Bucket Key for object encryption with SSE-KMS. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html"> Using Amazon S3 Bucket Keys</a> in the <i>Amazon S3 User Guide</i>. </p> <p>Valid Values: <code>true</code> | <code>false</code> </p>"""


# --- restXml ser/de ---
def serialize_xml(value: SSEKMSEncryption, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "KMSKeyArn").text = str(value["kms_key_arn"])
    if "bucket_key_enabled" in value:
        SubElement(el, "BucketKeyEnabled").text = (
            "true" if value["bucket_key_enabled"] else "false"
        )


def deserialize_xml(el: Element) -> SSEKMSEncryption:
    out: SSEKMSEncryption = {}  # type: ignore[typeddict-item]
    child_kms_key_arn = el.find("KMSKeyArn")
    if child_kms_key_arn is not None:
        out["kms_key_arn"] = str(child_kms_key_arn.text or "")
    else:
        raise DeserializationError("SSEKMSEncryption.kms_key_arn required")
    child_bucket_key_enabled = el.find("BucketKeyEnabled")
    if child_bucket_key_enabled is not None:
        out["bucket_key_enabled"] = (
            child_bucket_key_enabled.text or ""
        ).lower() == "true"
    return out
