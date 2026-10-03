"""Generated from Smithy shape ``com.amazonaws.sagemaker#LabelingJobResourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.vpc_config


class LabelingJobResourceConfig(TypedDict, closed=True):
    volume_kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training and inference jobs used for automated data labeling. </p> <p>You can only specify a <code>VolumeKmsKeyId</code> when you create a labeling job with automated data labeling enabled using the API operation <code>CreateLabelingJob</code>. You cannot specify an Amazon Web Services KMS key to encrypt the storage volume used for automated data labeling model training and inference when you create a labeling job using the console. To learn more, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security.html">Output Data and Storage Volume Encryption</a>.</p> <p>The <code>VolumeKmsKeyId</code> can be any of the following formats:</p> <ul> <li> <p>KMS Key ID</p> <p> <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key</p> <p> <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>"""
    vpc_config: NotRequired["capo_sagemaker.types.vpc_config.VpcConfig"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelingJobResourceConfig) -> dict:
    out: dict = {}
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    if "vpc_config" in value:
        import capo_sagemaker.types.vpc_config

        out["VpcConfig"] = capo_sagemaker.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelingJobResourceConfig:
    out: LabelingJobResourceConfig = {}  # type: ignore[typeddict-item]
    if data.get("VolumeKmsKeyId") is not None:
        out["volume_kms_key_id"] = data["VolumeKmsKeyId"]
    if data.get("VpcConfig") is not None:
        import capo_sagemaker.types.vpc_config

        out["vpc_config"] = capo_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    return out
