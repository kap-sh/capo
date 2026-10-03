"""Generated from Smithy shape ``com.amazonaws.sagemaker#TransformResources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.transform_ami_version
    import capo_sagemaker.types.transform_instance_count
    import capo_sagemaker.types.transform_instance_type


class TransformResources(TypedDict, closed=True):
    instance_type: NotRequired[
        "capo_sagemaker.types.transform_instance_type.TransformInstanceType"
    ]
    """<p>The ML compute instance type for the transform job. If you are using built-in algorithms to transform moderately sized datasets, we recommend using ml.m4.xlarge or <code>ml.m5.large</code>instance types.</p>"""
    instance_count: NotRequired[
        "capo_sagemaker.types.transform_instance_count.TransformInstanceCount"
    ]
    """<p>The number of ML compute instances to use in the transform job. The default value is <code>1</code>, and the maximum is <code>100</code>. For distributed transform jobs, specify a value greater than <code>1</code>.</p>"""
    volume_kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt model data on the storage volume attached to the ML compute instance(s) that run the batch transform job.</p> <note> <p>Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You can't request a <code>VolumeKmsKeyId</code> when using an instance type with local storage.</p> <p>For a list of instance types that support local instance storage, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes">Instance Store Volumes</a>.</p> <p>For more information about local instance storage encryption, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html">SSD Instance Store Volumes</a>.</p> </note> <p> The <code>VolumeKmsKeyId</code> can be any of the following formats:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Alias name: <code>alias/ExampleAlias</code> </p> </li> <li> <p>Alias name ARN: <code>arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias</code> </p> </li> </ul>"""
    transform_ami_version: NotRequired[
        "capo_sagemaker.types.transform_ami_version.TransformAmiVersion"
    ]
    """<p>Specifies an option from a collection of preconfigured Amazon Machine Image (AMI) images. Each image is configured by Amazon Web Services with a set of software and driver versions.</p> <dl> <dt>al2-ami-sagemaker-batch-gpu-470</dt> <dd> <ul> <li> <p>Accelerator: GPU</p> </li> <li> <p>NVIDIA driver version: 470</p> </li> </ul> </dd> <dt>al2-ami-sagemaker-batch-gpu-535</dt> <dd> <ul> <li> <p>Accelerator: GPU</p> </li> <li> <p>NVIDIA driver version: 535</p> </li> </ul> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformResources) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import capo_sagemaker.types.transform_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.transform_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    if "transform_ami_version" in value:
        out["TransformAmiVersion"] = value["transform_ami_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TransformResources:
    out: TransformResources = {}  # type: ignore[typeddict-item]
    if data.get("InstanceType") is not None:
        import capo_sagemaker.types.transform_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.transform_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if data.get("InstanceCount") is not None:
        out["instance_count"] = data["InstanceCount"]
    if data.get("VolumeKmsKeyId") is not None:
        out["volume_kms_key_id"] = data["VolumeKmsKeyId"]
    if data.get("TransformAmiVersion") is not None:
        out["transform_ami_version"] = data["TransformAmiVersion"]
    return out
