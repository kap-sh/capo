"""Generated from Smithy shape ``com.amazonaws.eks#Cluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.access_config_response
    import capo_eks.types.boxed_boolean
    import capo_eks.types.certificate
    import capo_eks.types.cluster_health
    import capo_eks.types.cluster_status
    import capo_eks.types.compute_config_response
    import capo_eks.types.connector_config_response
    import capo_eks.types.control_plane_scaling_config
    import capo_eks.types.encryption_config_list
    import capo_eks.types.identity
    import capo_eks.types.kube_api_server_config_response
    import capo_eks.types.kube_controller_manager_config_response
    import capo_eks.types.kube_scheduler_config_response
    import capo_eks.types.kubernetes_network_config_response
    import capo_eks.types.logging
    import capo_eks.types.outpost_config_response
    import capo_eks.types.remote_network_config_response
    import capo_eks.types.storage_config_response
    import capo_eks.types.string
    import capo_eks.types.tag_map
    import capo_eks.types.timestamp
    import capo_eks.types.upgrade_policy_response
    import capo_eks.types.vpc_config_response
    import capo_eks.types.zonal_shift_config_response


class Cluster(TypedDict, closed=True):
    name: NotRequired["capo_eks.types.string.String"]
    """<p>The name of your cluster.</p>"""
    arn: NotRequired["capo_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    created_at: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp at object creation.</p>"""
    version: NotRequired["capo_eks.types.string.String"]
    """<p>The Kubernetes server version for the cluster.</p>"""
    endpoint: NotRequired["capo_eks.types.string.String"]
    """<p>The endpoint for your Kubernetes API server.</p>"""
    role_arn: NotRequired["capo_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to Amazon Web Services API operations on your behalf.</p>"""
    resources_vpc_config: NotRequired[
        "capo_eks.types.vpc_config_response.VpcConfigResponse"
    ]
    """<p>The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html">Cluster VPC considerations</a> and <a href="https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html">Cluster security group considerations</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    kubernetes_network_config: NotRequired[
        "capo_eks.types.kubernetes_network_config_response.KubernetesNetworkConfigResponse"
    ]
    """<p>The Kubernetes network configuration for the cluster.</p>"""
    logging: NotRequired["capo_eks.types.logging.Logging"]
    """<p>The logging configuration for your cluster.</p>"""
    identity: NotRequired["capo_eks.types.identity.Identity"]
    """<p>The identity provider information for the cluster.</p>"""
    status: NotRequired["capo_eks.types.cluster_status.ClusterStatus"]
    """<p>The current status of the cluster.</p>"""
    certificate_authority: NotRequired["capo_eks.types.certificate.Certificate"]
    """<p>The <code>certificate-authority-data</code> for your cluster.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    platform_version: NotRequired["capo_eks.types.string.String"]
    """<p>The platform version of your Amazon EKS cluster. For more information about clusters deployed on the Amazon Web Services Cloud, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html">Platform versions</a> in the <i> <i>Amazon EKS User Guide</i> </i>. For more information about local clusters deployed on an Outpost, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-platform-versions.html">Amazon EKS local cluster platform versions</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p>"""
    tags: NotRequired["capo_eks.types.tag_map.TagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""
    encryption_config: NotRequired[
        "capo_eks.types.encryption_config_list.EncryptionConfigList"
    ]
    """<p>The encryption configuration for the cluster.</p>"""
    connector_config: NotRequired[
        "capo_eks.types.connector_config_response.ConnectorConfigResponse"
    ]
    """<p>The configuration used to connect to a cluster for registration.</p>"""
    id: NotRequired["capo_eks.types.string.String"]
    """<p>The ID of your local Amazon EKS cluster on an Amazon Web Services Outpost. This property isn't available for an Amazon EKS cluster on the Amazon Web Services cloud.</p>"""
    health: NotRequired["capo_eks.types.cluster_health.ClusterHealth"]
    """<p>An object representing the health of your Amazon EKS cluster.</p>"""
    outpost_config: NotRequired[
        "capo_eks.types.outpost_config_response.OutpostConfigResponse"
    ]
    """<p>An object representing the configuration of your local Amazon EKS cluster on an Amazon Web Services Outpost. This object isn't available for clusters on the Amazon Web Services cloud.</p>"""
    access_config: NotRequired[
        "capo_eks.types.access_config_response.AccessConfigResponse"
    ]
    """<p>The access configuration for the cluster.</p>"""
    upgrade_policy: NotRequired[
        "capo_eks.types.upgrade_policy_response.UpgradePolicyResponse"
    ]
    """<p>This value indicates if extended support is enabled or disabled for the cluster.</p> <p> <a href="https://docs.aws.amazon.com/eks/latest/userguide/extended-support-control.html">Learn more about EKS Extended Support in the <i>Amazon EKS User Guide</i>.</a> </p>"""
    zonal_shift_config: NotRequired[
        "capo_eks.types.zonal_shift_config_response.ZonalShiftConfigResponse"
    ]
    """<p>The configuration for zonal shift for the cluster.</p>"""
    remote_network_config: NotRequired[
        "capo_eks.types.remote_network_config_response.RemoteNetworkConfigResponse"
    ]
    """<p>The configuration in the cluster for EKS Hybrid Nodes. You can add, change, or remove this configuration after the cluster is created.</p>"""
    compute_config: NotRequired[
        "capo_eks.types.compute_config_response.ComputeConfigResponse"
    ]
    """<p>Indicates the current configuration of the compute capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled. If the compute capability is enabled, EKS Auto Mode will create and delete EC2 Managed Instances in your Amazon Web Services account. For more information, see EKS Auto Mode compute capability in the <i>Amazon EKS User Guide</i>.</p>"""
    storage_config: NotRequired[
        "capo_eks.types.storage_config_response.StorageConfigResponse"
    ]
    """<p>Indicates the current configuration of the block storage capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled. If the block storage capability is enabled, EKS Auto Mode will create and delete EBS volumes in your Amazon Web Services account. For more information, see EKS Auto Mode block storage capability in the <i>Amazon EKS User Guide</i>.</p>"""
    deletion_protection: NotRequired["capo_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>The current deletion protection setting for the cluster. When <code>true</code>, deletion protection is enabled and the cluster cannot be deleted until protection is disabled. When <code>false</code>, the cluster can be deleted normally. This setting only applies to clusters in an active state.</p>"""
    control_plane_scaling_config: NotRequired[
        "capo_eks.types.control_plane_scaling_config.ControlPlaneScalingConfig"
    ]
    """<p>The control plane scaling tier configuration. For more information, see EKS Provisioned Control Plane in the Amazon EKS User Guide.</p>"""
    kube_api_server_config: NotRequired[
        "capo_eks.types.kube_api_server_config_response.KubeApiServerConfigResponse"
    ]
    """<p>The Kubernetes API server configuration for the cluster.</p>"""
    kube_scheduler_config: NotRequired[
        "capo_eks.types.kube_scheduler_config_response.KubeSchedulerConfigResponse"
    ]
    """<p>The Kubernetes scheduler configuration for the cluster.</p>"""
    kube_controller_manager_config: NotRequired[
        "capo_eks.types.kube_controller_manager_config_response.KubeControllerManagerConfigResponse"
    ]
    """<p>The Kubernetes controller manager configuration for the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Cluster) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import capo_eks.types.timestamp

        out["createdAt"] = capo_eks.types.timestamp.serialize_json(value["created_at"])
    if "version" in value:
        out["version"] = value["version"]
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "resources_vpc_config" in value:
        import capo_eks.types.vpc_config_response

        out["resourcesVpcConfig"] = capo_eks.types.vpc_config_response.serialize_json(
            value["resources_vpc_config"]
        )
    if "kubernetes_network_config" in value:
        import capo_eks.types.kubernetes_network_config_response

        out["kubernetesNetworkConfig"] = (
            capo_eks.types.kubernetes_network_config_response.serialize_json(
                value["kubernetes_network_config"]
            )
        )
    if "logging" in value:
        import capo_eks.types.logging

        out["logging"] = capo_eks.types.logging.serialize_json(value["logging"])
    if "identity" in value:
        import capo_eks.types.identity

        out["identity"] = capo_eks.types.identity.serialize_json(value["identity"])
    if "status" in value:
        import capo_eks.types.cluster_status

        out["status"] = capo_eks.types.cluster_status.serialize_json(value["status"])
    if "certificate_authority" in value:
        import capo_eks.types.certificate

        out["certificateAuthority"] = capo_eks.types.certificate.serialize_json(
            value["certificate_authority"]
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "platform_version" in value:
        out["platformVersion"] = value["platform_version"]
    if "tags" in value:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.serialize_json(value["tags"])
    if "encryption_config" in value:
        import capo_eks.types.encryption_config_list

        out["encryptionConfig"] = capo_eks.types.encryption_config_list.serialize_json(
            value["encryption_config"]
        )
    if "connector_config" in value:
        import capo_eks.types.connector_config_response

        out["connectorConfig"] = (
            capo_eks.types.connector_config_response.serialize_json(
                value["connector_config"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    if "health" in value:
        import capo_eks.types.cluster_health

        out["health"] = capo_eks.types.cluster_health.serialize_json(value["health"])
    if "outpost_config" in value:
        import capo_eks.types.outpost_config_response

        out["outpostConfig"] = capo_eks.types.outpost_config_response.serialize_json(
            value["outpost_config"]
        )
    if "access_config" in value:
        import capo_eks.types.access_config_response

        out["accessConfig"] = capo_eks.types.access_config_response.serialize_json(
            value["access_config"]
        )
    if "upgrade_policy" in value:
        import capo_eks.types.upgrade_policy_response

        out["upgradePolicy"] = capo_eks.types.upgrade_policy_response.serialize_json(
            value["upgrade_policy"]
        )
    if "zonal_shift_config" in value:
        import capo_eks.types.zonal_shift_config_response

        out["zonalShiftConfig"] = (
            capo_eks.types.zonal_shift_config_response.serialize_json(
                value["zonal_shift_config"]
            )
        )
    if "remote_network_config" in value:
        import capo_eks.types.remote_network_config_response

        out["remoteNetworkConfig"] = (
            capo_eks.types.remote_network_config_response.serialize_json(
                value["remote_network_config"]
            )
        )
    if "compute_config" in value:
        import capo_eks.types.compute_config_response

        out["computeConfig"] = capo_eks.types.compute_config_response.serialize_json(
            value["compute_config"]
        )
    if "storage_config" in value:
        import capo_eks.types.storage_config_response

        out["storageConfig"] = capo_eks.types.storage_config_response.serialize_json(
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
        import capo_eks.types.kube_api_server_config_response

        out["kubeApiServerConfig"] = (
            capo_eks.types.kube_api_server_config_response.serialize_json(
                value["kube_api_server_config"]
            )
        )
    if "kube_scheduler_config" in value:
        import capo_eks.types.kube_scheduler_config_response

        out["kubeSchedulerConfig"] = (
            capo_eks.types.kube_scheduler_config_response.serialize_json(
                value["kube_scheduler_config"]
            )
        )
    if "kube_controller_manager_config" in value:
        import capo_eks.types.kube_controller_manager_config_response

        out["kubeControllerManagerConfig"] = (
            capo_eks.types.kube_controller_manager_config_response.serialize_json(
                value["kube_controller_manager_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> Cluster:
    out: Cluster = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("createdAt") is not None:
        import capo_eks.types.timestamp

        out["created_at"] = capo_eks.types.timestamp.deserialize_json(data["createdAt"])
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("resourcesVpcConfig") is not None:
        import capo_eks.types.vpc_config_response

        out["resources_vpc_config"] = (
            capo_eks.types.vpc_config_response.deserialize_json(
                data["resourcesVpcConfig"]
            )
        )
    if data.get("kubernetesNetworkConfig") is not None:
        import capo_eks.types.kubernetes_network_config_response

        out["kubernetes_network_config"] = (
            capo_eks.types.kubernetes_network_config_response.deserialize_json(
                data["kubernetesNetworkConfig"]
            )
        )
    if data.get("logging") is not None:
        import capo_eks.types.logging

        out["logging"] = capo_eks.types.logging.deserialize_json(data["logging"])
    if data.get("identity") is not None:
        import capo_eks.types.identity

        out["identity"] = capo_eks.types.identity.deserialize_json(data["identity"])
    if data.get("status") is not None:
        import capo_eks.types.cluster_status

        out["status"] = capo_eks.types.cluster_status.deserialize_json(data["status"])
    if data.get("certificateAuthority") is not None:
        import capo_eks.types.certificate

        out["certificate_authority"] = capo_eks.types.certificate.deserialize_json(
            data["certificateAuthority"]
        )
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("platformVersion") is not None:
        out["platform_version"] = data["platformVersion"]
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
    if data.get("connectorConfig") is not None:
        import capo_eks.types.connector_config_response

        out["connector_config"] = (
            capo_eks.types.connector_config_response.deserialize_json(
                data["connectorConfig"]
            )
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("health") is not None:
        import capo_eks.types.cluster_health

        out["health"] = capo_eks.types.cluster_health.deserialize_json(data["health"])
    if data.get("outpostConfig") is not None:
        import capo_eks.types.outpost_config_response

        out["outpost_config"] = capo_eks.types.outpost_config_response.deserialize_json(
            data["outpostConfig"]
        )
    if data.get("accessConfig") is not None:
        import capo_eks.types.access_config_response

        out["access_config"] = capo_eks.types.access_config_response.deserialize_json(
            data["accessConfig"]
        )
    if data.get("upgradePolicy") is not None:
        import capo_eks.types.upgrade_policy_response

        out["upgrade_policy"] = capo_eks.types.upgrade_policy_response.deserialize_json(
            data["upgradePolicy"]
        )
    if data.get("zonalShiftConfig") is not None:
        import capo_eks.types.zonal_shift_config_response

        out["zonal_shift_config"] = (
            capo_eks.types.zonal_shift_config_response.deserialize_json(
                data["zonalShiftConfig"]
            )
        )
    if data.get("remoteNetworkConfig") is not None:
        import capo_eks.types.remote_network_config_response

        out["remote_network_config"] = (
            capo_eks.types.remote_network_config_response.deserialize_json(
                data["remoteNetworkConfig"]
            )
        )
    if data.get("computeConfig") is not None:
        import capo_eks.types.compute_config_response

        out["compute_config"] = capo_eks.types.compute_config_response.deserialize_json(
            data["computeConfig"]
        )
    if data.get("storageConfig") is not None:
        import capo_eks.types.storage_config_response

        out["storage_config"] = capo_eks.types.storage_config_response.deserialize_json(
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
        import capo_eks.types.kube_api_server_config_response

        out["kube_api_server_config"] = (
            capo_eks.types.kube_api_server_config_response.deserialize_json(
                data["kubeApiServerConfig"]
            )
        )
    if data.get("kubeSchedulerConfig") is not None:
        import capo_eks.types.kube_scheduler_config_response

        out["kube_scheduler_config"] = (
            capo_eks.types.kube_scheduler_config_response.deserialize_json(
                data["kubeSchedulerConfig"]
            )
        )
    if data.get("kubeControllerManagerConfig") is not None:
        import capo_eks.types.kube_controller_manager_config_response

        out["kube_controller_manager_config"] = (
            capo_eks.types.kube_controller_manager_config_response.deserialize_json(
                data["kubeControllerManagerConfig"]
            )
        )
    return out
