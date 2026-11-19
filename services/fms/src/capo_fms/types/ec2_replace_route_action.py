"""Generated from Smithy shape ``com.amazonaws.fms#EC2ReplaceRouteAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.action_target
    import capo_fms.types.cidr
    import capo_fms.types.length_bounded_string
    import capo_fms.types.resource_id


class EC2ReplaceRouteAction(TypedDict, closed=True):
    description: NotRequired["capo_fms.types.length_bounded_string.LengthBoundedString"]
    """<p>A description of the ReplaceRoute action in Amazon EC2.</p>"""
    destination_cidr_block: NotRequired["capo_fms.types.cidr.CIDR"]
    """<p>Information about the IPv4 CIDR address block used for the destination match. The value that you provide must match the CIDR of an existing route in the table.</p>"""
    destination_prefix_list_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>Information about the ID of the prefix list for the route.</p>"""
    destination_ipv6_cidr_block: NotRequired["capo_fms.types.cidr.CIDR"]
    """<p>Information about the IPv6 CIDR address block used for the destination match. The value that you provide must match the CIDR of an existing route in the table.</p>"""
    gateway_id: NotRequired["capo_fms.types.action_target.ActionTarget"]
    """<p>Information about the ID of an internet gateway or virtual private gateway.</p>"""
    route_table_id: "capo_fms.types.action_target.ActionTarget"
    """<p>Information about the ID of the route table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2ReplaceRouteAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "destination_cidr_block" in value:
        out["DestinationCidrBlock"] = value["destination_cidr_block"]
    if "destination_prefix_list_id" in value:
        out["DestinationPrefixListId"] = value["destination_prefix_list_id"]
    if "destination_ipv6_cidr_block" in value:
        out["DestinationIpv6CidrBlock"] = value["destination_ipv6_cidr_block"]
    if "gateway_id" in value:
        import capo_fms.types.action_target

        out["GatewayId"] = capo_fms.types.action_target.serialize_aws_json_1_1(
            value["gateway_id"]
        )
    import capo_fms.types.action_target

    out["RouteTableId"] = capo_fms.types.action_target.serialize_aws_json_1_1(
        value["route_table_id"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2ReplaceRouteAction:
    out: EC2ReplaceRouteAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DestinationCidrBlock") is not None:
        out["destination_cidr_block"] = data["DestinationCidrBlock"]
    if data.get("DestinationPrefixListId") is not None:
        out["destination_prefix_list_id"] = data["DestinationPrefixListId"]
    if data.get("DestinationIpv6CidrBlock") is not None:
        out["destination_ipv6_cidr_block"] = data["DestinationIpv6CidrBlock"]
    if data.get("GatewayId") is not None:
        import capo_fms.types.action_target

        out["gateway_id"] = capo_fms.types.action_target.deserialize_aws_json_1_1(
            data["GatewayId"]
        )
    if data.get("RouteTableId") is not None:
        import capo_fms.types.action_target

        out["route_table_id"] = capo_fms.types.action_target.deserialize_aws_json_1_1(
            data["RouteTableId"]
        )
    else:
        raise DeserializationError("EC2ReplaceRouteAction.route_table_id required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EC2ReplaceRouteAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "destination_cidr_block" in value:
        out["DestinationCidrBlock"] = value["destination_cidr_block"]
    if "destination_prefix_list_id" in value:
        out["DestinationPrefixListId"] = value["destination_prefix_list_id"]
    if "destination_ipv6_cidr_block" in value:
        out["DestinationIpv6CidrBlock"] = value["destination_ipv6_cidr_block"]
    if "gateway_id" in value:
        import capo_fms.types.action_target

        out["GatewayId"] = capo_fms.types.action_target.serialize_cbor(
            value["gateway_id"]
        )
    import capo_fms.types.action_target

    out["RouteTableId"] = capo_fms.types.action_target.serialize_cbor(
        value["route_table_id"]
    )
    return out


def deserialize_cbor(data: dict) -> EC2ReplaceRouteAction:
    out: EC2ReplaceRouteAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DestinationCidrBlock") is not None:
        out["destination_cidr_block"] = data["DestinationCidrBlock"]
    if data.get("DestinationPrefixListId") is not None:
        out["destination_prefix_list_id"] = data["DestinationPrefixListId"]
    if data.get("DestinationIpv6CidrBlock") is not None:
        out["destination_ipv6_cidr_block"] = data["DestinationIpv6CidrBlock"]
    if data.get("GatewayId") is not None:
        import capo_fms.types.action_target

        out["gateway_id"] = capo_fms.types.action_target.deserialize_cbor(
            data["GatewayId"]
        )
    if data.get("RouteTableId") is not None:
        import capo_fms.types.action_target

        out["route_table_id"] = capo_fms.types.action_target.deserialize_cbor(
            data["RouteTableId"]
        )
    else:
        raise DeserializationError("EC2ReplaceRouteAction.route_table_id required")
    return out
