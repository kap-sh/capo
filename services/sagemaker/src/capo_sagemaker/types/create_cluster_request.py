"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_auto_scaling_config
    import capo_sagemaker.types.cluster_instance_group_specifications
    import capo_sagemaker.types.cluster_name
    import capo_sagemaker.types.cluster_node_provisioning_mode
    import capo_sagemaker.types.cluster_node_recovery
    import capo_sagemaker.types.cluster_orchestrator
    import capo_sagemaker.types.cluster_restricted_instance_group_specifications
    import capo_sagemaker.types.cluster_restricted_instance_groups_config
    import capo_sagemaker.types.cluster_tiered_storage_config
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.vpc_config


class CreateClusterRequest(TypedDict, closed=True):
    cluster_name: NotRequired["capo_sagemaker.types.cluster_name.ClusterName"]
    """<p>The name for the new SageMaker HyperPod cluster.</p>"""
    instance_groups: NotRequired[
        "capo_sagemaker.types.cluster_instance_group_specifications.ClusterInstanceGroupSpecifications"
    ]
    """<p>The instance groups to be created in the SageMaker HyperPod cluster.</p>"""
    restricted_instance_groups: NotRequired[
        "capo_sagemaker.types.cluster_restricted_instance_group_specifications.ClusterRestrictedInstanceGroupSpecifications"
    ]
    """<p>The specialized instance groups for training models like Amazon Nova to be created in the SageMaker HyperPod cluster.</p>"""
    restricted_instance_groups_config: NotRequired[
        "capo_sagemaker.types.cluster_restricted_instance_groups_config.ClusterRestrictedInstanceGroupsConfig"
    ]
    """<p>The configuration for the restricted instance groups (RIG) in the SageMaker HyperPod cluster.</p>"""
    vpc_config: NotRequired["capo_sagemaker.types.vpc_config.VpcConfig"]
    """<p>Specifies the Amazon Virtual Private Cloud (VPC) that is associated with the Amazon SageMaker HyperPod cluster. You can control access to and from your resources by configuring your VPC. For more information, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html">Give SageMaker access to resources in your Amazon VPC</a>.</p> <note> <p>When your Amazon VPC and subnets support IPv6, network communications differ based on the cluster orchestration platform:</p> <ul> <li> <p>Slurm-orchestrated clusters automatically configure nodes with dual IPv6 and IPv4 addresses, allowing immediate IPv6 network communications.</p> </li> <li> <p>In Amazon EKS-orchestrated clusters, nodes receive dual-stack addressing, but pods can only use IPv6 when the Amazon EKS cluster is explicitly IPv6-enabled. For information about deploying an IPv6 Amazon EKS cluster, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/deploy-ipv6-cluster.html#_deploy_an_ipv6_cluster_with_eksctl">Amazon EKS IPv6 Cluster Deployment</a>.</p> </li> </ul> <p>Additional resources for IPv6 configuration:</p> <ul> <li> <p>For information about adding IPv6 support to your VPC, see to <a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6.html">IPv6 Support for VPC</a>.</p> </li> <li> <p>For information about creating a new IPv6-compatible VPC, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html">Amazon VPC Creation Guide</a>.</p> </li> <li> <p>To configure SageMaker HyperPod with a custom Amazon VPC, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html#sagemaker-hyperpod-prerequisites-optional-vpc">Custom Amazon VPC Setup for SageMaker HyperPod</a>.</p> </li> </ul> </note>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>Custom tags for managing the SageMaker HyperPod cluster as an Amazon Web Services resource. You can add tags to your cluster in the same way you add them in other Amazon Web Services services that support tagging. To learn more about tagging Amazon Web Services resources in general, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html">Tagging Amazon Web Services Resources User Guide</a>.</p>"""
    orchestrator: NotRequired[
        "capo_sagemaker.types.cluster_orchestrator.ClusterOrchestrator"
    ]
    """<p>The type of orchestrator to use for the SageMaker HyperPod cluster. Currently, supported values are <code>"Eks"</code> and <code>"Slurm"</code>, which is to use an Amazon Elastic Kubernetes Service or Slurm cluster as the orchestrator.</p> <note> <p>If you specify the <code>Orchestrator</code> field, you must provide exactly one orchestrator configuration: either <code>Eks</code> or <code>Slurm</code>. Specifying both or providing an empty configuration returns a validation error.</p> </note>"""
    node_recovery: NotRequired[
        "capo_sagemaker.types.cluster_node_recovery.ClusterNodeRecovery"
    ]
    """<p>The node recovery mode for the SageMaker HyperPod cluster. When set to <code>Automatic</code>, SageMaker HyperPod will automatically reboot or replace faulty nodes when issues are detected. When set to <code>None</code>, cluster administrators will need to manually manage any faulty cluster instances.</p>"""
    tiered_storage_config: NotRequired[
        "capo_sagemaker.types.cluster_tiered_storage_config.ClusterTieredStorageConfig"
    ]
    """<p>The configuration for managed tier checkpointing on the HyperPod cluster. When enabled, this feature uses a multi-tier storage approach for storing model checkpoints, providing faster checkpoint operations and improved fault tolerance across cluster nodes.</p>"""
    node_provisioning_mode: NotRequired[
        "capo_sagemaker.types.cluster_node_provisioning_mode.ClusterNodeProvisioningMode"
    ]
    """<p>The mode for provisioning nodes in the cluster. You can specify the following modes:</p> <ul> <li> <p> <b>Continuous</b>: Scaling behavior that enables 1) concurrent operation execution within instance groups, 2) continuous retry mechanisms for failed operations, 3) enhanced customer visibility into cluster events through detailed event streams, 4) partial provisioning capabilities. Your clusters and instance groups remain <code>InService</code> while scaling. This mode is only supported for EKS orchestrated clusters.</p> </li> </ul>"""
    cluster_role: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that HyperPod assumes to perform cluster autoscaling operations. This role must have permissions for <code>sagemaker:BatchAddClusterNodes</code> and <code>sagemaker:BatchDeleteClusterNodes</code>. This is only required when autoscaling is enabled and when HyperPod is performing autoscaling operations.</p>"""
    auto_scaling: NotRequired[
        "capo_sagemaker.types.cluster_auto_scaling_config.ClusterAutoScalingConfig"
    ]
    """<p>The autoscaling configuration for the cluster. Enables automatic scaling of cluster nodes based on workload demand using a Karpenter-based system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterRequest) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "instance_groups" in value:
        import capo_sagemaker.types.cluster_instance_group_specifications

        out["InstanceGroups"] = (
            capo_sagemaker.types.cluster_instance_group_specifications.serialize_aws_json_1_1(
                value["instance_groups"]
            )
        )
    if "restricted_instance_groups" in value:
        import capo_sagemaker.types.cluster_restricted_instance_group_specifications

        out["RestrictedInstanceGroups"] = (
            capo_sagemaker.types.cluster_restricted_instance_group_specifications.serialize_aws_json_1_1(
                value["restricted_instance_groups"]
            )
        )
    if "restricted_instance_groups_config" in value:
        import capo_sagemaker.types.cluster_restricted_instance_groups_config

        out["RestrictedInstanceGroupsConfig"] = (
            capo_sagemaker.types.cluster_restricted_instance_groups_config.serialize_aws_json_1_1(
                value["restricted_instance_groups_config"]
            )
        )
    if "vpc_config" in value:
        import capo_sagemaker.types.vpc_config

        out["VpcConfig"] = capo_sagemaker.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "orchestrator" in value:
        import capo_sagemaker.types.cluster_orchestrator

        out["Orchestrator"] = (
            capo_sagemaker.types.cluster_orchestrator.serialize_aws_json_1_1(
                value["orchestrator"]
            )
        )
    if "node_recovery" in value:
        import capo_sagemaker.types.cluster_node_recovery

        out["NodeRecovery"] = (
            capo_sagemaker.types.cluster_node_recovery.serialize_aws_json_1_1(
                value["node_recovery"]
            )
        )
    if "tiered_storage_config" in value:
        import capo_sagemaker.types.cluster_tiered_storage_config

        out["TieredStorageConfig"] = (
            capo_sagemaker.types.cluster_tiered_storage_config.serialize_aws_json_1_1(
                value["tiered_storage_config"]
            )
        )
    if "node_provisioning_mode" in value:
        import capo_sagemaker.types.cluster_node_provisioning_mode

        out["NodeProvisioningMode"] = (
            capo_sagemaker.types.cluster_node_provisioning_mode.serialize_aws_json_1_1(
                value["node_provisioning_mode"]
            )
        )
    if "cluster_role" in value:
        out["ClusterRole"] = value["cluster_role"]
    if "auto_scaling" in value:
        import capo_sagemaker.types.cluster_auto_scaling_config

        out["AutoScaling"] = (
            capo_sagemaker.types.cluster_auto_scaling_config.serialize_aws_json_1_1(
                value["auto_scaling"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterRequest:
    out: CreateClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    if data.get("InstanceGroups") is not None:
        import capo_sagemaker.types.cluster_instance_group_specifications

        out["instance_groups"] = (
            capo_sagemaker.types.cluster_instance_group_specifications.deserialize_aws_json_1_1(
                data["InstanceGroups"]
            )
        )
    if data.get("RestrictedInstanceGroups") is not None:
        import capo_sagemaker.types.cluster_restricted_instance_group_specifications

        out["restricted_instance_groups"] = (
            capo_sagemaker.types.cluster_restricted_instance_group_specifications.deserialize_aws_json_1_1(
                data["RestrictedInstanceGroups"]
            )
        )
    if data.get("RestrictedInstanceGroupsConfig") is not None:
        import capo_sagemaker.types.cluster_restricted_instance_groups_config

        out["restricted_instance_groups_config"] = (
            capo_sagemaker.types.cluster_restricted_instance_groups_config.deserialize_aws_json_1_1(
                data["RestrictedInstanceGroupsConfig"]
            )
        )
    if data.get("VpcConfig") is not None:
        import capo_sagemaker.types.vpc_config

        out["vpc_config"] = capo_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("Orchestrator") is not None:
        import capo_sagemaker.types.cluster_orchestrator

        out["orchestrator"] = (
            capo_sagemaker.types.cluster_orchestrator.deserialize_aws_json_1_1(
                data["Orchestrator"]
            )
        )
    if data.get("NodeRecovery") is not None:
        import capo_sagemaker.types.cluster_node_recovery

        out["node_recovery"] = (
            capo_sagemaker.types.cluster_node_recovery.deserialize_aws_json_1_1(
                data["NodeRecovery"]
            )
        )
    if data.get("TieredStorageConfig") is not None:
        import capo_sagemaker.types.cluster_tiered_storage_config

        out["tiered_storage_config"] = (
            capo_sagemaker.types.cluster_tiered_storage_config.deserialize_aws_json_1_1(
                data["TieredStorageConfig"]
            )
        )
    if data.get("NodeProvisioningMode") is not None:
        import capo_sagemaker.types.cluster_node_provisioning_mode

        out["node_provisioning_mode"] = (
            capo_sagemaker.types.cluster_node_provisioning_mode.deserialize_aws_json_1_1(
                data["NodeProvisioningMode"]
            )
        )
    if data.get("ClusterRole") is not None:
        out["cluster_role"] = data["ClusterRole"]
    if data.get("AutoScaling") is not None:
        import capo_sagemaker.types.cluster_auto_scaling_config

        out["auto_scaling"] = (
            capo_sagemaker.types.cluster_auto_scaling_config.deserialize_aws_json_1_1(
                data["AutoScaling"]
            )
        )
    return out
