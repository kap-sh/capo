"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ContainerMonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.container_attributes
    import capo_network_firewall.types.resource_arn


class ContainerMonitoringConfiguration(TypedDict, closed=True):
    cluster_arn: "capo_network_firewall.types.resource_arn.ResourceArn"
    """<p>The ARN of the Amazon ECS or Amazon EKS cluster to monitor. The cluster must be in the same Region and account as the container association.</p>"""
    attribute_filters: NotRequired[
        "capo_network_firewall.types.container_attributes.ContainerAttributes"
    ]
    """<p>Key-value pairs that filter which containers are tracked. For Amazon EKS, you can filter by namespace and Kubernetes labels. For Amazon ECS, you can filter by container instance attributes (EC2 launch type only).</p> <p>Attribute values can contain wildcard patterns, for example <code>payments-*</code>. Attribute keys must match exactly.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContainerMonitoringConfiguration) -> dict:
    out: dict = {}
    out["ClusterArn"] = value["cluster_arn"]
    if "attribute_filters" in value:
        import capo_network_firewall.types.container_attributes

        out["AttributeFilters"] = (
            capo_network_firewall.types.container_attributes.serialize_aws_json_1_0(
                value["attribute_filters"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ContainerMonitoringConfiguration:
    out: ContainerMonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ClusterArn") is not None:
        out["cluster_arn"] = data["ClusterArn"]
    else:
        out["cluster_arn"] = ""
    if data.get("AttributeFilters") is not None:
        import capo_network_firewall.types.container_attributes

        out["attribute_filters"] = (
            capo_network_firewall.types.container_attributes.deserialize_aws_json_1_0(
                data["AttributeFilters"]
            )
        )
    return out
