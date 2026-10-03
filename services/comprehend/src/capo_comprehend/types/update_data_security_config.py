"""Generated from Smithy shape ``com.amazonaws.comprehend#UpdateDataSecurityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.kms_key_id
    import capo_comprehend.types.vpc_config


class UpdateDataSecurityConfig(TypedDict, closed=True):
    model_kms_key_id: NotRequired["capo_comprehend.types.kms_key_id.KmsKeyId"]
    """<p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>"""
    volume_kms_key_id: NotRequired["capo_comprehend.types.kms_key_id.KmsKeyId"]
    """<p>ID for the KMS key that Amazon Comprehend uses to encrypt the volume.</p>"""
    vpc_config: NotRequired["capo_comprehend.types.vpc_config.VpcConfig"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDataSecurityConfig) -> dict:
    out: dict = {}
    if "model_kms_key_id" in value:
        out["ModelKmsKeyId"] = value["model_kms_key_id"]
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    if "vpc_config" in value:
        import capo_comprehend.types.vpc_config

        out["VpcConfig"] = capo_comprehend.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDataSecurityConfig:
    out: UpdateDataSecurityConfig = {}  # type: ignore[typeddict-item]
    if data.get("ModelKmsKeyId") is not None:
        out["model_kms_key_id"] = data["ModelKmsKeyId"]
    if data.get("VolumeKmsKeyId") is not None:
        out["volume_kms_key_id"] = data["VolumeKmsKeyId"]
    if data.get("VpcConfig") is not None:
        import capo_comprehend.types.vpc_config

        out["vpc_config"] = capo_comprehend.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    return out
