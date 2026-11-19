"""Generated from Smithy shape ``com.amazonaws.directconnect#RouteFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.address_family
    import capo_direct_connect.types.as_path_list
    import capo_direct_connect.types.community_list
    import capo_direct_connect.types.route_direction
    import capo_direct_connect.types.route_filter_cidr_string_list


class RouteFilters(TypedDict, closed=True):
    route_direction: NotRequired[
        "capo_direct_connect.types.route_direction.RouteDirection"
    ]
    """<p>The direction of the routes to return.</p> <p>The valid values are <code>accepted</code> (routes received from the customer network) and <code>advertised</code> (routes advertised to the customer network).</p>"""
    address_family: NotRequired[
        "capo_direct_connect.types.address_family.AddressFamily"
    ]
    """<p>The address family of the routes to return.</p> <p>The valid values are <code>ipv4</code> and <code>ipv6</code>.</p>"""
    cidrs: NotRequired[
        "capo_direct_connect.types.route_filter_cidr_string_list.RouteFilterCidrStringList"
    ]
    """<p>The CIDRs (prefixes) used to filter the routes. You can specify up to 10 CIDRs.</p>"""
    as_path: NotRequired["capo_direct_connect.types.as_path_list.AsPathList"]
    """<p>The autonomous system (AS) numbers used to filter the routes by their AS path.</p>"""
    communities: NotRequired["capo_direct_connect.types.community_list.CommunityList"]
    """<p>The BGP communities used to filter the routes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RouteFilters) -> dict:
    out: dict = {}
    if "route_direction" in value:
        import capo_direct_connect.types.route_direction

        out["routeDirection"] = (
            capo_direct_connect.types.route_direction.serialize_aws_json_1_1(
                value["route_direction"]
            )
        )
    if "address_family" in value:
        import capo_direct_connect.types.address_family

        out["addressFamily"] = (
            capo_direct_connect.types.address_family.serialize_aws_json_1_1(
                value["address_family"]
            )
        )
    if "cidrs" in value:
        import capo_direct_connect.types.route_filter_cidr_string_list

        out["cidrs"] = (
            capo_direct_connect.types.route_filter_cidr_string_list.serialize_aws_json_1_1(
                value["cidrs"]
            )
        )
    if "as_path" in value:
        import capo_direct_connect.types.as_path_list

        out["asPath"] = capo_direct_connect.types.as_path_list.serialize_aws_json_1_1(
            value["as_path"]
        )
    if "communities" in value:
        import capo_direct_connect.types.community_list

        out["communities"] = (
            capo_direct_connect.types.community_list.serialize_aws_json_1_1(
                value["communities"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RouteFilters:
    out: RouteFilters = {}  # type: ignore[typeddict-item]
    if data.get("routeDirection") is not None:
        import capo_direct_connect.types.route_direction

        out["route_direction"] = (
            capo_direct_connect.types.route_direction.deserialize_aws_json_1_1(
                data["routeDirection"]
            )
        )
    if data.get("addressFamily") is not None:
        import capo_direct_connect.types.address_family

        out["address_family"] = (
            capo_direct_connect.types.address_family.deserialize_aws_json_1_1(
                data["addressFamily"]
            )
        )
    if data.get("cidrs") is not None:
        import capo_direct_connect.types.route_filter_cidr_string_list

        out["cidrs"] = (
            capo_direct_connect.types.route_filter_cidr_string_list.deserialize_aws_json_1_1(
                data["cidrs"]
            )
        )
    if data.get("asPath") is not None:
        import capo_direct_connect.types.as_path_list

        out["as_path"] = (
            capo_direct_connect.types.as_path_list.deserialize_aws_json_1_1(
                data["asPath"]
            )
        )
    if data.get("communities") is not None:
        import capo_direct_connect.types.community_list

        out["communities"] = (
            capo_direct_connect.types.community_list.deserialize_aws_json_1_1(
                data["communities"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RouteFilters) -> dict:
    out: dict = {}
    if "route_direction" in value:
        import capo_direct_connect.types.route_direction

        out["routeDirection"] = (
            capo_direct_connect.types.route_direction.serialize_cbor(
                value["route_direction"]
            )
        )
    if "address_family" in value:
        import capo_direct_connect.types.address_family

        out["addressFamily"] = capo_direct_connect.types.address_family.serialize_cbor(
            value["address_family"]
        )
    if "cidrs" in value:
        import capo_direct_connect.types.route_filter_cidr_string_list

        out["cidrs"] = (
            capo_direct_connect.types.route_filter_cidr_string_list.serialize_cbor(
                value["cidrs"]
            )
        )
    if "as_path" in value:
        import capo_direct_connect.types.as_path_list

        out["asPath"] = capo_direct_connect.types.as_path_list.serialize_cbor(
            value["as_path"]
        )
    if "communities" in value:
        import capo_direct_connect.types.community_list

        out["communities"] = capo_direct_connect.types.community_list.serialize_cbor(
            value["communities"]
        )
    return out


def deserialize_cbor(data: dict) -> RouteFilters:
    out: RouteFilters = {}  # type: ignore[typeddict-item]
    if data.get("routeDirection") is not None:
        import capo_direct_connect.types.route_direction

        out["route_direction"] = (
            capo_direct_connect.types.route_direction.deserialize_cbor(
                data["routeDirection"]
            )
        )
    if data.get("addressFamily") is not None:
        import capo_direct_connect.types.address_family

        out["address_family"] = (
            capo_direct_connect.types.address_family.deserialize_cbor(
                data["addressFamily"]
            )
        )
    if data.get("cidrs") is not None:
        import capo_direct_connect.types.route_filter_cidr_string_list

        out["cidrs"] = (
            capo_direct_connect.types.route_filter_cidr_string_list.deserialize_cbor(
                data["cidrs"]
            )
        )
    if data.get("asPath") is not None:
        import capo_direct_connect.types.as_path_list

        out["as_path"] = capo_direct_connect.types.as_path_list.deserialize_cbor(
            data["asPath"]
        )
    if data.get("communities") is not None:
        import capo_direct_connect.types.community_list

        out["communities"] = capo_direct_connect.types.community_list.deserialize_cbor(
            data["communities"]
        )
    return out
