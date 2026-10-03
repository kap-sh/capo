"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.active_operations
    import capo_sagemaker.types.cluster_auto_patch_config_details
    import capo_sagemaker.types.cluster_capacity_requirements
    import capo_sagemaker.types.cluster_image_version_status
    import capo_sagemaker.types.cluster_instance_count
    import capo_sagemaker.types.cluster_instance_group_name
    import capo_sagemaker.types.cluster_instance_requirement_details
    import capo_sagemaker.types.cluster_instance_storage_configs
    import capo_sagemaker.types.cluster_instance_type
    import capo_sagemaker.types.cluster_instance_type_details
    import capo_sagemaker.types.cluster_kubernetes_config_details
    import capo_sagemaker.types.cluster_life_cycle_config
    import capo_sagemaker.types.cluster_network_interface_details
    import capo_sagemaker.types.cluster_non_negative_instance_count
    import capo_sagemaker.types.cluster_slurm_config_details
    import capo_sagemaker.types.cluster_threads_per_core
    import capo_sagemaker.types.deployment_configuration
    import capo_sagemaker.types.image_id
    import capo_sagemaker.types.image_release_version
    import capo_sagemaker.types.instance_group_status
    import capo_sagemaker.types.instance_group_training_plan_status
    import capo_sagemaker.types.on_start_deep_health_checks
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.scheduled_update_config
    import capo_sagemaker.types.software_update_status
    import capo_sagemaker.types.training_plan_arn
    import capo_sagemaker.types.vpc_config


