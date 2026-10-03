"""Generated from Smithy shape ``com.amazonaws.autoscaling#TrafficSourceIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.xml_string_max_len511


class TrafficSourceIdentifier(TypedDict, closed=True):
    identifier: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len511.XmlStringMaxLen511"
    ]
    """<p>Identifies the traffic source.</p> <p>For Application Load Balancers, Gateway Load Balancers, Network Load Balancers, and VPC Lattice, this will be the Amazon Resource Name (ARN) for a target group in this account and Region. For Classic Load Balancers, this will be the name of the Classic Load Balancer in this account and Region.</p> <p>For example: </p> <ul> <li> <p>Application Load Balancer ARN: <code>arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/1234567890123456</code> </p> </li> <li> <p>Classic Load Balancer name: <code>my-classic-load-balancer</code> </p> </li> <li> <p>VPC Lattice ARN: <code>arn:aws:vpc-lattice:us-west-2:123456789012:targetgroup/tg-1234567890123456</code> </p> </li> </ul> <p>To get the ARN of a target group for a Application Load Balancer, Gateway Load Balancer, or Network Load Balancer, or the name of a Classic Load Balancer, use the Elastic Load Balancing <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html">DescribeTargetGroups</a> and <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html">DescribeLoadBalancers</a> API operations.</p> <p>To get the ARN of a target group for VPC Lattice, use the VPC Lattice <a href="https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetTargetGroup.html">GetTargetGroup</a> API operation.</p>"""
    type: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len511.XmlStringMaxLen511"
    ]
    """<p>Provides additional context for the value of <code>Identifier</code>.</p> <p>The following lists the valid values:</p> <ul> <li> <p> <code>elb</code> if <code>Identifier</code> is the name of a Classic Load Balancer.</p> </li> <li> <p> <code>elbv2</code> if <code>Identifier</code> is the ARN of an Application Load Balancer, Gateway Load Balancer, or Network Load Balancer target group.</p> </li> <li> <p> <code>vpc-lattice</code> if <code>Identifier</code> is the ARN of a VPC Lattice target group.</p> </li> </ul> <p>Required if the identifier is the name of a Classic Load Balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TrafficSourceIdentifier, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "identifier" in value:
        pairs.append((f"{key_prefix}Identifier", str(value["identifier"])))
    if "type" in value:
        pairs.append((f"{key_prefix}Type", str(value["type"])))


def deserialize_query(el: Element) -> TrafficSourceIdentifier:
    out: TrafficSourceIdentifier = {}  # type: ignore[typeddict-item]
    child_identifier = el.find("Identifier")
    if child_identifier is not None:
        out["identifier"] = str(child_identifier.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    return out
