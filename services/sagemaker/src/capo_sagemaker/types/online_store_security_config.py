"""Generated from Smithy shape ``com.amazonaws.sagemaker#OnlineStoreSecurityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.kms_key_id


class OnlineStoreSecurityConfig(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services Key Management Service (KMS) key ARN that SageMaker Feature Store uses to encrypt the Amazon S3 objects at rest using Amazon S3 server-side encryption.</p> <p>The caller (either user or IAM role) of <code>CreateFeatureGroup</code> must have below permissions to the <code>OnlineStore</code> <code>KmsKeyId</code>:</p> <ul> <li> <p> <code>"kms:Encrypt"</code> </p> </li> <li> <p> <code>"kms:Decrypt"</code> </p> </li> <li> <p> <code>"kms:DescribeKey"</code> </p> </li> <li> <p> <code>"kms:CreateGrant"</code> </p> </li> <li> <p> <code>"kms:RetireGrant"</code> </p> </li> <li> <p> <code>"kms:ReEncryptFrom"</code> </p> </li> <li> <p> <code>"kms:ReEncryptTo"</code> </p> </li> <li> <p> <code>"kms:GenerateDataKey"</code> </p> </li> <li> <p> <code>"kms:ListAliases"</code> </p> </li> <li> <p> <code>"kms:ListGrants"</code> </p> </li> <li> <p> <code>"kms:RevokeGrant"</code> </p> </li> </ul> <p>The caller (either user or IAM role) to all DataPlane operations (<code>PutRecord</code>, <code>GetRecord</code>, <code>DeleteRecord</code>) must have the following permissions to the <code>KmsKeyId</code>:</p> <ul> <li> <p> <code>"kms:Decrypt"</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnlineStoreSecurityConfig) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OnlineStoreSecurityConfig:
    out: OnlineStoreSecurityConfig = {}  # type: ignore[typeddict-item]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
