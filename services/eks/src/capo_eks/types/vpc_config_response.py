"""Generated from Smithy shape ``com.amazonaws.eks#VpcConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.boolean
    import capo_eks.types.control_plane_egress_mode_type
    import capo_eks.types.string
    import capo_eks.types.string_list


class VpcConfigResponse(TypedDict, closed=True):
    subnet_ids: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>The subnets associated with your cluster.</p>"""
    security_group_ids: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your nodes and the Kubernetes control plane.</p>"""
    cluster_security_group_id: NotRequired["capo_eks.types.string.String"]
    """<p>The cluster security group that was created by Amazon EKS for the cluster. Managed node groups use this security group for control-plane-to-data-plane communication.</p>"""
    vpc_id: NotRequired["capo_eks.types.string.String"]
    """<p>The VPC associated with your cluster.</p>"""
    endpoint_public_access: "capo_eks.types.boolean.Boolean"
    """<p>Whether the public API server endpoint is enabled.</p>"""
    endpoint_private_access: "capo_eks.types.boolean.Boolean"
    """<p>This parameter indicates whether the Amazon EKS private API server endpoint is enabled. If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that originate from within your cluster's VPC use the private VPC endpoint instead of traversing the internet. If this value is disabled and you have nodes or Fargate pods in the cluster, then ensure that <code>publicAccessCidrs</code> includes the necessary CIDR blocks for communication with the nodes or Fargate pods. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html">Cluster API server endpoint</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p>"""
    public_access_cidrs: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>The CIDR blocks that are allowed access to your cluster's public Kubernetes API server endpoint. Communication to the endpoint from addresses outside of the CIDR blocks that you specify is denied. The default value is <code>0.0.0.0/0</code> and additionally <code>::/0</code> for dual-stack `IPv6` clusters. If you've disabled private endpoint access, make sure that you specify the necessary CIDR blocks for every node and Fargate <code>Pod</code> in the cluster. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html">Cluster API server endpoint</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p> <p>Note that the public endpoints are dual-stack for only <code>IPv6</code> clusters that are made after October 2024. You can't add <code>IPv6</code> CIDR blocks to <code>IPv4</code> clusters or <code>IPv6</code> clusters that were made before October 2024.</p>"""
    control_plane_egress_mode: NotRequired[
        "capo_eks.types.control_plane_egress_mode_type.ControlPlaneEgressModeType"
    ]
    """<p>The current control plane egress routing mode for the cluster. If the cluster is set to <code>AWS_MANAGED</code>, Amazon EKS manages the egress path from the control plane. If the cluster is set to <code>CUSTOMER_ROUTED</code>, you manage the egress path from the control plane in your VPC subnets.</p> <p> <a href="https://docs.aws.amazon.com/eks/latest/userguide/control-plane-egress.html">Learn more about control plane egress routing in the <i>Amazon EKS User Guide</i>.</a> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfigResponse) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import capo_eks.types.string_list

        out["subnetIds"] = capo_eks.types.string_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_eks.types.string_list

        out["securityGroupIds"] = capo_eks.types.string_list.serialize_json(
            value["security_group_ids"]
        )
    if "cluster_security_group_id" in value:
        out["clusterSecurityGroupId"] = value["cluster_security_group_id"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    out["endpointPublicAccess"] = value.get("endpoint_public_access", False)
    out["endpointPrivateAccess"] = value.get("endpoint_private_access", False)
    if "public_access_cidrs" in value:
        import capo_eks.types.string_list

        out["publicAccessCidrs"] = capo_eks.types.string_list.serialize_json(
            value["public_access_cidrs"]
        )
    if "control_plane_egress_mode" in value:
        import capo_eks.types.control_plane_egress_mode_type

        out["controlPlaneEgressMode"] = (
            capo_eks.types.control_plane_egress_mode_type.serialize_json(
                value["control_plane_egress_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> VpcConfigResponse:
    out: VpcConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("subnetIds") is not None:
        import capo_eks.types.string_list

        out["subnet_ids"] = capo_eks.types.string_list.deserialize_json(
            data["subnetIds"]
        )
    if data.get("securityGroupIds") is not None:
        import capo_eks.types.string_list

        out["security_group_ids"] = capo_eks.types.string_list.deserialize_json(
            data["securityGroupIds"]
        )
    if data.get("clusterSecurityGroupId") is not None:
        out["cluster_security_group_id"] = data["clusterSecurityGroupId"]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    if data.get("endpointPublicAccess") is not None:
        out["endpoint_public_access"] = data["endpointPublicAccess"]
    else:
        out["endpoint_public_access"] = False
    if data.get("endpointPrivateAccess") is not None:
        out["endpoint_private_access"] = data["endpointPrivateAccess"]
    else:
        out["endpoint_private_access"] = False
    if data.get("publicAccessCidrs") is not None:
        import capo_eks.types.string_list

        out["public_access_cidrs"] = capo_eks.types.string_list.deserialize_json(
            data["publicAccessCidrs"]
        )
    if data.get("controlPlaneEgressMode") is not None:
        import capo_eks.types.control_plane_egress_mode_type

        out["control_plane_egress_mode"] = (
            capo_eks.types.control_plane_egress_mode_type.deserialize_json(
                data["controlPlaneEgressMode"]
            )
        )
    return out
