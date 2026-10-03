"""Generated from Smithy shape ``com.amazonaws.eks#KubernetesNetworkConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.elastic_load_balancing
    import capo_eks.types.ip_family
    import capo_eks.types.string


class KubernetesNetworkConfigRequest(TypedDict, closed=True):
    service_ipv4_cidr: NotRequired["capo_eks.types.string.String"]
    """<p>Don't specify a value if you select <code>ipv6</code> for <b>ipFamily</b>. The CIDR block to assign Kubernetes service IP addresses from. If you don't specify a block, Kubernetes assigns addresses from either the <code>10.100.0.0/16</code> or <code>172.20.0.0/16</code> CIDR blocks. We recommend that you specify a block that does not overlap with resources in other networks that are peered or connected to your VPC. The block must meet the following requirements:</p> <ul> <li> <p>Within one of the following private IP address blocks: <code>10.0.0.0/8</code>, <code>172.16.0.0/12</code>, or <code>192.168.0.0/16</code>.</p> </li> <li> <p>Doesn't overlap with any CIDR block assigned to the VPC that you selected for VPC.</p> </li> <li> <p>Between <code>/24</code> and <code>/12</code>.</p> </li> </ul> <important> <p>You can only specify a custom CIDR block when you create a cluster. You can't change this value after the cluster is created.</p> </important>"""
    ip_family: NotRequired["capo_eks.types.ip_family.IpFamily"]
    """<p>Specify which IP family is used to assign Kubernetes pod and service IP addresses. If you don't specify a value, <code>ipv4</code> is used by default. You can only specify an IP family when you create a cluster and can't change this value once the cluster is created. If you specify <code>ipv6</code>, the VPC and subnets that you specify for cluster creation must have both <code>IPv4</code> and <code>IPv6</code> CIDR blocks assigned to them. You can't specify <code>ipv6</code> for clusters in China Regions.</p> <p>You can only specify <code>ipv6</code> for <code>1.21</code> and later clusters that use version <code>1.10.1</code> or later of the Amazon VPC CNI add-on. If you specify <code>ipv6</code>, then ensure that your VPC meets the requirements listed in the considerations listed in <a href="https://docs.aws.amazon.com/eks/latest/userguide/cni-ipv6.html">Assigning IPv6 addresses to pods and services</a> in the <i>Amazon EKS User Guide</i>. Kubernetes assigns services <code>IPv6</code> addresses from the unique local address range <code>(fc00::/7)</code>. You can't specify a custom <code>IPv6</code> CIDR block. Pod addresses are assigned from the subnet's <code>IPv6</code> CIDR.</p>"""
    elastic_load_balancing: NotRequired[
        "capo_eks.types.elastic_load_balancing.ElasticLoadBalancing"
    ]
    """<p>Request to enable or disable the load balancing capability on your EKS Auto Mode cluster. For more information, see EKS Auto Mode load balancing capability in the <i>Amazon EKS User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesNetworkConfigRequest) -> dict:
    out: dict = {}
    if "service_ipv4_cidr" in value:
        out["serviceIpv4Cidr"] = value["service_ipv4_cidr"]
    if "ip_family" in value:
        import capo_eks.types.ip_family

        out["ipFamily"] = capo_eks.types.ip_family.serialize_json(value["ip_family"])
    if "elastic_load_balancing" in value:
        import capo_eks.types.elastic_load_balancing

        out["elasticLoadBalancing"] = (
            capo_eks.types.elastic_load_balancing.serialize_json(
                value["elastic_load_balancing"]
            )
        )
    return out


def deserialize_json(data: dict) -> KubernetesNetworkConfigRequest:
    out: KubernetesNetworkConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceIpv4Cidr") is not None:
        out["service_ipv4_cidr"] = data["serviceIpv4Cidr"]
    if data.get("ipFamily") is not None:
        import capo_eks.types.ip_family

        out["ip_family"] = capo_eks.types.ip_family.deserialize_json(data["ipFamily"])
    if data.get("elasticLoadBalancing") is not None:
        import capo_eks.types.elastic_load_balancing

        out["elastic_load_balancing"] = (
            capo_eks.types.elastic_load_balancing.deserialize_json(
                data["elasticLoadBalancing"]
            )
        )
    return out
