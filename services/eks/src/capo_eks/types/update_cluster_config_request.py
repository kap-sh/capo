"""Generated from Smithy shape ``com.amazonaws.eks#UpdateClusterConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.boxed_boolean
    import capo_eks.types.compute_config_request
    import capo_eks.types.control_plane_scaling_config
    import capo_eks.types.kube_api_server_config_request
    import capo_eks.types.kube_controller_manager_config_request
    import capo_eks.types.kube_scheduler_config_request
    import capo_eks.types.kubernetes_network_config_request
    import capo_eks.types.logging
    import capo_eks.types.remote_network_config_request
    import capo_eks.types.storage_config_request
    import capo_eks.types.string
    import capo_eks.types.update_access_config_request
    import capo_eks.types.upgrade_policy_request
    import capo_eks.types.vpc_config_request
    import capo_eks.types.zonal_shift_config_request


class UpdateClusterConfigRequest(TypedDict, closed=True):
    name: "capo_eks.types.string.String"
    """<p>The name of the Amazon EKS cluster to update.</p>"""
    resources_vpc_config: NotRequired[
        "capo_eks.types.vpc_config_request.VpcConfigRequest"
    ]
    """<p>An object representing the VPC configuration to use for the cluster update. You can use this parameter to update the control plane egress mode, the subnets used by the cluster, the security groups, and the endpoint access settings.</p>"""
    logging: NotRequired["capo_eks.types.logging.Logging"]
    """<p>Enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs . By default, cluster control plane logs aren't exported to CloudWatch Logs . For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html">Amazon EKS cluster control plane logs</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p> <note> <p>CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see <a href="http://aws.amazon.com/cloudwatch/pricing/">CloudWatch Pricing</a>.</p> </note>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    access_config: NotRequired[
        "capo_eks.types.update_access_config_request.UpdateAccessConfigRequest"
    ]
    """<p>The access configuration for the cluster.</p>"""
    upgrade_policy: NotRequired[
        "capo_eks.types.upgrade_policy_request.UpgradePolicyRequest"
    ]
    """<p>You can enable or disable extended support for clusters currently on standard support. You cannot disable extended support once it starts. You must enable extended support before your cluster exits standard support.</p>"""
    zonal_shift_config: NotRequired[
        "capo_eks.types.zonal_shift_config_request.ZonalShiftConfigRequest"
    ]
    """<p>Enable or disable ARC zonal shift for the cluster. If zonal shift is enabled, Amazon Web Services configures zonal autoshift for the cluster.</p> <p>Zonal shift is a feature of Amazon Application Recovery Controller (ARC). ARC zonal shift is designed to be a temporary measure that allows you to move traffic for a resource away from an impaired AZ until the zonal shift expires or you cancel it. You can extend the zonal shift if necessary.</p> <p>You can start a zonal shift for an EKS cluster, or you can allow Amazon Web Services to do it for you by enabling <i>zonal autoshift</i>. This shift updates the flow of east-to-west network traffic in your cluster to only consider network endpoints for Pods running on worker nodes in healthy AZs. Additionally, any ALB or NLB handling ingress traffic for applications in your EKS cluster will automatically route traffic to targets in the healthy AZs. For more information about zonal shift in EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html">Learn about Amazon Application Recovery Controller (ARC) Zonal Shift in Amazon EKS</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p>"""
    compute_config: NotRequired[
        "capo_eks.types.compute_config_request.ComputeConfigRequest"
    ]
    """<p>Update the configuration of the compute capability of your EKS Auto Mode cluster. For example, enable the capability.</p>"""
    kubernetes_network_config: NotRequired[
        "capo_eks.types.kubernetes_network_config_request.KubernetesNetworkConfigRequest"
    ]
    storage_config: NotRequired[
        "capo_eks.types.storage_config_request.StorageConfigRequest"
    ]
    """<p>Update the configuration of the block storage capability of your EKS Auto Mode cluster. For example, enable the capability.</p>"""
    remote_network_config: NotRequired[
        "capo_eks.types.remote_network_config_request.RemoteNetworkConfigRequest"
    ]
    deletion_protection: NotRequired["capo_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether to enable or disable deletion protection for the cluster. When enabled (<code>true</code>), the cluster cannot be deleted until deletion protection is explicitly disabled. When disabled (<code>false</code>), the cluster can be deleted normally.</p>"""
    control_plane_scaling_config: NotRequired[
        "capo_eks.types.control_plane_scaling_config.ControlPlaneScalingConfig"
    ]
    """<p>The control plane scaling tier configuration. For more information, see EKS Provisioned Control Plane in the Amazon EKS User Guide.</p>"""
    kube_api_server_config: NotRequired[
        "capo_eks.types.kube_api_server_config_request.KubeApiServerConfigRequest"
    ]
    """<p>The Kubernetes API server configuration for the updated cluster.</p>"""
    kube_scheduler_config: NotRequired[
        "capo_eks.types.kube_scheduler_config_request.KubeSchedulerConfigRequest"
    ]
    """<p>The Kubernetes scheduler configuration for the updated cluster.</p>"""
    kube_controller_manager_config: NotRequired[
        "capo_eks.types.kube_controller_manager_config_request.KubeControllerManagerConfigRequest"
    ]
    """<p>The Kubernetes controller manager configuration for the updated cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClusterConfigRequest) -> dict:
    out: dict = {}
    if "resources_vpc_config" in value:
        import capo_eks.types.vpc_config_request

        out["resourcesVpcConfig"] = capo_eks.types.vpc_config_request.serialize_json(
            value["resources_vpc_config"]
        )
    if "logging" in value:
        import capo_eks.types.logging

        out["logging"] = capo_eks.types.logging.serialize_json(value["logging"])
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "access_config" in value:
        import capo_eks.types.update_access_config_request

        out["accessConfig"] = (
            capo_eks.types.update_access_config_request.serialize_json(
                value["access_config"]
            )
        )
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
    if "compute_config" in value:
        import capo_eks.types.compute_config_request

        out["computeConfig"] = capo_eks.types.compute_config_request.serialize_json(
            value["compute_config"]
        )
    if "kubernetes_network_config" in value:
        import capo_eks.types.kubernetes_network_config_request

        out["kubernetesNetworkConfig"] = (
            capo_eks.types.kubernetes_network_config_request.serialize_json(
                value["kubernetes_network_config"]
            )
        )
    if "storage_config" in value:
        import capo_eks.types.storage_config_request

        out["storageConfig"] = capo_eks.types.storage_config_request.serialize_json(
            value["storage_config"]
        )
    if "remote_network_config" in value:
        import capo_eks.types.remote_network_config_request

        out["remoteNetworkConfig"] = (
            capo_eks.types.remote_network_config_request.serialize_json(
                value["remote_network_config"]
            )
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


def deserialize_json(data: dict) -> UpdateClusterConfigRequest:
    out: UpdateClusterConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourcesVpcConfig") is not None:
        import capo_eks.types.vpc_config_request

        out["resources_vpc_config"] = (
            capo_eks.types.vpc_config_request.deserialize_json(
                data["resourcesVpcConfig"]
            )
        )
    if data.get("logging") is not None:
        import capo_eks.types.logging

        out["logging"] = capo_eks.types.logging.deserialize_json(data["logging"])
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("accessConfig") is not None:
        import capo_eks.types.update_access_config_request

        out["access_config"] = (
            capo_eks.types.update_access_config_request.deserialize_json(
                data["accessConfig"]
            )
        )
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
    if data.get("computeConfig") is not None:
        import capo_eks.types.compute_config_request

        out["compute_config"] = capo_eks.types.compute_config_request.deserialize_json(
            data["computeConfig"]
        )
    if data.get("kubernetesNetworkConfig") is not None:
        import capo_eks.types.kubernetes_network_config_request

        out["kubernetes_network_config"] = (
            capo_eks.types.kubernetes_network_config_request.deserialize_json(
                data["kubernetesNetworkConfig"]
            )
        )
    if data.get("storageConfig") is not None:
        import capo_eks.types.storage_config_request

        out["storage_config"] = capo_eks.types.storage_config_request.deserialize_json(
            data["storageConfig"]
        )
    if data.get("remoteNetworkConfig") is not None:
        import capo_eks.types.remote_network_config_request

        out["remote_network_config"] = (
            capo_eks.types.remote_network_config_request.deserialize_json(
                data["remoteNetworkConfig"]
            )
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
