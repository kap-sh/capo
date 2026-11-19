"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ContextFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.region
    import capo_network_firewall.types.resource_type


class ContextFilters(TypedDict, closed=True):
    region: NotRequired["capo_network_firewall.types.region.Region"]
    """<p>The Amazon Web Services Region of the resources to return, for example <code>us-east-1</code>.</p>"""
    resource_type: NotRequired["capo_network_firewall.types.resource_type.ResourceType"]
    """<p>The type of resource to return. Each resource type corresponds to the <code>ContextType</code> that Network Firewall reports for the resource:</p> <ul> <li> <p> <code>SecurityGroup</code> - Security groups. Reported with the <code>SegmentId</code> context type.</p> </li> <li> <p> <code>VPC</code> - VPCs. Reported with the <code>ResourceId</code> context type.</p> </li> <li> <p> <code>Subnet</code> - Subnets. Reported with the <code>Subnet</code> context type.</p> </li> <li> <p> <code>TGWAttachment</code> - Transit gateway attachments. Reported with the <code>Attachment</code> context type.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContextFilters) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    if "resource_type" in value:
        import capo_network_firewall.types.resource_type

        out["ResourceType"] = (
            capo_network_firewall.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ContextFilters:
    out: ContextFilters = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("ResourceType") is not None:
        import capo_network_firewall.types.resource_type

        out["resource_type"] = (
            capo_network_firewall.types.resource_type.deserialize_aws_json_1_0(
                data["ResourceType"]
            )
        )
    return out
