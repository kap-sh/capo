"""Generated from Smithy shape ``com.amazonaws.eks#VpcConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.boxed_boolean
    import capo_eks.types.control_plane_egress_mode_type
    import capo_eks.types.string_list


class VpcConfigRequest(TypedDict, closed=True):
    subnet_ids: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>Specify subnets for your Amazon EKS nodes. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your nodes and the Kubernetes control plane.</p>"""
    security_group_ids: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>Specify one or more security groups for the cross-account elastic network interfaces that Amazon EKS creates to use that allow communication between your nodes and the Kubernetes control plane. If you don't specify any security groups, then familiarize yourself with the difference between Amazon EKS defaults for clusters deployed with Kubernetes. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html">Amazon EKS security group considerations</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p>"""
    endpoint_public_access: NotRequired["capo_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Set this value to <code>false</code> to disable public access to your cluster's Kubernetes API server endpoint. If you disable public access, your cluster's Kubernetes API server can only receive requests from within the cluster VPC. The default value for this parameter is <code>true</code>, which enables public access for your Kubernetes API server. The endpoint domain name and IP address family depends on the value of the <code>ipFamily</code> for the cluster. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html">Cluster API server endpoint</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p>"""
    endpoint_private_access: NotRequired["capo_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Set this value to <code>true</code> to enable private access for your cluster's Kubernetes API server endpoint. If you enable private access, Kubernetes API requests from within your cluster's VPC use the private VPC endpoint. The default value for this parameter is <code>false</code>, which disables private access for your Kubernetes API server. If you disable private access and you have nodes or Fargate pods in the cluster, then ensure that <code>publicAccessCidrs</code> includes the necessary CIDR blocks for communication with the nodes or Fargate pods. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html">Cluster API server endpoint</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p>"""
    public_access_cidrs: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>The CIDR blocks that are allowed access to your cluster's public Kubernetes API server endpoint. Communication to the endpoint from addresses outside of the CIDR blocks that you specify is denied. The default value is <code>0.0.0.0/0</code> and additionally <code>::/0</code> for dual-stack `IPv6` clusters. If you've disabled private endpoint access, make sure that you specify the necessary CIDR blocks for every node and Fargate <code>Pod</code> in the cluster. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html">Cluster API server endpoint</a> in the <i> <i>Amazon EKS User Guide</i> </i>.</p> <p>Note that the public endpoints are dual-stack for only <code>IPv6</code> clusters that are made after October 2024. You can't add <code>IPv6</code> CIDR blocks to <code>IPv4</code> clusters or <code>IPv6</code> clusters that were made before October 2024.</p>"""
    control_plane_egress_mode: NotRequired[
        "capo_eks.types.control_plane_egress_mode_type.ControlPlaneEgressModeType"
    ]
    """<p>Specifies the control plane egress routing mode for the cluster. If the cluster is set to <code>AWS_MANAGED</code>, Amazon EKS manages the egress path from the control plane and you don't need to configure NAT gateways or other routing infrastructure for control plane traffic. If the cluster is set to <code>CUSTOMER_ROUTED</code>, you manage the egress path from the control plane in your VPC subnets. You are responsible for ensuring that the control plane can reach required endpoints such as webhook servers and OIDC providers. The default value is <code>AWS_MANAGED</code>. Once set to <code>CUSTOMER_ROUTED</code>, this setting cannot be changed back to <code>AWS_MANAGED</code> on the same cluster.</p> <p> <a href="https://docs.aws.amazon.com/eks/latest/userguide/control-plane-egress.html">Learn more about control plane egress routing in the <i>Amazon EKS User Guide</i>.</a> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfigRequest) -> dict:
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
    if "endpoint_public_access" in value:
        out["endpointPublicAccess"] = value["endpoint_public_access"]
    if "endpoint_private_access" in value:
        out["endpointPrivateAccess"] = value["endpoint_private_access"]
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


def deserialize_json(data: dict) -> VpcConfigRequest:
    out: VpcConfigRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("endpointPublicAccess") is not None:
        out["endpoint_public_access"] = data["endpointPublicAccess"]
    if data.get("endpointPrivateAccess") is not None:
        out["endpoint_private_access"] = data["endpointPrivateAccess"]
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
