"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.transit_gateway_attachment_association
    import capo_ec2.types.transit_gateway_attachment_nat_gateway_support_state
    import capo_ec2.types.transit_gateway_attachment_resource_type
    import capo_ec2.types.transit_gateway_attachment_state


class TransitGatewayAttachment(TypedDict, closed=True):
    transit_gateway_attachment_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the attachment.</p>"""
    transit_gateway_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the transit gateway.</p>"""
    transit_gateway_owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the transit gateway.</p>"""
    resource_owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the resource.</p>"""
    resource_type: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The resource type. Note that the <code>tgw-peering</code> resource type has been deprecated.</p>"""
    resource_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    state: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_state.TransitGatewayAttachmentState"
    ]
    """<p>The attachment state. Note that the <code>initiating</code> state has been deprecated.</p>"""
    association: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_association.TransitGatewayAttachmentAssociation"
    ]
    """<p>The association.</p>"""
    creation_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The creation time.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags for the attachment.</p>"""
    nat_gateway_support: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_nat_gateway_support_state.TransitGatewayAttachmentNatGatewaySupportState"
    ]
    """<p>The state of NAT gateway support for the attachment. Only the owner of the transit gateway receives this parameter.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayAttachment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "transit_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}TransitGatewayId", str(value["transit_gateway_id"]))
        )
    if "transit_gateway_owner_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayOwnerId",
                str(value["transit_gateway_owner_id"]),
            )
        )
    if "resource_owner_id" in value:
        pairs.append((f"{key_prefix}ResourceOwnerId", str(value["resource_owner_id"])))
    if "resource_type" in value:
        import capo_ec2.types.transit_gateway_attachment_resource_type

        capo_ec2.types.transit_gateway_attachment_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{key_prefix}ResourceType"
        )
    if "resource_id" in value:
        pairs.append((f"{key_prefix}ResourceId", str(value["resource_id"])))
    if "state" in value:
        import capo_ec2.types.transit_gateway_attachment_state

        capo_ec2.types.transit_gateway_attachment_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "association" in value:
        import capo_ec2.types.transit_gateway_attachment_association

        capo_ec2.types.transit_gateway_attachment_association.serialize_ec2_query(
            value["association"], pairs, f"{key_prefix}Association"
        )
    if "creation_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{key_prefix}CreationTime"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "nat_gateway_support" in value:
        import capo_ec2.types.transit_gateway_attachment_nat_gateway_support_state

        capo_ec2.types.transit_gateway_attachment_nat_gateway_support_state.serialize_ec2_query(
            value["nat_gateway_support"], pairs, f"{key_prefix}NatGatewaySupport"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayAttachment:
    out: TransitGatewayAttachment = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("transitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_transit_gateway_id = el.find("transitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_transit_gateway_owner_id = el.find("transitGatewayOwnerId")
    if child_transit_gateway_owner_id is not None:
        out["transit_gateway_owner_id"] = str(child_transit_gateway_owner_id.text or "")
    child_resource_owner_id = el.find("resourceOwnerId")
    if child_resource_owner_id is not None:
        out["resource_owner_id"] = str(child_resource_owner_id.text or "")
    child_resource_type = el.find("resourceType")
    if child_resource_type is not None:
        import capo_ec2.types.transit_gateway_attachment_resource_type

        out["resource_type"] = (
            capo_ec2.types.transit_gateway_attachment_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_resource_id = el.find("resourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.transit_gateway_attachment_state

        out["state"] = (
            capo_ec2.types.transit_gateway_attachment_state.deserialize_ec2_query(
                child_state
            )
        )
    child_association = el.find("association")
    if child_association is not None:
        import capo_ec2.types.transit_gateway_attachment_association

        out["association"] = (
            capo_ec2.types.transit_gateway_attachment_association.deserialize_ec2_query(
                child_association
            )
        )
    child_creation_time = el.find("creationTime")
    if child_creation_time is not None:
        import capo_ec2.types.date_time

        out["creation_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_creation_time
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_nat_gateway_support = el.find("natGatewaySupport")
    if child_nat_gateway_support is not None:
        import capo_ec2.types.transit_gateway_attachment_nat_gateway_support_state

        out["nat_gateway_support"] = (
            capo_ec2.types.transit_gateway_attachment_nat_gateway_support_state.deserialize_ec2_query(
                child_nat_gateway_support
            )
        )
    return out
