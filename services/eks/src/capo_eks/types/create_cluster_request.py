"""Generated from Smithy shape ``com.amazonaws.eks#CreateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks.types.boxed_boolean
    import capo_eks.types.cluster_name
    import capo_eks.types.compute_config_request
    import capo_eks.types.control_plane_scaling_config
    import capo_eks.types.create_access_config_request
    import capo_eks.types.encryption_config_list
    import capo_eks.types.kube_api_server_config_request
    import capo_eks.types.kube_controller_manager_config_request
    import capo_eks.types.kube_scheduler_config_request
    import capo_eks.types.kubernetes_network_config_request
    import capo_eks.types.logging
    import capo_eks.types.outpost_config_request
    import capo_eks.types.remote_network_config_request
    import capo_eks.types.storage_config_request
    import capo_eks.types.string
    import capo_eks.types.tag_map
    import capo_eks.types.upgrade_policy_request
    import capo_eks.types.vpc_config_request
    import capo_eks.types.zonal_shift_config_request


class CreateClusterRequest(TypedDict, closed=True):
    name: "capo_eks.types.cluster_name.ClusterName"
    """<p>The unique name to give to your cluster. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphanumeric character and can't be longer than 100 characters. The name must be unique within the Amazon Web Services Region and Amazon Web Services account that you're creating the cluster in.</p>"""
    version: NotRequired["capo_eks.types.string.String"]
    """<p>The desired Kubernetes version for your cluster. If you don't specify a value here, the default version available in Amazon EKS is used.</p> <note> <p>The default version might not be the latest version available.</p> </note>"""
    role_arn: "capo_eks.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to Amazon Web Services API operations on your behalf. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/service_IAM_role.html">Amazon EKS Service IAM Role</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p>"""
    resources_vpc_config: "capo_eks.types.vpc_config_request.VpcConfigRequest"
    """<p>The VPC configuration that's used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html">Cluster VPC Considerations</a> and <a href="https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html">Cluster Security Group Considerations</a> in the <i>Amazon EKS User Guide</i>. You must specify at least two subnets. You can specify up to five security groups. However, we recommend that you use a dedicated security group for your cluster control plane.</p>"""
    kubernetes_network_config: NotRequired[
        "capo_eks.types.kubernetes_network_config_request.KubernetesNetworkConfigRequest"
    ]
    """<p>The Kubernetes network configuration for the cluster.</p>"""
    logging: NotRequired["capo_eks.types.logging.Logging"]
    """<p>Enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs . By default, cluster control plane logs aren't exported to CloudWatch Logs . For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html">Amazon EKS Cluster control plane logs</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p> <note> <p>CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see <a href="http://aws.amazon.com/cloudwatch/pricing/">CloudWatch Pricing</a>.</p> </note>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tags: NotRequired["capo_eks.types.tag_map.TagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""
    encryption_config: NotRequired[
        "capo_eks.types.encryption_config_list.EncryptionConfigList"
    ]
    """<p>The encryption configuration for the cluster.</p>"""
    outpost_config: NotRequired[
        "capo_eks.types.outpost_config_request.OutpostConfigRequest"
    ]
    """<p>An object representing the configuration of your local Amazon EKS cluster on an Amazon Web Services Outpost. Before creating a local cluster on an Outpost, review <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-local-cluster-overview.html">Local clusters for Amazon EKS on Amazon Web Services Outposts</a> in the <i>Amazon EKS User Guide</i>. This object isn't available for creating Amazon EKS clusters on the Amazon Web Services cloud.</p>"""
    access_config: NotRequired[
        "capo_eks.types.create_access_config_request.CreateAccessConfigRequest"
    ]
    """<p>The access configuration for the cluster.</p>"""
    bootstrap_self_managed_addons: NotRequired[
        "capo_eks.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>If you set this value to <code>False</code> when creating a cluster, the default networking add-ons will not be installed.</p> <p>The default networking add-ons include <code>vpc-cni</code>, <code>coredns</code>, and <code>kube-proxy</code>.</p> <p>Use this option when you plan to install third-party alternative add-ons or self-manage the default networking add-ons.</p>"""
    upgrade_policy: NotRequired[
        "capo_eks.types.upgrade_policy_request.UpgradePolicyRequest"
    ]
    """<p>New clusters, by default, have extended support enabled. You can disable extended support when creating a cluster by setting this value to <code>STANDARD</code>.</p>"""
    zonal_shift_config: NotRequired[
        "capo_eks.types.zonal_shift_config_request.ZonalShiftConfigRequest"
    ]
    """<p>Enable or disable ARC zonal shift for the cluster. If zonal shift is enabled, Amazon Web Services configures zonal autoshift for the cluster.</p> <p>Zonal shift is a feature of Amazon Application Recovery Controller (ARC). ARC zonal shift is designed to be a temporary measure that allows you to move traffic for a resource away from an impaired AZ until the zonal shift expires or you cancel it. You can extend the zonal shift if necessary.</p> <p>You can start a zonal shift for an Amazon EKS cluster, or you can allow Amazon Web Services to do it for you by enabling <i>zonal autoshift</i>. This shift updates the flow of east-to-west network traffic in your cluster to only consider network endpoints for Pods running on worker nodes in healthy AZs. Additionally, any ALB or NLB handling ingress traffic for applications in your Amazon EKS cluster will automatically route traffic to targets in the healthy AZs. For more information about zonal shift in EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html">Learn about Amazon Application Recovery Controller (ARC) Zonal Shift in Amazon EKS</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p>"""
    remote_network_config: NotRequired[
        "capo_eks.types.remote_network_config_request.RemoteNetworkConfigRequest"
    ]
    """<p>The configuration in the cluster for EKS Hybrid Nodes. You can add, change, or remove this configuration after the cluster is created.</p>"""
    compute_config: NotRequired[
        "capo_eks.types.compute_config_request.ComputeConfigRequest"
    ]
    """<p>Enable or disable the compute capability of EKS Auto Mode when creating your EKS Auto Mode cluster. If the compute capability is enabled, EKS Auto Mode will create and delete EC2 Managed Instances in your Amazon Web Services account</p>"""
    storage_config: NotRequired[
        "capo_eks.types.storage_config_request.StorageConfigRequest"
    ]
    """<p>Enable or disable the block storage capability of EKS Auto Mode when creating your EKS Auto Mode cluster. If the block storage capability is enabled, EKS Auto Mode will create and delete EBS volumes in your Amazon Web Services account.</p>"""
    deletion_protection: NotRequired["capo_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates whether to enable deletion protection for the cluster. When enabled, the cluster cannot be deleted unless deletion protection is first disabled. This helps prevent accidental cluster deletion. Default value is <code>false</code>.</p>"""
    control_plane_scaling_config: NotRequired[
        "capo_eks.types.control_plane_scaling_config.ControlPlaneScalingConfig"
    ]
    """<p>The control plane scaling tier configuration. For more information, see EKS Provisioned Control Plane in the Amazon EKS User Guide.</p>"""
    kube_api_server_config: NotRequired[
        "capo_eks.types.kube_api_server_config_request.KubeApiServerConfigRequest"
    ]
    """<p>The Kubernetes API server configuration for the new cluster.</p>"""
    kube_scheduler_config: NotRequired[
        "capo_eks.types.kube_scheduler_config_request.KubeSchedulerConfigRequest"
    ]
    """<p>The Kubernetes scheduler configuration for the new cluster.</p>"""
    kube_controller_manager_config: NotRequired[
        "capo_eks.types.kube_controller_manager_config_request.KubeControllerManagerConfigRequest"
    ]
    """<p>The Kubernetes controller manager configuration for the new cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateClusterRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    out["roleArn"] = value["role_arn"]
    import capo_eks.types.vpc_config_request

    out["resourcesVpcConfig"] = capo_eks.types.vpc_config_request.serialize_json(
        value["resources_vpc_config"]
    )
    if "kubernetes_network_config" in value:
        import capo_eks.types.kubernetes_network_config_request

        out["kubernetesNetworkConfig"] = (
            capo_eks.types.kubernetes_network_config_request.serialize_json(
                value["kubernetes_network_config"]
            )
        )
    if "logging" in value:
        import capo_eks.types.logging

        out["logging"] = capo_eks.types.logging.serialize_json(value["logging"])
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.serialize_json(value["tags"])
    if "encryption_config" in value:
        import capo_eks.types.encryption_config_list

        out["encryptionConfig"] = capo_eks.types.encryption_config_list.serialize_json(
            value["encryption_config"]
        )
    if "outpost_config" in value:
        import capo_eks.types.outpost_config_request

        out["outpostConfig"] = capo_eks.types.outpost_config_request.serialize_json(
            value["outpost_config"]
        )
    if "access_config" in value:
        import capo_eks.types.create_access_config_request

        out["accessConfig"] = (
            capo_eks.types.create_access_config_request.serialize_json(
                value["access_config"]
            )
        )
    if "bootstrap_self_managed_addons" in value:
        out["bootstrapSelfManagedAddons"] = value["bootstrap_self_managed_addons"]
    if "upgrade_policy" in value:
        import capo_eks.types.upgrade_policy_request

        out["upgradePolicy"] = capo_eks.types.upgrade_policy_request.serialize_json(
            value["upgrade_policy"]
        )
    if "zonal_shift_config" in value:
        import capo_eks.types.zonal_shift_config_request

        out["zonalShiftConfig"] = (
            capo_eks.types.zonal_shift_config_request.serialize_json(
                value["zonal_shift_config"]
            )
        )
    if "remote_network_config" in value:
        import capo_eks.types.remote_network_config_request

        out["remoteNetworkConfig"] = (
            capo_eks.types.remote_network_config_request.serialize_json(
                value["remote_network_config"]
            )
        )
    if "compute_config" in value:
        import capo_eks.types.compute_config_request

        out["computeConfig"] = capo_eks.types.compute_config_request.serialize_json(
            value["compute_config"]
        )
    if "storage_config" in value:
        import capo_eks.types.storage_config_request

        out["storageConfig"] = capo_eks.types.storage_config_request.serialize_json(
            value["storage_config"]
        )
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    if "control_plane_scaling_config" in value:
        import capo_eks.types.control_plane_scaling_config

        out["controlPlaneScalingConfig"] = (
            capo_eks.types.control_plane_scaling_config.serialize_json(
                value["control_plane_scaling_config"]
            )
        )
    if "kube_api_server_config" in value:
        import capo_eks.types.kube_api_server_config_request

        out["kubeApiServerConfig"] = (
            capo_eks.types.kube_api_server_config_request.serialize_json(
                value["kube_api_server_config"]
            )
        )
    if "kube_scheduler_config" in value:
        import capo_eks.types.kube_scheduler_config_request

        out["kubeSchedulerConfig"] = (
            capo_eks.types.kube_scheduler_config_request.serialize_json(
                value["kube_scheduler_config"]
            )
        )
    if "kube_controller_manager_config" in value:
        import capo_eks.types.kube_controller_manager_config_request

        out["kubeControllerManagerConfig"] = (
            capo_eks.types.kube_controller_manager_config_request.serialize_json(
                value["kube_controller_manager_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateClusterRequest:
    out: CreateClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateClusterRequest.name required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateClusterRequest.role_arn required")
    if data.get("resourcesVpcConfig") is not None:
        import capo_eks.types.vpc_config_request

        out["resources_vpc_config"] = (
            capo_eks.types.vpc_config_request.deserialize_json(
                data["resourcesVpcConfig"]
            )
        )
    else:
        raise DeserializationError("CreateClusterRequest.resources_vpc_config required")
    if data.get("kubernetesNetworkConfig") is not None:
        import capo_eks.types.kubernetes_network_config_request

        out["kubernetes_network_config"] = (
            capo_eks.types.kubernetes_network_config_request.deserialize_json(
                data["kubernetesNetworkConfig"]
            )
        )
    if data.get("logging") is not None:
        import capo_eks.types.logging

        out["logging"] = capo_eks.types.logging.deserialize_json(data["logging"])
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("tags") is not None:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.deserialize_json(data["tags"])
    if data.get("encryptionConfig") is not None:
        import capo_eks.types.encryption_config_list

        out["encryption_config"] = (
            capo_eks.types.encryption_config_list.deserialize_json(
                data["encryptionConfig"]
            )
        )
    if data.get("outpostConfig") is not None:
        import capo_eks.types.outpost_config_request

        out["outpost_config"] = capo_eks.types.outpost_config_request.deserialize_json(
            data["outpostConfig"]
        )
    if data.get("accessConfig") is not None:
        import capo_eks.types.create_access_config_request

        out["access_config"] = (
            capo_eks.types.create_access_config_request.deserialize_json(
                data["accessConfig"]
            )
        )
    if data.get("bootstrapSelfManagedAddons") is not None:
        out["bootstrap_self_managed_addons"] = data["bootstrapSelfManagedAddons"]
    if data.get("upgradePolicy") is not None:
        import capo_eks.types.upgrade_policy_request

        out["upgrade_policy"] = capo_eks.types.upgrade_policy_request.deserialize_json(
            data["upgradePolicy"]
        )
    if data.get("zonalShiftConfig") is not None:
        import capo_eks.types.zonal_shift_config_request

        out["zonal_shift_config"] = (
            capo_eks.types.zonal_shift_config_request.deserialize_json(
                data["zonalShiftConfig"]
            )
        )
    if data.get("remoteNetworkConfig") is not None:
        import capo_eks.types.remote_network_config_request

        out["remote_network_config"] = (
            capo_eks.types.remote_network_config_request.deserialize_json(
                data["remoteNetworkConfig"]
            )
        )
    if data.get("computeConfig") is not None:
        import capo_eks.types.compute_config_request

        out["compute_config"] = capo_eks.types.compute_config_request.deserialize_json(
            data["computeConfig"]
        )
    if data.get("storageConfig") is not None:
        import capo_eks.types.storage_config_request

        out["storage_config"] = capo_eks.types.storage_config_request.deserialize_json(
            data["storageConfig"]
        )
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    if data.get("controlPlaneScalingConfig") is not None:
        import capo_eks.types.control_plane_scaling_config

        out["control_plane_scaling_config"] = (
            capo_eks.types.control_plane_scaling_config.deserialize_json(
                data["controlPlaneScalingConfig"]
            )
        )
    if data.get("kubeApiServerConfig") is not None:
        import capo_eks.types.kube_api_server_config_request

        out["kube_api_server_config"] = (
            capo_eks.types.kube_api_server_config_request.deserialize_json(
                data["kubeApiServerConfig"]
            )
        )
    if data.get("kubeSchedulerConfig") is not None:
        import capo_eks.types.kube_scheduler_config_request

        out["kube_scheduler_config"] = (
            capo_eks.types.kube_scheduler_config_request.deserialize_json(
                data["kubeSchedulerConfig"]
            )
        )
    if data.get("kubeControllerManagerConfig") is not None:
        import capo_eks.types.kube_controller_manager_config_request

        out["kube_controller_manager_config"] = (
            capo_eks.types.kube_controller_manager_config_request.deserialize_json(
                data["kubeControllerManagerConfig"]
            )
        )
    return out
