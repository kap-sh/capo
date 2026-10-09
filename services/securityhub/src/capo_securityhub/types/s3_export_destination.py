"""Generated from Smithy shape ``com.amazonaws.securityhub#S3ExportDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.s3_object_prefix


class S3ExportDestination(TypedDict, closed=True):
    bucket_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the Amazon S3 bucket that Security Hub writes the export to. You must own the bucket, and its bucket policy must grant the Security Hub service principal (<code>exportv2.securityhub.amazonaws.com</code>) permission to write objects. For the required bucket policy, see the Examples section of <code>StartExportJobV2</code>.</p>"""
    kms_key_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the Amazon Web Services KMS key that Security Hub uses to encrypt the export objects with server-side encryption. The key policy must allow the Security Hub service principal (<code>exportv2.securityhub.amazonaws.com</code>) to use the key through Amazon S3. For the required key policy, see the Examples section of <code>StartExportJobV2</code>.</p> <p>The key must meet all of the following requirements:</p> <ul> <li> <p>It must be a symmetric key with a key usage of <code>ENCRYPT_DECRYPT</code>.</p> </li> <li> <p>It must be a single-Region key. Multi-Region keys, whose key IDs begin with <code>mrk-</code>, are rejected.</p> </li> <li> <p>You must specify the full key ARN. Key IDs and aliases are rejected.</p> </li> <li> <p>The key must be in the same Amazon Web Services account as the export job.</p> </li> <li> <p>The key must be in the same Amazon Web Services Region as the export job.</p> </li> <li> <p>The key must be in the <code>aws</code>, <code>aws-cn</code>, or <code>aws-us-gov</code> partition.</p> </li> </ul>"""
    object_prefix: NotRequired["capo_securityhub.types.s3_object_prefix.S3ObjectPrefix"]
    """<p>An optional key prefix that Security Hub prepends to the Amazon S3 object keys of the export output. Use a prefix to organize exports within the bucket. The value can be up to 512 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ExportDestination) -> dict:
    out: dict = {}
    if "bucket_arn" in value:
        out["BucketArn"] = value["bucket_arn"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "object_prefix" in value:
        out["ObjectPrefix"] = value["object_prefix"]
    return out


def deserialize_json(data: dict) -> S3ExportDestination:
    out: S3ExportDestination = {}  # type: ignore[typeddict-item]
    if data.get("BucketArn") is not None:
        out["bucket_arn"] = data["BucketArn"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("ObjectPrefix") is not None:
        out["object_prefix"] = data["ObjectPrefix"]
    return out
