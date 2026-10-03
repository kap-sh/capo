"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.instance_groups
    import capo_sagemaker.types.instance_placement_config
    import capo_sagemaker.types.instance_preference_list
    import capo_sagemaker.types.keep_alive_period_in_seconds
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.optional_volume_size_in_gb
    import capo_sagemaker.types.training_instance_count
    import capo_sagemaker.types.training_instance_type
    import capo_sagemaker.types.training_plan_arn


class ResourceConfig(TypedDict, closed=True):
    instance_type: NotRequired[
        "capo_sagemaker.types.training_instance_type.TrainingInstanceType"
    ]
    """<p>The ML compute instance type. </p>"""
    instance_count: NotRequired[
        "capo_sagemaker.types.training_instance_count.TrainingInstanceCount"
    ]
    """<p>The number of ML compute instances to use. For distributed training, provide a value greater than 1. </p>"""
    volume_size_in_gb: NotRequired[
        "capo_sagemaker.types.optional_volume_size_in_gb.OptionalVolumeSizeInGB"
    ]
    """<p>The size of the ML storage volume that you want to provision. </p> <p>SageMaker automatically selects the volume size for serverless training jobs. You cannot customize this setting.</p> <p>ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose <code>File</code> as the <code>TrainingInputMode</code> in the algorithm specification. </p> <p>When using an ML instance with <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#nvme-ssd-volumes">NVMe SSD volumes</a>, SageMaker doesn't provision Amazon EBS General Purpose SSD (gp2) storage. Available storage is fixed to the NVMe-type instance's storage capacity. SageMaker configures storage paths for training datasets, checkpoints, model artifacts, and outputs to use the entire capacity of the instance storage. For example, ML instance families with the NVMe-type instance storage include <code>ml.p4d</code>, <code>ml.g4dn</code>, and <code>ml.g5</code>. </p> <p>When using an ML instance with the EBS-only storage option and without instance storage, you must define the size of EBS volume through <code>VolumeSizeInGB</code> in the <code>ResourceConfig</code> API. For example, ML instance families that use EBS volumes include <code>ml.c5</code> and <code>ml.p2</code>. </p> <p>To look up instance types and their instance storage types and volumes, see <a href="http://aws.amazon.com/ec2/instance-types/">Amazon EC2 Instance Types</a>.</p> <p>To find the default local paths defined by the SageMaker training platform, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-train-storage.html">Amazon SageMaker Training Storage Folders for Training Datasets, Checkpoints, Model Artifacts, and Outputs</a>.</p>"""
    volume_kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services KMS key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job.</p> <note> <p>Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You can't request a <code>VolumeKmsKeyId</code> when using an instance type with local storage.</p> <p>For a list of instance types that support local instance storage, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes">Instance Store Volumes</a>.</p> <p>For more information about local instance storage encryption, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html">SSD Instance Store Volumes</a>.</p> </note> <p>The <code>VolumeKmsKeyId</code> can be in any of the following formats:</p> <ul> <li> <p>// KMS Key ID</p> <p> <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>// Amazon Resource Name (ARN) of a KMS Key</p> <p> <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>"""
    keep_alive_period_in_seconds: NotRequired[
        "capo_sagemaker.types.keep_alive_period_in_seconds.KeepAlivePeriodInSeconds"
    ]
    """<p>The duration of time in seconds to retain configured resources in a warm pool for subsequent training jobs.</p>"""
    instance_groups: NotRequired["capo_sagemaker.types.instance_groups.InstanceGroups"]
    """<p>The configuration of a heterogeneous cluster in JSON format.</p>"""
    training_plan_arn: NotRequired[
        "capo_sagemaker.types.training_plan_arn.TrainingPlanArn"
    ]
    """<p>The Amazon Resource Name (ARN); of the training plan to use for this resource configuration.</p>"""
    instance_placement_config: NotRequired[
        "capo_sagemaker.types.instance_placement_config.InstancePlacementConfig"
    ]
    """<p>Configuration for how training job instances are placed and allocated within UltraServers. Only applicable for UltraServer capacity.</p>"""
    instance_preferences: NotRequired[
        "capo_sagemaker.types.instance_preference_list.InstancePreferenceList"
    ]
    """<p>An ordered list of ML compute instance types for the training job, in priority order. SageMaker launches the training job on the first instance type in the list that has available capacity. If capacity is insufficient, SageMaker evaluates the next instance type in the preferred list. Exactly one instance type is selected for the job.</p> <p> <code>InstancePreferences</code> is mutually exclusive with <code>InstanceType</code>, <code>InstanceGroups</code>, <code>InstancePlacementConfig</code>, and <code>EnableManagedSpotTraining</code>, and supports only Flexible Training Plans (FTP) and On-Demand capacity.</p>"""
    selected_instance_type: NotRequired[
        "capo_sagemaker.types.training_instance_type.TrainingInstanceType"
    ]
    """<p>The instance type that SageMaker selected for the job from the provided <code>InstancePreferences</code>. The job is billed for this instance type and count. Returned by <code> <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingJob.html">DescribeTrainingJob</a> </code> after an instance type is selected. This field is read-only and isn't accepted in <code>CreateTrainingJob</code> requests.</p>"""
    selected_instance_count: NotRequired[
        "capo_sagemaker.types.training_instance_count.TrainingInstanceCount"
    ]
    """<p>The number of instances of <code>SelectedInstanceType</code> that the training job launched with. The job is billed for this instance type and count. Returned by <code>DescribeTrainingJob</code> after an instance type is selected. This field is read-only and isn't accepted in <code>CreateTrainingJob</code> requests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceConfig) -> dict:
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
    if "keep_alive_period_in_seconds" in value:
        out["KeepAlivePeriodInSeconds"] = value["keep_alive_period_in_seconds"]
    if "instance_groups" in value:
        import capo_sagemaker.types.instance_groups

        out["InstanceGroups"] = (
            capo_sagemaker.types.instance_groups.serialize_aws_json_1_1(
                value["instance_groups"]
            )
        )
    if "training_plan_arn" in value:
        out["TrainingPlanArn"] = value["training_plan_arn"]
    if "instance_placement_config" in value:
        import capo_sagemaker.types.instance_placement_config

        out["InstancePlacementConfig"] = (
            capo_sagemaker.types.instance_placement_config.serialize_aws_json_1_1(
                value["instance_placement_config"]
            )
        )
    if "instance_preferences" in value:
        import capo_sagemaker.types.instance_preference_list

        out["InstancePreferences"] = (
            capo_sagemaker.types.instance_preference_list.serialize_aws_json_1_1(
                value["instance_preferences"]
            )
        )
    if "selected_instance_type" in value:
        import capo_sagemaker.types.training_instance_type

        out["SelectedInstanceType"] = (
            capo_sagemaker.types.training_instance_type.serialize_aws_json_1_1(
                value["selected_instance_type"]
            )
        )
    if "selected_instance_count" in value:
        out["SelectedInstanceCount"] = value["selected_instance_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceConfig:
    out: ResourceConfig = {}  # type: ignore[typeddict-item]
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
    if data.get("KeepAlivePeriodInSeconds") is not None:
        out["keep_alive_period_in_seconds"] = data["KeepAlivePeriodInSeconds"]
    if data.get("InstanceGroups") is not None:
        import capo_sagemaker.types.instance_groups

        out["instance_groups"] = (
            capo_sagemaker.types.instance_groups.deserialize_aws_json_1_1(
                data["InstanceGroups"]
            )
        )
    if data.get("TrainingPlanArn") is not None:
        out["training_plan_arn"] = data["TrainingPlanArn"]
    if data.get("InstancePlacementConfig") is not None:
        import capo_sagemaker.types.instance_placement_config

        out["instance_placement_config"] = (
            capo_sagemaker.types.instance_placement_config.deserialize_aws_json_1_1(
                data["InstancePlacementConfig"]
            )
        )
    if data.get("InstancePreferences") is not None:
        import capo_sagemaker.types.instance_preference_list

        out["instance_preferences"] = (
            capo_sagemaker.types.instance_preference_list.deserialize_aws_json_1_1(
                data["InstancePreferences"]
            )
        )
    if data.get("SelectedInstanceType") is not None:
        import capo_sagemaker.types.training_instance_type

        out["selected_instance_type"] = (
            capo_sagemaker.types.training_instance_type.deserialize_aws_json_1_1(
                data["SelectedInstanceType"]
            )
        )
    if data.get("SelectedInstanceCount") is not None:
        out["selected_instance_count"] = data["SelectedInstanceCount"]
    return out
