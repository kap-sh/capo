"""Generated from Smithy shape ``com.amazonaws.sagemaker#S3StorageConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.s3_uri


class S3StorageConfig(TypedDict, closed=True):
    s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The S3 URI, or location in Amazon S3, of <code>OfflineStore</code>.</p> <p>S3 URIs have a format similar to the following: <code>s3://example-bucket/prefix/</code>.</p>"""
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services Key Management Service (KMS) key ARN of the key used to encrypt any objects written into the <code>OfflineStore</code> S3 location.</p> <p>The IAM <code>roleARN</code> that is passed as a parameter to <code>CreateFeatureGroup</code> must have below permissions to the <code>KmsKeyId</code>:</p> <ul> <li> <p> <code>"kms:GenerateDataKey"</code> </p> </li> </ul>"""
    resolved_output_s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The S3 path where offline records are written.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3StorageConfig) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "resolved_output_s3_uri" in value:
        out["ResolvedOutputS3Uri"] = value["resolved_output_s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3StorageConfig:
    out: S3StorageConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("ResolvedOutputS3Uri") is not None:
        out["resolved_output_s3_uri"] = data["ResolvedOutputS3Uri"]
    return out
