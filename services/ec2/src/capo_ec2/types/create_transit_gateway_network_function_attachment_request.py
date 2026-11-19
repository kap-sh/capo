"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayNetworkFunctionAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.network_function_attachment_az_id_list
    import capo_ec2.types.network_function_attachment_az_name_list
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.transit_gateway_id


class CreateTransitGatewayNetworkFunctionAttachmentRequest(TypedDict, closed=True):
    transit_gateway_id: NotRequired[
        "capo_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway. The transit gateway must be in the <code>available</code> state.</p>"""
    service_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the Gateway Load Balancer endpoint service.</p>"""
    availability_zones: NotRequired[
        "capo_ec2.types.network_function_attachment_az_name_list.NetworkFunctionAttachmentAZNameList"
    ]
    """<p>The names of the Availability Zones for the attachment. You must specify at least one Availability Zone, using this parameter, <code>AvailabilityZoneIds</code>, or both. Each Availability Zone must be supported by both the transit gateway and the endpoint service.</p>"""
    availability_zone_ids: NotRequired[
        "capo_ec2.types.network_function_attachment_az_id_list.NetworkFunctionAttachmentAZIdList"
    ]
    """<p>The IDs of the Availability Zones for the attachment. You must specify at least one Availability Zone, using this parameter, <code>AvailabilityZones</code>, or both. Each Availability Zone must be supported by both the transit gateway and the endpoint service.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the network function attachment.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayNetworkFunctionAttachmentRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}TransitGatewayId", str(value["transit_gateway_id"]))
        )
    if "service_name" in value:
        pairs.append((f"{key_prefix}ServiceName", str(value["service_name"])))
    if "availability_zones" in value:
        import capo_ec2.types.network_function_attachment_az_name_list

        capo_ec2.types.network_function_attachment_az_name_list.serialize_ec2_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZone"
        )
    if "availability_zone_ids" in value:
        import capo_ec2.types.network_function_attachment_az_id_list

        capo_ec2.types.network_function_attachment_az_id_list.serialize_ec2_query(
            value["availability_zone_ids"], pairs, f"{key_prefix}AvailabilityZoneId"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> CreateTransitGatewayNetworkFunctionAttachmentRequest:
    out: CreateTransitGatewayNetworkFunctionAttachmentRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_service_name = el.find("ServiceName")
    if child_service_name is not None:
        out["service_name"] = str(child_service_name.text or "")
    child_availability_zones = el.find("AvailabilityZone")
    if child_availability_zones is not None:
        import capo_ec2.types.network_function_attachment_az_name_list

        out["availability_zones"] = (
            capo_ec2.types.network_function_attachment_az_name_list.deserialize_ec2_query(
                child_availability_zones
            )
        )
    child_availability_zone_ids = el.find("AvailabilityZoneId")
    if child_availability_zone_ids is not None:
        import capo_ec2.types.network_function_attachment_az_id_list

        out["availability_zone_ids"] = (
            capo_ec2.types.network_function_attachment_az_id_list.deserialize_ec2_query(
                child_availability_zone_ids
            )
        )
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
