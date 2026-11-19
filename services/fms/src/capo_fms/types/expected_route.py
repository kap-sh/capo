"""Generated from Smithy shape ``com.amazonaws.fms#ExpectedRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.cidr
    import capo_fms.types.length_bounded_string_list
    import capo_fms.types.resource_id
    import capo_fms.types.resource_id_list


class ExpectedRoute(TypedDict, closed=True):
    ip_v4_cidr: NotRequired["capo_fms.types.cidr.CIDR"]
    """<p>Information about the IPv4 CIDR block.</p>"""
    prefix_list_id: NotRequired["capo_fms.types.cidr.CIDR"]
    """<p>Information about the ID of the prefix list for the route.</p>"""
    ip_v6_cidr: NotRequired["capo_fms.types.cidr.CIDR"]
    """<p>Information about the IPv6 CIDR block.</p>"""
    contributing_subnets: NotRequired["capo_fms.types.resource_id_list.ResourceIdList"]
    """<p>Information about the contributing subnets.</p>"""
    allowed_targets: NotRequired[
        "capo_fms.types.length_bounded_string_list.LengthBoundedStringList"
    ]
    """<p>Information about the allowed targets.</p>"""
    route_table_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>Information about the route table ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpectedRoute) -> dict:
    out: dict = {}
    if "ip_v4_cidr" in value:
        out["IpV4Cidr"] = value["ip_v4_cidr"]
    if "prefix_list_id" in value:
        out["PrefixListId"] = value["prefix_list_id"]
    if "ip_v6_cidr" in value:
        out["IpV6Cidr"] = value["ip_v6_cidr"]
    if "contributing_subnets" in value:
        import capo_fms.types.resource_id_list

        out["ContributingSubnets"] = (
            capo_fms.types.resource_id_list.serialize_aws_json_1_1(
                value["contributing_subnets"]
            )
        )
    if "allowed_targets" in value:
        import capo_fms.types.length_bounded_string_list

        out["AllowedTargets"] = (
            capo_fms.types.length_bounded_string_list.serialize_aws_json_1_1(
                value["allowed_targets"]
            )
        )
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpectedRoute:
    out: ExpectedRoute = {}  # type: ignore[typeddict-item]
    if data.get("IpV4Cidr") is not None:
        out["ip_v4_cidr"] = data["IpV4Cidr"]
    if data.get("PrefixListId") is not None:
        out["prefix_list_id"] = data["PrefixListId"]
    if data.get("IpV6Cidr") is not None:
        out["ip_v6_cidr"] = data["IpV6Cidr"]
    if data.get("ContributingSubnets") is not None:
        import capo_fms.types.resource_id_list

        out["contributing_subnets"] = (
            capo_fms.types.resource_id_list.deserialize_aws_json_1_1(
                data["ContributingSubnets"]
            )
        )
    if data.get("AllowedTargets") is not None:
        import capo_fms.types.length_bounded_string_list

        out["allowed_targets"] = (
            capo_fms.types.length_bounded_string_list.deserialize_aws_json_1_1(
                data["AllowedTargets"]
            )
        )
    if data.get("RouteTableId") is not None:
        out["route_table_id"] = data["RouteTableId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExpectedRoute) -> dict:
    out: dict = {}
    if "ip_v4_cidr" in value:
        out["IpV4Cidr"] = value["ip_v4_cidr"]
    if "prefix_list_id" in value:
        out["PrefixListId"] = value["prefix_list_id"]
    if "ip_v6_cidr" in value:
        out["IpV6Cidr"] = value["ip_v6_cidr"]
    if "contributing_subnets" in value:
        import capo_fms.types.resource_id_list

        out["ContributingSubnets"] = capo_fms.types.resource_id_list.serialize_cbor(
            value["contributing_subnets"]
        )
    if "allowed_targets" in value:
        import capo_fms.types.length_bounded_string_list

        out["AllowedTargets"] = (
            capo_fms.types.length_bounded_string_list.serialize_cbor(
                value["allowed_targets"]
            )
        )
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    return out


def deserialize_cbor(data: dict) -> ExpectedRoute:
    out: ExpectedRoute = {}  # type: ignore[typeddict-item]
    if data.get("IpV4Cidr") is not None:
        out["ip_v4_cidr"] = data["IpV4Cidr"]
    if data.get("PrefixListId") is not None:
        out["prefix_list_id"] = data["PrefixListId"]
    if data.get("IpV6Cidr") is not None:
        out["ip_v6_cidr"] = data["IpV6Cidr"]
    if data.get("ContributingSubnets") is not None:
        import capo_fms.types.resource_id_list

        out["contributing_subnets"] = capo_fms.types.resource_id_list.deserialize_cbor(
            data["ContributingSubnets"]
        )
    if data.get("AllowedTargets") is not None:
        import capo_fms.types.length_bounded_string_list

        out["allowed_targets"] = (
            capo_fms.types.length_bounded_string_list.deserialize_cbor(
                data["AllowedTargets"]
            )
        )
    if data.get("RouteTableId") is not None:
        out["route_table_id"] = data["RouteTableId"]
    return out
