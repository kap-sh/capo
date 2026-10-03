"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingClusterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.processing_instance_count
    import capo_sagemaker.types.processing_instance_preference_list
    import capo_sagemaker.types.processing_instance_type
    import capo_sagemaker.types.processing_volume_size_in_gb


class ProcessingClusterConfig(TypedDict, closed=True):
    instance_count: NotRequired[
        "capo_sagemaker.types.processing_instance_count.ProcessingInstanceCount"
    ]
    """<p>The number of ML compute instances to use in the processing job. For distributed processing jobs, specify a value greater than 1. The default value is 1.</p>"""
    instance_type: NotRequired[
        "capo_sagemaker.types.processing_instance_type.ProcessingInstanceType"
    ]
    """<p>The ML compute instance type for the processing job.</p>"""
    volume_size_in_gb: NotRequired[
        "capo_sagemaker.types.processing_volume_size_in_gb.ProcessingVolumeSizeInGB"
    ]
    """<p>The size of the ML storage volume in gigabytes that you want to provision. You must specify sufficient ML storage for your scenario.</p> <note> <p>Certain Nitro-based instances include local storage with a fixed total size, dependent on the instance type. When using these instances for processing, Amazon SageMaker mounts the local instance storage instead of Amazon EBS gp2 storage. You can't request a <code>VolumeSizeInGB</code> greater than the total size of the local instance storage.</p> <p>For a list of instance types that support local instance storage, including the total size per instance type, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes">Instance Store Volumes</a>.</p> </note>"""
    volume_kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the processing job. </p> <note> <p>Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You can't request a <code>VolumeKmsKeyId</code> when using an instance type with local storage.</p> <p>For a list of instance types that support local instance storage, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes">Instance Store Volumes</a>.</p> <p>For more information about local instance storage encryption, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html">SSD Instance Store Volumes</a>.</p> </note>"""
    instance_preferences: NotRequired[
        "capo_sagemaker.types.processing_instance_preference_list.ProcessingInstancePreferenceList"
    ]
    """<p>An ordered list of ML compute instance types for the processing job, in priority order. Amazon SageMaker launches the job on the first instance type in the list that has available capacity. If capacity is insufficient, Amazon SageMaker evaluates the next instance type in the list. Exactly one instance type is selected for the job.</p> <p> <code>InstancePreferences</code> is mutually exclusive with <code>InstanceType</code>.</p>"""
    selected_instance_type: NotRequired[
        "capo_sagemaker.types.processing_instance_type.ProcessingInstanceType"
    ]
    """<p>The instance type that Amazon SageMaker selected for the job from <code>InstancePreferences</code>. Returned by <code> <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeProcessingJob.html">DescribeProcessingJob</a> </code> after an instance type is selected. This field is read-only and isn't accepted in <code>CreateProcessingJob</code> requests.</p>"""
    selected_instance_count: NotRequired[
        "capo_sagemaker.types.processing_instance_count.ProcessingInstanceCount"
    ]
    """<p>The number of instances of <code>SelectedInstanceType</code> that the job launched with. The job is billed for this instance type and count. Returned by <code>DescribeProcessingJob</code> after an instance type is selected. This field is read-only and isn't accepted in <code>CreateProcessingJob</code> requests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingClusterConfig) -> dict:
    out: dict = {}
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "instance_type" in value:
        import capo_sagemaker.types.processing_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.processing_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "volume_size_in_gb" in value:
        out["VolumeSizeInGB"] = value["volume_size_in_gb"]
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    if "instance_preferences" in value:
        import capo_sagemaker.types.processing_instance_preference_list

        out["InstancePreferences"] = (
            capo_sagemaker.types.processing_instance_preference_list.serialize_aws_json_1_1(
                value["instance_preferences"]
            )
        )
    if "selected_instance_type" in value:
        import capo_sagemaker.types.processing_instance_type

        out["SelectedInstanceType"] = (
            capo_sagemaker.types.processing_instance_type.serialize_aws_json_1_1(
                value["selected_instance_type"]
            )
        )
    if "selected_instance_count" in value:
        out["SelectedInstanceCount"] = value["selected_instance_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessingClusterConfig:
    out: ProcessingClusterConfig = {}  # type: ignore[typeddict-item]
    if data.get("InstanceCount") is not None:
        out["instance_count"] = data["InstanceCount"]
    if data.get("InstanceType") is not None:
        import capo_sagemaker.types.processing_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.processing_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if data.get("VolumeSizeInGB") is not None:
        out["volume_size_in_gb"] = data["VolumeSizeInGB"]
    if data.get("VolumeKmsKeyId") is not None:
        out["volume_kms_key_id"] = data["VolumeKmsKeyId"]
    if data.get("InstancePreferences") is not None:
        import capo_sagemaker.types.processing_instance_preference_list

        out["instance_preferences"] = (
            capo_sagemaker.types.processing_instance_preference_list.deserialize_aws_json_1_1(
                data["InstancePreferences"]
            )
        )
    if data.get("SelectedInstanceType") is not None:
        import capo_sagemaker.types.processing_instance_type

        out["selected_instance_type"] = (
            capo_sagemaker.types.processing_instance_type.deserialize_aws_json_1_1(
                data["SelectedInstanceType"]
            )
        )
    if data.get("SelectedInstanceCount") is not None:
        out["selected_instance_count"] = data["SelectedInstanceCount"]
    return out