class ClusterInstanceGroupDetails(TypedDict, closed=True):
    current_count: NotRequired[
        "capo_sagemaker.types.cluster_non_negative_instance_count.ClusterNonNegativeInstanceCount"
    ]
    """<p>The number of instances that are currently in the instance group of a SageMaker HyperPod cluster.</p>"""
    target_count: NotRequired[
        "capo_sagemaker.types.cluster_instance_count.ClusterInstanceCount"
    ]
    """<p>The number of instances you specified to add to the instance group of a SageMaker HyperPod cluster.</p>"""
    min_count: NotRequired[
        "capo_sagemaker.types.cluster_instance_count.ClusterInstanceCount"
    ]
    """<p>The minimum number of instances that must be available in the instance group of a SageMaker HyperPod cluster before it transitions to <code>InService</code> status. </p>"""
    instance_group_name: NotRequired[
        "capo_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    ]
    """<p>The name of the instance group of a SageMaker HyperPod cluster.</p>"""
    instance_type: NotRequired[
        "capo_sagemaker.types.cluster_instance_type.ClusterInstanceType"
    ]
    """<p>The instance type of the instance group of a SageMaker HyperPod cluster.</p>"""
    instance_requirements: NotRequired[
        "capo_sagemaker.types.cluster_instance_requirement_details.ClusterInstanceRequirementDetails"
    ]
    """<p>The instance requirements for the instance group, including the current and desired instance types. This field is present for flexible instance groups that support multiple instance types.</p>"""
    instance_type_details: NotRequired[
        "capo_sagemaker.types.cluster_instance_type_details.ClusterInstanceTypeDetails"
    ]
    """<p>Details about the instance types in the instance group, including the count and configuration of each instance type. This field is present for flexible instance groups that support multiple instance types.</p>"""
    life_cycle_config: NotRequired[
        "capo_sagemaker.types.cluster_life_cycle_config.ClusterLifeCycleConfig"
    ]
    """<p>Details of LifeCycle configuration for the instance group.</p>"""
    execution_role: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The execution role for the instance group to assume.</p>"""
    threads_per_core: NotRequired[
        "capo_sagemaker.types.cluster_threads_per_core.ClusterThreadsPerCore"
    ]
    """<p>The number you specified to <code>TreadsPerCore</code> in <code>CreateCluster</code> for enabling or disabling multithreading. For instance types that support multithreading, you can specify 1 for disabling multithreading and 2 for enabling multithreading. For more information, see the reference table of <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.html">CPU cores and threads per CPU core per instance type</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p>"""
    instance_storage_configs: NotRequired[
        "capo_sagemaker.types.cluster_instance_storage_configs.ClusterInstanceStorageConfigs"
    ]
    """<p>The additional storage configurations for the instances in the SageMaker HyperPod cluster instance group.</p>"""
    on_start_deep_health_checks: NotRequired[
        "capo_sagemaker.types.on_start_deep_health_checks.OnStartDeepHealthChecks"
    ]
    """<p>A flag indicating whether deep health checks should be performed when the cluster instance group is created or updated.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.instance_group_status.InstanceGroupStatus"
    ]
    """<p>The current status of the cluster instance group.</p> <ul> <li> <p> <code>InService</code>: The instance group is active and healthy.</p> </li> <li> <p> <code>Creating</code>: The instance group is being provisioned.</p> </li> <li> <p> <code>Updating</code>: The instance group is being updated.</p> </li> <li> <p> <code>Failed</code>: The instance group has failed to provision or is no longer healthy.</p> </li> <li> <p> <code>Degraded</code>: The instance group is degraded, meaning that some instances have failed to provision or are no longer healthy.</p> </li> <li> <p> <code>Deleting</code>: The instance group is being deleted.</p> </li> </ul>"""
    training_plan_arn: NotRequired[
        "capo_sagemaker.types.training_plan_arn.TrainingPlanArn"
    ]
    """<p>The Amazon Resource Name (ARN); of the training plan associated with this cluster instance group.</p> <p>For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see <code> <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html">CreateTrainingPlan</a> </code>.</p>"""
    training_plan_status: NotRequired[
        "capo_sagemaker.types.instance_group_training_plan_status.InstanceGroupTrainingPlanStatus"
    ]
    """<p>The current status of the training plan associated with this cluster instance group.</p>"""
    override_vpc_config: NotRequired["capo_sagemaker.types.vpc_config.VpcConfig"]
    """<p>The customized Amazon VPC configuration at the instance group level that overrides the default Amazon VPC configuration of the SageMaker HyperPod cluster.</p>"""
    scheduled_update_config: NotRequired[
        "capo_sagemaker.types.scheduled_update_config.ScheduledUpdateConfig"
    ]
    """<p>The configuration object of the schedule that SageMaker follows when updating the AMI.</p>"""
    auto_patch_config: NotRequired[
        "capo_sagemaker.types.cluster_auto_patch_config_details.ClusterAutoPatchConfigDetails"
    ]
    """<p>The auto-patching configuration for the instance group, including the current patching strategy and next scheduled patch date.</p>"""
    current_image_id: NotRequired["capo_sagemaker.types.image_id.ImageId"]
    """<p>The ID of the Amazon Machine Image (AMI) currently in use by the instance group.</p>"""
    desired_image_id: NotRequired["capo_sagemaker.types.image_id.ImageId"]
    """<p>The ID of the Amazon Machine Image (AMI) desired for the instance group.</p>"""
    current_image_release_version: NotRequired[
        "capo_sagemaker.types.image_release_version.ImageReleaseVersion"
    ]
    """<p>The version of the HyperPod-managed AMI currently running on the instance group.</p>"""
    desired_image_release_version: NotRequired[
        "capo_sagemaker.types.image_release_version.ImageReleaseVersion"
    ]
    """<p>The desired version of the HyperPod-managed AMI for the instance group. This may differ from the current version when an update is pending.</p>"""
    image_version_status: NotRequired[
        "capo_sagemaker.types.cluster_image_version_status.ClusterImageVersionStatus"
    ]
    """<p>The status of the image version for the instance group. Indicates whether the instance group is running the latest image version or if an update is available.</p>"""
    active_operations: NotRequired[
        "capo_sagemaker.types.active_operations.ActiveOperations"
    ]
    """<p>A map indicating active operations currently in progress for the instance group of a SageMaker HyperPod cluster. When there is a scaling operation in progress, this map contains a key <code>Scaling</code> with value 1. </p>"""
    kubernetes_config: NotRequired[
        "capo_sagemaker.types.cluster_kubernetes_config_details.ClusterKubernetesConfigDetails"
    ]
    """<p>The Kubernetes configuration for the instance group that contains labels and taints to be applied for the nodes in this instance group. </p>"""
    capacity_requirements: NotRequired[
        "capo_sagemaker.types.cluster_capacity_requirements.ClusterCapacityRequirements"
    ]
    """<p>The instance capacity requirements for the instance group.</p>"""
    target_state_count: NotRequired[
        "capo_sagemaker.types.cluster_instance_count.ClusterInstanceCount"
    ]
    """<p>Represents the number of running nodes using the desired Image ID.</p> <ol> <li> <p> <b>During software update operations:</b> This count shows the number of nodes running on the desired Image ID. If a rollback occurs, the current image ID and desired image ID (both included in the describe cluster response) swap values. The TargetStateCount then shows the number of nodes running on the newly designated desired image ID (which was previously the current image ID).</p> </li> <li> <p> <b>During simultaneous scaling and software update operations:</b> This count shows the number of instances running on the desired image ID, including any new instances created as part of the scaling request. New nodes are always created using the desired image ID, so TargetStateCount reflects the total count of nodes running on the desired image ID, even during rollback scenarios.</p> </li> </ol>"""
    software_update_status: NotRequired[
        "capo_sagemaker.types.software_update_status.SoftwareUpdateStatus"
    ]
    """<p>Status of the last software udpate request.</p> <p>Status transitions follow these possible sequences:</p> <ul> <li> <p>Pending -&gt; InProgress -&gt; Succeeded</p> </li> <li> <p>Pending -&gt; InProgress -&gt; RollbackInProgress -&gt; RollbackComplete</p> </li> <li> <p>Pending -&gt; InProgress -&gt; RollbackInProgress -&gt; Failed</p> </li> </ul>"""
    active_software_update_config: NotRequired[
        "capo_sagemaker.types.deployment_configuration.DeploymentConfiguration"
    ]
    slurm_config: NotRequired[
        "capo_sagemaker.types.cluster_slurm_config_details.ClusterSlurmConfigDetails"
    ]
    """<p>The Slurm configuration for the instance group.</p>"""
    network_interface: NotRequired[
        "capo_sagemaker.types.cluster_network_interface_details.ClusterNetworkInterfaceDetails"
    ]
    """<p>The network interface configuration for the instance group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstanceGroupDetails) -> dict:
    out: dict = {}
    if "current_count" in value:
        out["CurrentCount"] = value["current_count"]
    if "target_count" in value:
        out["TargetCount"] = value["target_count"]
    if "min_count" in value:
        out["MinCount"] = value["min_count"]
    if "instance_group_name" in value:
        out["InstanceGroupName"] = value["instance_group_name"]
    if "instance_type" in value:
        import capo_sagemaker.types.cluster_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.cluster_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "instance_requirements" in value:
        import capo_sagemaker.types.cluster_instance_requirement_details

        out["InstanceRequirements"] = (
            capo_sagemaker.types.cluster_instance_requirement_details.serialize_aws_json_1_1(
                value["instance_requirements"]
            )
        )
    if "instance_type_details" in value:
        import capo_sagemaker.types.cluster_instance_type_details

        out["InstanceTypeDetails"] = (
            capo_sagemaker.types.cluster_instance_type_details.serialize_aws_json_1_1(
                value["instance_type_details"]
            )
        )
    if "life_cycle_config" in value:
        import capo_sagemaker.types.cluster_life_cycle_config

        out["LifeCycleConfig"] = (
            capo_sagemaker.types.cluster_life_cycle_config.serialize_aws_json_1_1(
                value["life_cycle_config"]
            )
        )
    if "execution_role" in value:
        out["ExecutionRole"] = value["execution_role"]
    if "threads_per_core" in value:
        out["ThreadsPerCore"] = value["threads_per_core"]
    if "instance_storage_configs" in value:
        import capo_sagemaker.types.cluster_instance_storage_configs

        out["InstanceStorageConfigs"] = (
            capo_sagemaker.types.cluster_instance_storage_configs.serialize_aws_json_1_1(
                value["instance_storage_configs"]
            )
        )
    if "on_start_deep_health_checks" in value:
        import capo_sagemaker.types.on_start_deep_health_checks

        out["OnStartDeepHealthChecks"] = (
            capo_sagemaker.types.on_start_deep_health_checks.serialize_aws_json_1_1(
                value["on_start_deep_health_checks"]
            )
        )
    if "status" in value:
        import capo_sagemaker.types.instance_group_status

        out["Status"] = (
            capo_sagemaker.types.instance_group_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "training_plan_arn" in value:
        out["TrainingPlanArn"] = value["training_plan_arn"]
    if "training_plan_status" in value:
        out["TrainingPlanStatus"] = value["training_plan_status"]
    if "override_vpc_config" in value:
        import capo_sagemaker.types.vpc_config

        out["OverrideVpcConfig"] = (
            capo_sagemaker.types.vpc_config.serialize_aws_json_1_1(
                value["override_vpc_config"]
            )
        )
    if "scheduled_update_config" in value:
        import capo_sagemaker.types.scheduled_update_config

        out["ScheduledUpdateConfig"] = (
            capo_sagemaker.types.scheduled_update_config.serialize_aws_json_1_1(
                value["scheduled_update_config"]
            )
        )
    if "auto_patch_config" in value:
        import capo_sagemaker.types.cluster_auto_patch_config_details

        out["AutoPatchConfig"] = (
            capo_sagemaker.types.cluster_auto_patch_config_details.serialize_aws_json_1_1(
                value["auto_patch_config"]
            )
        )
    if "current_image_id" in value:
        out["CurrentImageId"] = value["current_image_id"]
    if "desired_image_id" in value:
        out["DesiredImageId"] = value["desired_image_id"]
    if "current_image_release_version" in value:
        out["CurrentImageReleaseVersion"] = value["current_image_release_version"]
    if "desired_image_release_version" in value:
        out["DesiredImageReleaseVersion"] = value["desired_image_release_version"]
    if "image_version_status" in value:
        import capo_sagemaker.types.cluster_image_version_status

        out["ImageVersionStatus"] = (
            capo_sagemaker.types.cluster_image_version_status.serialize_aws_json_1_1(
                value["image_version_status"]
            )
        )
    if "active_operations" in value:
        import capo_sagemaker.types.active_operations

        out["ActiveOperations"] = (
            capo_sagemaker.types.active_operations.serialize_aws_json_1_1(
                value["active_operations"]
            )
        )
    if "kubernetes_config" in value:
        import capo_sagemaker.types.cluster_kubernetes_config_details

        out["KubernetesConfig"] = (
            capo_sagemaker.types.cluster_kubernetes_config_details.serialize_aws_json_1_1(
                value["kubernetes_config"]
            )
        )
    if "capacity_requirements" in value:
        import capo_sagemaker.types.cluster_capacity_requirements

        out["CapacityRequirements"] = (
            capo_sagemaker.types.cluster_capacity_requirements.serialize_aws_json_1_1(
                value["capacity_requirements"]
            )
        )
    if "target_state_count" in value:
        out["TargetStateCount"] = value["target_state_count"]
    if "software_update_status" in value:
        import capo_sagemaker.types.software_update_status

        out["SoftwareUpdateStatus"] = (
            capo_sagemaker.types.software_update_status.serialize_aws_json_1_1(
                value["software_update_status"]
            )
        )
    if "active_software_update_config" in value:
        import capo_sagemaker.types.deployment_configuration

        out["ActiveSoftwareUpdateConfig"] = (
            capo_sagemaker.types.deployment_configuration.serialize_aws_json_1_1(
                value["active_software_update_config"]
            )
        )
    if "slurm_config" in value:
        import capo_sagemaker.types.cluster_slurm_config_details

        out["SlurmConfig"] = (
            capo_sagemaker.types.cluster_slurm_config_details.serialize_aws_json_1_1(
                value["slurm_config"]
            )
        )
    if "network_interface" in value:
        import capo_sagemaker.types.cluster_network_interface_details

        out["NetworkInterface"] = (
            capo_sagemaker.types.cluster_network_interface_details.serialize_aws_json_1_1(
                value["network_interface"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterInstanceGroupDetails:
    out: ClusterInstanceGroupDetails = {}  # type: ignore[typeddict-item]
    if data.get("CurrentCount") is not None:
        out["current_count"] = data["CurrentCount"]
    if data.get("TargetCount") is not None:
        out["target_count"] = data["TargetCount"]
    if data.get("MinCount") is not None:
        out["min_count"] = data["MinCount"]
    if data.get("InstanceGroupName") is not None:
        out["instance_group_name"] = data["InstanceGroupName"]
    if data.get("InstanceType") is not None:
        import capo_sagemaker.types.cluster_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.cluster_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if data.get("InstanceRequirements") is not None:
        import capo_sagemaker.types.cluster_instance_requirement_details

        out["instance_requirements"] = (
            capo_sagemaker.types.cluster_instance_requirement_details.deserialize_aws_json_1_1(
                data["InstanceRequirements"]
            )
        )
    if data.get("InstanceTypeDetails") is not None:
        import capo_sagemaker.types.cluster_instance_type_details

        out["instance_type_details"] = (
            capo_sagemaker.types.cluster_instance_type_details.deserialize_aws_json_1_1(
                data["InstanceTypeDetails"]
            )
        )
    if data.get("LifeCycleConfig") is not None:
        import capo_sagemaker.types.cluster_life_cycle_config

        out["life_cycle_config"] = (
            capo_sagemaker.types.cluster_life_cycle_config.deserialize_aws_json_1_1(
                data["LifeCycleConfig"]
            )
        )
    if data.get("ExecutionRole") is not None:
        out["execution_role"] = data["ExecutionRole"]
    if data.get("ThreadsPerCore") is not None:
        out["threads_per_core"] = data["ThreadsPerCore"]
    if data.get("InstanceStorageConfigs") is not None:
        import capo_sagemaker.types.cluster_instance_storage_configs

        out["instance_storage_configs"] = (
            capo_sagemaker.types.cluster_instance_storage_configs.deserialize_aws_json_1_1(
                data["InstanceStorageConfigs"]
            )
        )
    if data.get("OnStartDeepHealthChecks") is not None:
        import capo_sagemaker.types.on_start_deep_health_checks

        out["on_start_deep_health_checks"] = (
            capo_sagemaker.types.on_start_deep_health_checks.deserialize_aws_json_1_1(
                data["OnStartDeepHealthChecks"]
            )
        )
    if data.get("Status") is not None:
        import capo_sagemaker.types.instance_group_status

        out["status"] = (
            capo_sagemaker.types.instance_group_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("TrainingPlanArn") is not None:
        out["training_plan_arn"] = data["TrainingPlanArn"]
    if data.get("TrainingPlanStatus") is not None:
        out["training_plan_status"] = data["TrainingPlanStatus"]
    if data.get("OverrideVpcConfig") is not None:
        import capo_sagemaker.types.vpc_config

        out["override_vpc_config"] = (
            capo_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
                data["OverrideVpcConfig"]
            )
        )
    if data.get("ScheduledUpdateConfig") is not None:
        import capo_sagemaker.types.scheduled_update_config

        out["scheduled_update_config"] = (
            capo_sagemaker.types.scheduled_update_config.deserialize_aws_json_1_1(
                data["ScheduledUpdateConfig"]
            )
        )
    if data.get("AutoPatchConfig") is not None:
        import capo_sagemaker.types.cluster_auto_patch_config_details

        out["auto_patch_config"] = (
            capo_sagemaker.types.cluster_auto_patch_config_details.deserialize_aws_json_1_1(
                data["AutoPatchConfig"]
            )
        )
    if data.get("CurrentImageId") is not None:
        out["current_image_id"] = data["CurrentImageId"]
    if data.get("DesiredImageId") is not None:
        out["desired_image_id"] = data["DesiredImageId"]
    if data.get("CurrentImageReleaseVersion") is not None:
        out["current_image_release_version"] = data["CurrentImageReleaseVersion"]
    if data.get("DesiredImageReleaseVersion") is not None:
        out["desired_image_release_version"] = data["DesiredImageReleaseVersion"]
    if data.get("ImageVersionStatus") is not None:
        import capo_sagemaker.types.cluster_image_version_status

        out["image_version_status"] = (
            capo_sagemaker.types.cluster_image_version_status.deserialize_aws_json_1_1(
                data["ImageVersionStatus"]
            )
        )
    if data.get("ActiveOperations") is not None:
        import capo_sagemaker.types.active_operations

        out["active_operations"] = (
            capo_sagemaker.types.active_operations.deserialize_aws_json_1_1(
                data["ActiveOperations"]
            )
        )
    if data.get("KubernetesConfig") is not None:
        import capo_sagemaker.types.cluster_kubernetes_config_details

        out["kubernetes_config"] = (
            capo_sagemaker.types.cluster_kubernetes_config_details.deserialize_aws_json_1_1(
                data["KubernetesConfig"]
            )
        )
    if data.get("CapacityRequirements") is not None:
        import capo_sagemaker.types.cluster_capacity_requirements

        out["capacity_requirements"] = (
            capo_sagemaker.types.cluster_capacity_requirements.deserialize_aws_json_1_1(
                data["CapacityRequirements"]
            )
        )
    if data.get("TargetStateCount") is not None:
        out["target_state_count"] = data["TargetStateCount"]
    if data.get("SoftwareUpdateStatus") is not None:
        import capo_sagemaker.types.software_update_status

        out["software_update_status"] = (
            capo_sagemaker.types.software_update_status.deserialize_aws_json_1_1(
                data["SoftwareUpdateStatus"]
            )
        )
    if data.get("ActiveSoftwareUpdateConfig") is not None:
        import capo_sagemaker.types.deployment_configuration

        out["active_software_update_config"] = (
            capo_sagemaker.types.deployment_configuration.deserialize_aws_json_1_1(
                data["ActiveSoftwareUpdateConfig"]
            )
        )
    if data.get("SlurmConfig") is not None:
        import capo_sagemaker.types.cluster_slurm_config_details

        out["slurm_config"] = (
            capo_sagemaker.types.cluster_slurm_config_details.deserialize_aws_json_1_1(
                data["SlurmConfig"]
            )
        )
    if data.get("NetworkInterface") is not None:
        import capo_sagemaker.types.cluster_network_interface_details

        out["network_interface"] = (
            capo_sagemaker.types.cluster_network_interface_details.deserialize_aws_json_1_1(
                data["NetworkInterface"]
            )
        )
    return out
