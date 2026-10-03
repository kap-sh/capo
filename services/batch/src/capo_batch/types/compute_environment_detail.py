"""Generated from Smithy shape ``com.amazonaws.batch#ComputeEnvironmentDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.ce_state
    import capo_batch.types.ce_status
    import capo_batch.types.ce_type
    import capo_batch.types.compute_resource
    import capo_batch.types.ecs_settings
    import capo_batch.types.eks_configuration
    import capo_batch.types.integer
    import capo_batch.types.orchestration_type
    import capo_batch.types.string
    import capo_batch.types.tagris_tags_map
    import capo_batch.types.update_policy


class ComputeEnvironmentDetail(TypedDict, closed=True):
    compute_environment_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the compute environment. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>"""
    compute_environment_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the compute environment.</p>"""
    unmanagedv_cpus: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The maximum number of VCPUs expected to be used for an unmanaged compute environment.</p>"""
    ecs_cluster_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster that the compute environment uses.</p>"""
    tags: NotRequired["capo_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The tags applied to the compute environment.</p>"""
    type: NotRequired["capo_batch.types.ce_type.CEType"]
    """<p>The type of the compute environment: <code>MANAGED</code> or <code>UNMANAGED</code>. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html">Compute environments</a> in the <i>Batch User Guide</i>.</p>"""
    state: NotRequired["capo_batch.types.ce_state.CEState"]
    """<p>The state of the compute environment. The valid values are <code>ENABLED</code> or <code>DISABLED</code>.</p> <p>If the state is <code>ENABLED</code>, then the Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically based on the job queue demand.</p> <p>If the state is <code>DISABLED</code>, then the Batch scheduler doesn't attempt to place jobs within the environment. Jobs in a <code>STARTING</code> or <code>RUNNING</code> state continue to progress normally. Managed compute environments in the <code>DISABLED</code> state don't scale out. </p> <note> <p>Compute environments in a <code>DISABLED</code> state may continue to incur billing charges, for example, if they have running instances due to jobs that are still executing or a non-zero <code>minvCpus</code> setting. To prevent additional charges, disable and delete the compute environment.</p> </note> <p>When an instance is idle, the instance scales down to the <code>minvCpus</code> value. However, the instance size doesn't change. For example, consider a <code>c5.8xlarge</code> instance with a <code>minvCpus</code> value of <code>4</code> and a <code>desiredvCpus</code> value of <code>36</code>. This instance doesn't scale down to a <code>c5.large</code> instance.</p>"""
    status: NotRequired["capo_batch.types.ce_status.CEStatus"]
    """<p>The current status of the compute environment (for example, <code>CREATING</code> or <code>VALID</code>).</p>"""
    status_reason: NotRequired["capo_batch.types.string.String"]
    """<p>A short, human-readable string to provide additional details for the current status of the compute environment.</p>"""
    compute_resources: NotRequired["capo_batch.types.compute_resource.ComputeResource"]
    """<p>The compute resources defined for the compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html">Compute environments</a> in the <i>Batch User Guide</i>.</p>"""
    service_role: NotRequired["capo_batch.types.string.String"]
    """<p>The service role that's associated with the compute environment that allows Batch to make calls to Amazon Web Services API operations on your behalf. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html">Batch service IAM role</a> in the <i>Batch User Guide</i>.</p>"""
    update_policy: NotRequired["capo_batch.types.update_policy.UpdatePolicy"]
    """<p>Specifies the infrastructure update policy for the compute environment. For more information about infrastructure updates, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p>"""
    eks_configuration: NotRequired[
        "capo_batch.types.eks_configuration.EksConfiguration"
    ]
    """<p>The configuration for the Amazon EKS cluster that supports the Batch compute environment. Only specify this parameter if the <code>containerOrchestrationType</code> is <code>EKS</code>.</p>"""
    container_orchestration_type: NotRequired[
        "capo_batch.types.orchestration_type.OrchestrationType"
    ]
    """<p>The orchestration type of the compute environment. The valid values are <code>ECS</code> (default) or <code>EKS</code>.</p>"""
    uuid: NotRequired["capo_batch.types.string.String"]
    """<p>Unique identifier for the compute environment.</p>"""
    context: NotRequired["capo_batch.types.string.String"]
    """<p>Reserved.</p>"""
    ecs_settings: NotRequired["capo_batch.types.ecs_settings.EcsSettings"]
    """<p>The Amazon ECS settings for the compute environment. These settings control CloudWatch Container Insights collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputeEnvironmentDetail) -> dict:
    out: dict = {}
    if "compute_environment_name" in value:
        out["computeEnvironmentName"] = value["compute_environment_name"]
    if "compute_environment_arn" in value:
        out["computeEnvironmentArn"] = value["compute_environment_arn"]
    if "unmanagedv_cpus" in value:
        out["unmanagedvCpus"] = value["unmanagedv_cpus"]
    if "ecs_cluster_arn" in value:
        out["ecsClusterArn"] = value["ecs_cluster_arn"]
    if "tags" in value:
        import capo_batch.types.tagris_tags_map

        out["tags"] = capo_batch.types.tagris_tags_map.serialize_json(value["tags"])
    if "type" in value:
        import capo_batch.types.ce_type

        out["type"] = capo_batch.types.ce_type.serialize_json(value["type"])
    if "state" in value:
        import capo_batch.types.ce_state

        out["state"] = capo_batch.types.ce_state.serialize_json(value["state"])
    if "status" in value:
        import capo_batch.types.ce_status

        out["status"] = capo_batch.types.ce_status.serialize_json(value["status"])
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "compute_resources" in value:
        import capo_batch.types.compute_resource

        out["computeResources"] = capo_batch.types.compute_resource.serialize_json(
            value["compute_resources"]
        )
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "update_policy" in value:
        import capo_batch.types.update_policy

        out["updatePolicy"] = capo_batch.types.update_policy.serialize_json(
            value["update_policy"]
        )
    if "eks_configuration" in value:
        import capo_batch.types.eks_configuration

        out["eksConfiguration"] = capo_batch.types.eks_configuration.serialize_json(
            value["eks_configuration"]
        )
    if "container_orchestration_type" in value:
        import capo_batch.types.orchestration_type

        out["containerOrchestrationType"] = (
            capo_batch.types.orchestration_type.serialize_json(
                value["container_orchestration_type"]
            )
        )
    if "uuid" in value:
        out["uuid"] = value["uuid"]
    if "context" in value:
        out["context"] = value["context"]
    if "ecs_settings" in value:
        import capo_batch.types.ecs_settings

        out["ecsSettings"] = capo_batch.types.ecs_settings.serialize_json(
            value["ecs_settings"]
        )
    return out


def deserialize_json(data: dict) -> ComputeEnvironmentDetail:
    out: ComputeEnvironmentDetail = {}  # type: ignore[typeddict-item]
    if data.get("computeEnvironmentName") is not None:
        out["compute_environment_name"] = data["computeEnvironmentName"]
    if data.get("computeEnvironmentArn") is not None:
        out["compute_environment_arn"] = data["computeEnvironmentArn"]
    if data.get("unmanagedvCpus") is not None:
        out["unmanagedv_cpus"] = data["unmanagedvCpus"]
    if data.get("ecsClusterArn") is not None:
        out["ecs_cluster_arn"] = data["ecsClusterArn"]
    if data.get("tags") is not None:
        import capo_batch.types.tagris_tags_map

        out["tags"] = capo_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    if data.get("type") is not None:
        import capo_batch.types.ce_type

        out["type"] = capo_batch.types.ce_type.deserialize_json(data["type"])
    if data.get("state") is not None:
        import capo_batch.types.ce_state

        out["state"] = capo_batch.types.ce_state.deserialize_json(data["state"])
    if data.get("status") is not None:
        import capo_batch.types.ce_status

        out["status"] = capo_batch.types.ce_status.deserialize_json(data["status"])
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("computeResources") is not None:
        import capo_batch.types.compute_resource

        out["compute_resources"] = capo_batch.types.compute_resource.deserialize_json(
            data["computeResources"]
        )
    if data.get("serviceRole") is not None:
        out["service_role"] = data["serviceRole"]
    if data.get("updatePolicy") is not None:
        import capo_batch.types.update_policy

        out["update_policy"] = capo_batch.types.update_policy.deserialize_json(
            data["updatePolicy"]
        )
    if data.get("eksConfiguration") is not None:
        import capo_batch.types.eks_configuration

        out["eks_configuration"] = capo_batch.types.eks_configuration.deserialize_json(
            data["eksConfiguration"]
        )
    if data.get("containerOrchestrationType") is not None:
        import capo_batch.types.orchestration_type

        out["container_orchestration_type"] = (
            capo_batch.types.orchestration_type.deserialize_json(
                data["containerOrchestrationType"]
            )
        )
    if data.get("uuid") is not None:
        out["uuid"] = data["uuid"]
    if data.get("context") is not None:
        out["context"] = data["context"]
    if data.get("ecsSettings") is not None:
        import capo_batch.types.ecs_settings

        out["ecs_settings"] = capo_batch.types.ecs_settings.deserialize_json(
            data["ecsSettings"]
        )
    return out
