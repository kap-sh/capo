"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayNetworkFunctionAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.network_function_attachment_az_id_list
    import capo_ec2.types.network_function_attachment_az_name_list
    import capo_ec2.types.transit_gateway_attachment_id


class ModifyTransitGatewayNetworkFunctionAttachmentRequest(TypedDict, closed=True):
    transit_gateway_attachment_id: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the network function attachment.</p>"""
    add_availability_zones: NotRequired[
        "capo_ec2.types.network_function_attachment_az_name_list.NetworkFunctionAttachmentAZNameList"
    ]
    """<p>The names of the Availability Zones to add to the attachment. You can't add and remove the same Availability Zone in a single request.</p>"""
    add_availability_zone_ids: NotRequired[
        "capo_ec2.types.network_function_attachment_az_id_list.NetworkFunctionAttachmentAZIdList"
    ]
    """<p>The IDs of the Availability Zones to add to the attachment. You can't add and remove the same Availability Zone in a single request.</p>"""
    remove_availability_zones: NotRequired[
        "capo_ec2.types.network_function_attachment_az_name_list.NetworkFunctionAttachmentAZNameList"
    ]
    """<p>The names of the Availability Zones to remove from the attachment. Each Availability Zone must be currently in the attachment.</p>"""
    remove_availability_zone_ids: NotRequired[
        "capo_ec2.types.network_function_attachment_az_id_list.NetworkFunctionAttachmentAZIdList"
    ]
    """<p>The IDs of the Availability Zones to remove from the attachment. Each Availability Zone must be currently in the attachment.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTransitGatewayNetworkFunctionAttachmentRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "add_availability_zones" in value:
        import capo_ec2.types.network_function_attachment_az_name_list

        capo_ec2.types.network_function_attachment_az_name_list.serialize_ec2_query(
            value["add_availability_zones"], pairs, f"{key_prefix}AddAvailabilityZone"
        )
    if "add_availability_zone_ids" in value:
        import capo_ec2.types.network_function_attachment_az_id_list

        capo_ec2.types.network_function_attachment_az_id_list.serialize_ec2_query(
            value["add_availability_zone_ids"],
            pairs,
            f"{key_prefix}AddAvailabilityZoneId",
        )
    if "remove_availability_zones" in value:
        import capo_ec2.types.network_function_attachment_az_name_list

        capo_ec2.types.network_function_attachment_az_name_list.serialize_ec2_query(
            value["remove_availability_zones"],
            pairs,
            f"{key_prefix}RemoveAvailabilityZone",
        )
    if "remove_availability_zone_ids" in value:
        import capo_ec2.types.network_function_attachment_az_id_list

        capo_ec2.types.network_function_attachment_az_id_list.serialize_ec2_query(
            value["remove_availability_zone_ids"],
            pairs,
            f"{key_prefix}RemoveAvailabilityZoneId",
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> ModifyTransitGatewayNetworkFunctionAttachmentRequest:
    out: ModifyTransitGatewayNetworkFunctionAttachmentRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_add_availability_zones = el.find("AddAvailabilityZone")
    if child_add_availability_zones is not None:
        import capo_ec2.types.network_function_attachment_az_name_list

        out["add_availability_zones"] = (
            capo_ec2.types.network_function_attachment_az_name_list.deserialize_ec2_query(
                child_add_availability_zones
            )
        )
    child_add_availability_zone_ids = el.find("AddAvailabilityZoneId")
    if child_add_availability_zone_ids is not None:
        import capo_ec2.types.network_function_attachment_az_id_list

        out["add_availability_zone_ids"] = (
            capo_ec2.types.network_function_attachment_az_id_list.deserialize_ec2_query(
                child_add_availability_zone_ids
            )
        )
    child_remove_availability_zones = el.find("RemoveAvailabilityZone")
    if child_remove_availability_zones is not None:
        import capo_ec2.types.network_function_attachment_az_name_list

        out["remove_availability_zones"] = (
            capo_ec2.types.network_function_attachment_az_name_list.deserialize_ec2_query(
                child_remove_availability_zones
            )
        )
    child_remove_availability_zone_ids = el.find("RemoveAvailabilityZoneId")
    if child_remove_availability_zone_ids is not None:
        import capo_ec2.types.network_function_attachment_az_id_list

        out["remove_availability_zone_ids"] = (
            capo_ec2.types.network_function_attachment_az_id_list.deserialize_ec2_query(
                child_remove_availability_zone_ids
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
