"""Generated from Smithy shape ``com.amazonaws.batch#CreateComputeEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.ce_state
    import capo_batch.types.ce_type
    import capo_batch.types.compute_resource
    import capo_batch.types.ecs_settings
    import capo_batch.types.eks_configuration
    import capo_batch.types.integer
    import capo_batch.types.string
    import capo_batch.types.tagris_tags_map


class CreateComputeEnvironmentRequest(TypedDict, closed=True):
    compute_environment_name: NotRequired["capo_batch.types.string.String"]
    """<p>The name for your compute environment. It can be up to 128 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).</p>"""
    type: NotRequired["capo_batch.types.ce_type.CEType"]
    """<p>The type of the compute environment: <code>MANAGED</code> or <code>UNMANAGED</code>. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html">Compute Environments</a> in the <i>Batch User Guide</i>.</p>"""
    state: NotRequired["capo_batch.types.ce_state.CEState"]
    """<p>The state of the compute environment. A compute environment must be created in the <code>ENABLED</code> state.</p> <p>If the state is <code>ENABLED</code>, then the compute environment accepts jobs from a queue and can scale out automatically based on queues.</p> <p>If the state is <code>ENABLED</code>, then the Batch scheduler can attempt to place jobs from an associated job queue on the compute resources within the environment. If the compute environment is managed, then it can scale its instances out or in automatically, based on the job queue demand.</p> <p>If the state is <code>DISABLED</code>, then the Batch scheduler doesn't attempt to place jobs within the environment. Jobs in a <code>STARTING</code> or <code>RUNNING</code> state continue to progress normally. Managed compute environments in the <code>DISABLED</code> state don't scale out. </p> <note> <p>Compute environments in a <code>DISABLED</code> state may continue to incur billing charges, for example, if they have running instances due to jobs that are still executing or a non-zero <code>minvCpus</code> setting. To prevent additional charges, disable and delete the compute environment.</p> </note> <p>When an instance is idle, the instance scales down to the <code>minvCpus</code> value. However, the instance size doesn't change. For example, consider a <code>c5.8xlarge</code> instance with a <code>minvCpus</code> value of <code>4</code> and a <code>desiredvCpus</code> value of <code>36</code>. This instance doesn't scale down to a <code>c5.large</code> instance.</p>"""
    unmanagedv_cpus: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The maximum number of vCPUs for an unmanaged compute environment. This parameter is only used for fair-share scheduling to reserve vCPU capacity for new share identifiers. If this parameter isn't provided for a fair-share job queue, no vCPU capacity is reserved.</p> <note> <p>This parameter is only supported when the <code>type</code> parameter is set to <code>UNMANAGED</code>.</p> </note>"""
    compute_resources: NotRequired["capo_batch.types.compute_resource.ComputeResource"]
    """<p>Details about the compute resources managed by the compute environment. This parameter is required for managed compute environments. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html">Compute Environments</a> in the <i>Batch User Guide</i>.</p>"""
    service_role: NotRequired["capo_batch.types.string.String"]
    """<p>The full Amazon Resource Name (ARN) of the IAM role that allows Batch to make calls to other Amazon Web Services services on your behalf. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html">Batch service IAM role</a> in the <i>Batch User Guide</i>.</p> <important> <p>If your account already created the Batch service-linked role, that role is used by default for your compute environment unless you specify a different role here. If the Batch service-linked role doesn't exist in your account, and no role is specified here, the service attempts to create the Batch service-linked role in your account.</p> <p>This automatic service-linked role creation only applies to <code>MANAGED</code> compute environments. For <code>UNMANAGED</code> compute environments, you must explicitly specify a <code>serviceRole</code>.</p> </important> <p>If your specified role has a path other than <code>/</code>, then you must specify either the full role ARN (recommended) or prefix the role name with the path. For example, if a role with the name <code>bar</code> has a path of <code>/foo/</code>, specify <code>/foo/bar</code> as the role name. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names">Friendly names and paths</a> in the <i>IAM User Guide</i>.</p> <note> <p>Depending on how you created your Batch service role, its ARN might contain the <code>service-role</code> path prefix. When you only specify the name of the service role, Batch assumes that your ARN doesn't use the <code>service-role</code> path prefix. Because of this, we recommend that you specify the full ARN of your service role when you create compute environments.</p> </note>"""
    tags: NotRequired["capo_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The tags that you apply to the compute environment to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a> in <i>Amazon Web Services General Reference</i>.</p> <p>These tags can be updated or removed using the <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html">TagResource</a> and <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html">UntagResource</a> API operations. These tags don't propagate to the underlying compute resources.</p>"""
    eks_configuration: NotRequired[
        "capo_batch.types.eks_configuration.EksConfiguration"
    ]
    """<p>The details for the Amazon EKS cluster that supports the compute environment.</p> <note> <p>To create a compute environment that uses EKS resources, the caller must have permissions to call <code>eks:DescribeCluster</code>.</p> </note>"""
    context: NotRequired["capo_batch.types.string.String"]
    """<p>Reserved.</p>"""
    ecs_settings: NotRequired["capo_batch.types.ecs_settings.EcsSettings"]
    """<p>The Amazon ECS settings for the compute environment. These settings control CloudWatch Container Insights collection for the compute environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateComputeEnvironmentRequest) -> dict:
    out: dict = {}
    if "compute_environment_name" in value:
        out["computeEnvironmentName"] = value["compute_environment_name"]
    if "type" in value:
        import capo_batch.types.ce_type

        out["type"] = capo_batch.types.ce_type.serialize_json(value["type"])
    if "state" in value:
        import capo_batch.types.ce_state

        out["state"] = capo_batch.types.ce_state.serialize_json(value["state"])
    if "unmanagedv_cpus" in value:
        out["unmanagedvCpus"] = value["unmanagedv_cpus"]
    if "compute_resources" in value:
        import capo_batch.types.compute_resource

        out["computeResources"] = capo_batch.types.compute_resource.serialize_json(
            value["compute_resources"]
        )
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "tags" in value:
        import capo_batch.types.tagris_tags_map

        out["tags"] = capo_batch.types.tagris_tags_map.serialize_json(value["tags"])
    if "eks_configuration" in value:
        import capo_batch.types.eks_configuration

        out["eksConfiguration"] = capo_batch.types.eks_configuration.serialize_json(
            value["eks_configuration"]
        )
    if "context" in value:
        out["context"] = value["context"]
    if "ecs_settings" in value:
        import capo_batch.types.ecs_settings

        out["ecsSettings"] = capo_batch.types.ecs_settings.serialize_json(
            value["ecs_settings"]
        )
    return out


def deserialize_json(data: dict) -> CreateComputeEnvironmentRequest:
    out: CreateComputeEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("computeEnvironmentName") is not None:
        out["compute_environment_name"] = data["computeEnvironmentName"]
    if data.get("type") is not None:
        import capo_batch.types.ce_type

        out["type"] = capo_batch.types.ce_type.deserialize_json(data["type"])
    if data.get("state") is not None:
        import capo_batch.types.ce_state

        out["state"] = capo_batch.types.ce_state.deserialize_json(data["state"])
    if data.get("unmanagedvCpus") is not None:
        out["unmanagedv_cpus"] = data["unmanagedvCpus"]
    if data.get("computeResources") is not None:
        import capo_batch.types.compute_resource

        out["compute_resources"] = capo_batch.types.compute_resource.deserialize_json(
            data["computeResources"]
        )
    if data.get("serviceRole") is not None:
        out["service_role"] = data["serviceRole"]
    if data.get("tags") is not None:
        import capo_batch.types.tagris_tags_map

        out["tags"] = capo_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    if data.get("eksConfiguration") is not None:
        import capo_batch.types.eks_configuration

        out["eks_configuration"] = capo_batch.types.eks_configuration.deserialize_json(
            data["eksConfiguration"]
        )
    if data.get("context") is not None:
        out["context"] = data["context"]
    if data.get("ecsSettings") is not None:
        import capo_batch.types.ecs_settings

        out["ecs_settings"] = capo_batch.types.ecs_settings.deserialize_json(
            data["ecsSettings"]
        )
    return out
