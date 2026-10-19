"""Generated from Smithy shape ``com.amazonaws.s3control#S3UpdateObjectEncryptionSSEKMS``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.boolean
    import capo_s3_control.types.non_empty_kms_key_arn_string


class S3UpdateObjectEncryptionSSEKMS(TypedDict, closed=True):
    kms_key_arn: (
        "capo_s3_control.types.non_empty_kms_key_arn_string.NonEmptyKmsKeyArnString"
    )
    """<p>Specifies the Amazon Web Services KMS key Amazon Resource Name (ARN) to use for the updated server-side encryption type. Required if <code>UpdateObjectEncryption</code> specifies <code>SSEKMS</code>.</p>"""
    bucket_key_enabled: NotRequired["capo_s3_control.types.boolean.Boolean"]
    """<p>Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with server-side encryption using Key Management Service (KMS) keys (SSE-KMS). If this value isn't specified, it defaults to <code>false</code>. Setting this value to <code>true</code> causes Amazon S3 to use an S3 Bucket Key for update object encryption with SSE-KMS.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: S3UpdateObjectEncryptionSSEKMS, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "KMSKeyArn").text = str(value["kms_key_arn"])
    if "bucket_key_enabled" in value:
        SubElement(el, "BucketKeyEnabled").text = (
            "true" if value["bucket_key_enabled"] else "false"
        )


def deserialize_xml(el: Element) -> S3UpdateObjectEncryptionSSEKMS:
    out: S3UpdateObjectEncryptionSSEKMS = {}  # type: ignore[typeddict-item]
    child_kms_key_arn = el.find("KMSKeyArn")
    if child_kms_key_arn is not None:
        out["kms_key_arn"] = str(child_kms_key_arn.text or "")
    else:
        out["kms_key_arn"] = ""
    child_bucket_key_enabled = el.find("BucketKeyEnabled")
    if child_bucket_key_enabled is not None:
        out["bucket_key_enabled"] = (
            child_bucket_key_enabled.text or ""
        ).lower() == "true"
    return out
