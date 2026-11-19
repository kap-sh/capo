"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ResourceContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.attachment_type
    import capo_network_firewall.types.availability_zone
    import capo_network_firewall.types.context_type
    import capo_network_firewall.types.public_id
    import capo_network_firewall.types.region


class ResourceContext(TypedDict, closed=True):
    context_type: NotRequired["capo_network_firewall.types.context_type.ContextType"]
    """<p>The kind of context that the context store records for the resource. Valid values:</p> <ul> <li> <p> <code>ResourceId</code> - A VPC.</p> </li> <li> <p> <code>SegmentId</code> - A security group.</p> </li> <li> <p> <code>Subnet</code> - A subnet.</p> </li> <li> <p> <code>Attachment</code> - A transit gateway attachment.</p> </li> </ul>"""
    region: NotRequired["capo_network_firewall.types.region.Region"]
    """<p>The Amazon Web Services Region of the resource.</p>"""
    availability_zone: NotRequired[
        "capo_network_firewall.types.availability_zone.AvailabilityZone"
    ]
    """<p>The Availability Zone of the resource. Present for subnets.</p>"""
    attachment_type: NotRequired[
        "capo_network_firewall.types.attachment_type.AttachmentType"
    ]
    """<p>The type of the transit gateway attachment. Present for attachments.</p>"""
    public_id: "capo_network_firewall.types.public_id.PublicId"
    """<p>The identifier of the resource, for example <code>vpc-1234567890abcdef0</code>, <code>subnet-1234567890abcdef0</code>, <code>sg-1234567890abcdef0</code>, or <code>tgw-attach-1234567890abcdef0</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceContext) -> dict:
    out: dict = {}
    if "context_type" in value:
        import capo_network_firewall.types.context_type

        out["ContextType"] = (
            capo_network_firewall.types.context_type.serialize_aws_json_1_0(
                value["context_type"]
            )
        )
    if "region" in value:
        out["Region"] = value["region"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "attachment_type" in value:
        out["AttachmentType"] = value["attachment_type"]
    out["PublicId"] = value["public_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceContext:
    out: ResourceContext = {}  # type: ignore[typeddict-item]
    if data.get("ContextType") is not None:
        import capo_network_firewall.types.context_type

        out["context_type"] = (
            capo_network_firewall.types.context_type.deserialize_aws_json_1_0(
                data["ContextType"]
            )
        )
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("AttachmentType") is not None:
        out["attachment_type"] = data["AttachmentType"]
    if data.get("PublicId") is not None:
        out["public_id"] = data["PublicId"]
    else:
        out["public_id"] = ""
    return out
