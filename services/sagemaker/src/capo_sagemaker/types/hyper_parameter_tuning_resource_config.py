"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningResourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hyper_parameter_tuning_allocation_strategy
    import capo_sagemaker.types.hyper_parameter_tuning_instance_configs
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.optional_volume_size_in_gb
    import capo_sagemaker.types.training_instance_count
    import capo_sagemaker.types.training_instance_type


class HyperParameterTuningResourceConfig(TypedDict, closed=True):
    instance_type: NotRequired[
        "capo_sagemaker.types.training_instance_type.TrainingInstanceType"
    ]
    """<p>The instance type used to run hyperparameter optimization tuning jobs. See <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-instance-types.html"> descriptions of instance types</a> for more information.</p>"""
    instance_count: NotRequired[
        "capo_sagemaker.types.training_instance_count.TrainingInstanceCount"
    ]
    """<p>The number of compute instances of type <code>InstanceType</code> to use. For <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-use-api.html">distributed training</a>, select a value greater than 1.</p>"""
    volume_size_in_gb: NotRequired[
        "capo_sagemaker.types.optional_volume_size_in_gb.OptionalVolumeSizeInGB"
    ]
    """<p>The volume size in GB for the storage volume to be used in processing hyperparameter optimization jobs (optional). These volumes store model artifacts, incremental states and optionally, scratch space for training algorithms. Do not provide a value for this parameter if a value for <code>InstanceConfigs</code> is also specified.</p> <p>Some instance types have a fixed total local storage size. If you select one of these instances for training, <code>VolumeSizeInGB</code> cannot be greater than this total size. For a list of instance types with local instance storage and their sizes, see <a href="http://aws.amazon.com/releasenotes/host-instance-storage-volumes-table/">instance store volumes</a>.</p> <note> <p>SageMaker supports only the <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html">General Purpose SSD (gp2)</a> storage volume type.</p> </note>"""
    volume_kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>A key used by Amazon Web Services Key Management Service to encrypt data on the storage volume attached to the compute instances used to run the training job. You can use either of the following formats to specify a key.</p> <p>KMS Key ID:</p> <p> <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> <p>Amazon Resource Name (ARN) of a KMS key:</p> <p> <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> <p>Some instances use local storage, which use a <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html">hardware module to encrypt</a> storage volumes. If you choose one of these instance types, you cannot request a <code>VolumeKmsKeyId</code>. For a list of instance types that use local storage, see <a href="http://aws.amazon.com/releasenotes/host-instance-storage-volumes-table/">instance store volumes</a>. For more information about Amazon Web Services Key Management Service, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-kms-permissions.html">KMS encryption</a> for more information.</p>"""
    allocation_strategy: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_allocation_strategy.HyperParameterTuningAllocationStrategy"
    ]
    """<p>The strategy that determines the order of preference for resources specified in <code>InstanceConfigs</code> used in hyperparameter optimization.</p>"""
    instance_configs: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_instance_configs.HyperParameterTuningInstanceConfigs"
    ]
    """<p>A list containing the configuration(s) for one or more resources for processing hyperparameter jobs. These resources include compute instances and storage volumes to use in model training jobs launched by hyperparameter tuning jobs. The <code>AllocationStrategy</code> controls the order in which multiple configurations provided in <code>InstanceConfigs</code> are used.</p> <note> <p>If you only want to use a single instance configuration inside the <code>HyperParameterTuningResourceConfig</code> API, do not provide a value for <code>InstanceConfigs</code>. Instead, use <code>InstanceType</code>, <code>VolumeSizeInGB</code> and <code>InstanceCount</code>. If you use <code>InstanceConfigs</code>, do not provide values for <code>InstanceType</code>, <code>VolumeSizeInGB</code> or <code>InstanceCount</code>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningResourceConfig) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import capo_sagemaker.types.training_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.training_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "volume_size_in_gb" in value:
        out["VolumeSizeInGB"] = value["volume_size_in_gb"]
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    if "allocation_strategy" in value:
        import capo_sagemaker.types.hyper_parameter_tuning_allocation_strategy

        out["AllocationStrategy"] = (
            capo_sagemaker.types.hyper_parameter_tuning_allocation_strategy.serialize_aws_json_1_1(
                value["allocation_strategy"]
            )
        )
    if "instance_configs" in value:
        import capo_sagemaker.types.hyper_parameter_tuning_instance_configs

        out["InstanceConfigs"] = (
            capo_sagemaker.types.hyper_parameter_tuning_instance_configs.serialize_aws_json_1_1(
                value["instance_configs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterTuningResourceConfig:
    out: HyperParameterTuningResourceConfig = {}  # type: ignore[typeddict-item]
    if data.get("InstanceType") is not None:
        import capo_sagemaker.types.training_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.training_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if data.get("InstanceCount") is not None:
        out["instance_count"] = data["InstanceCount"]
    if data.get("VolumeSizeInGB") is not None:
        out["volume_size_in_gb"] = data["VolumeSizeInGB"]
    if data.get("VolumeKmsKeyId") is not None:
        out["volume_kms_key_id"] = data["VolumeKmsKeyId"]
    if data.get("AllocationStrategy") is not None:
        import capo_sagemaker.types.hyper_parameter_tuning_allocation_strategy

        out["allocation_strategy"] = (
            capo_sagemaker.types.hyper_parameter_tuning_allocation_strategy.deserialize_aws_json_1_1(
                data["AllocationStrategy"]
            )
        )
    if data.get("InstanceConfigs") is not None:
        import capo_sagemaker.types.hyper_parameter_tuning_instance_configs

        out["instance_configs"] = (
            capo_sagemaker.types.hyper_parameter_tuning_instance_configs.deserialize_aws_json_1_1(
                data["InstanceConfigs"]
            )
        )
    return out
