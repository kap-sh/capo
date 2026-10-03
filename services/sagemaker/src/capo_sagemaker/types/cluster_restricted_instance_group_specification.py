"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterRestrictedInstanceGroupSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_instance_count
    import capo_sagemaker.types.cluster_instance_group_name
    import capo_sagemaker.types.cluster_instance_storage_configs
    import capo_sagemaker.types.cluster_instance_type
    import capo_sagemaker.types.cluster_threads_per_core
    import capo_sagemaker.types.environment_config
    import capo_sagemaker.types.on_start_deep_health_checks
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.scheduled_update_config
    import capo_sagemaker.types.training_plan_arn
    import capo_sagemaker.types.vpc_config


class ClusterRestrictedInstanceGroupSpecification(TypedDict, closed=True):
    instance_count: NotRequired[
        "capo_sagemaker.types.cluster_instance_count.ClusterInstanceCount"
    ]
    """<p>Specifies the number of instances to add to the restricted instance group of a SageMaker HyperPod cluster.</p>"""
    instance_group_name: NotRequired[
        "capo_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    ]
    """<p>Specifies the name of the restricted instance group.</p>"""
    instance_type: NotRequired[
        "capo_sagemaker.types.cluster_instance_type.ClusterInstanceType"
    ]
    """<p>Specifies the instance type of the restricted instance group.</p>"""
    execution_role: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>Specifies an IAM execution role to be assumed by the restricted instance group.</p>"""
    threads_per_core: NotRequired[
        "capo_sagemaker.types.cluster_threads_per_core.ClusterThreadsPerCore"
    ]
    """<p>The number you specified to <code>TreadsPerCore</code> in <code>CreateCluster</code> for enabling or disabling multithreading. For instance types that support multithreading, you can specify 1 for disabling multithreading and 2 for enabling multithreading. For more information, see the reference table of <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.html">CPU cores and threads per CPU core per instance type</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p>"""
    instance_storage_configs: NotRequired[
        "capo_sagemaker.types.cluster_instance_storage_configs.ClusterInstanceStorageConfigs"
    ]
    """<p>Specifies the additional storage configurations for the instances in the SageMaker HyperPod cluster restricted instance group.</p>"""
    on_start_deep_health_checks: NotRequired[
        "capo_sagemaker.types.on_start_deep_health_checks.OnStartDeepHealthChecks"
    ]
    """<p>A flag indicating whether deep health checks should be performed when the cluster restricted instance group is created or updated.</p>"""
    training_plan_arn: NotRequired[
        "capo_sagemaker.types.training_plan_arn.TrainingPlanArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the training plan to filter clusters by. For more information about reserving GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see <code> <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html">CreateTrainingPlan</a> </code>.</p>"""
    override_vpc_config: NotRequired["capo_sagemaker.types.vpc_config.VpcConfig"]
    scheduled_update_config: NotRequired[
        "capo_sagemaker.types.scheduled_update_config.ScheduledUpdateConfig"
    ]
    environment_config: NotRequired[
        "capo_sagemaker.types.environment_config.EnvironmentConfig"
    ]
    """<p>The configuration for the restricted instance groups (RIG) environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterRestrictedInstanceGroupSpecification) -> dict:
    out: dict = {}
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "instance_group_name" in value:
        out["InstanceGroupName"] = value["instance_group_name"]
    if "instance_type" in value:
        import capo_sagemaker.types.cluster_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.cluster_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
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
    if "training_plan_arn" in value:
        out["TrainingPlanArn"] = value["training_plan_arn"]
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
    if "environment_config" in value:
        import capo_sagemaker.types.environment_config

        out["EnvironmentConfig"] = (
            capo_sagemaker.types.environment_config.serialize_aws_json_1_1(
                value["environment_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterRestrictedInstanceGroupSpecification:
    out: ClusterRestrictedInstanceGroupSpecification = {}  # type: ignore[typeddict-item]
    if data.get("InstanceCount") is not None:
        out["instance_count"] = data["InstanceCount"]
    if data.get("InstanceGroupName") is not None:
        out["instance_group_name"] = data["InstanceGroupName"]
    if data.get("InstanceType") is not None:
        import capo_sagemaker.types.cluster_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.cluster_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
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
    if data.get("TrainingPlanArn") is not None:
        out["training_plan_arn"] = data["TrainingPlanArn"]
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
    if data.get("EnvironmentConfig") is not None:
        import capo_sagemaker.types.environment_config

        out["environment_config"] = (
            capo_sagemaker.types.environment_config.deserialize_aws_json_1_1(
                data["EnvironmentConfig"]
            )
        )
    return out
