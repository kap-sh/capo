"""Generated from Smithy shape ``com.amazonaws.directconnect#Route``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.address_family
    import capo_direct_connect.types.as_path_segment_list
    import capo_direct_connect.types.aws_logical_device_id
    import capo_direct_connect.types.community_list
    import capo_direct_connect.types.route_cidr
    import capo_direct_connect.types.route_direction
    import capo_direct_connect.types.route_installed_at


class Route(TypedDict, closed=True):
    cidr: NotRequired["capo_direct_connect.types.route_cidr.RouteCidr"]
    """<p>The CIDR (prefix) of the route.</p>"""
    route_direction: NotRequired[
        "capo_direct_connect.types.route_direction.RouteDirection"
    ]
    """<p>The direction of the route.</p> <p>The valid values are <code>accepted</code> (received from the customer network) and <code>advertised</code> (advertised to the customer network).</p>"""
    address_family: NotRequired[
        "capo_direct_connect.types.address_family.AddressFamily"
    ]
    """<p>The address family of the route.</p> <p>The valid values are <code>ipv4</code> and <code>ipv6</code>.</p>"""
    as_path: NotRequired[
        "capo_direct_connect.types.as_path_segment_list.AsPathSegmentList"
    ]
    """<p>The autonomous system (AS) path of the route.</p>"""
    communities: NotRequired["capo_direct_connect.types.community_list.CommunityList"]
    """<p>The BGP communities associated with the route.</p>"""
    aws_logical_device_id: NotRequired[
        "capo_direct_connect.types.aws_logical_device_id.AwsLogicalDeviceId"
    ]
    """<p>The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.</p>"""
    route_installed_at: NotRequired[
        "capo_direct_connect.types.route_installed_at.RouteInstalledAt"
    ]
    """<p>The time when the route was installed. The value is displayed in UTC format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Route) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["cidr"] = value["cidr"]
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
    if "as_path" in value:
        import capo_direct_connect.types.as_path_segment_list

        out["asPath"] = (
            capo_direct_connect.types.as_path_segment_list.serialize_aws_json_1_1(
                value["as_path"]
            )
        )
    if "communities" in value:
        import capo_direct_connect.types.community_list

        out["communities"] = (
            capo_direct_connect.types.community_list.serialize_aws_json_1_1(
                value["communities"]
            )
        )
    if "aws_logical_device_id" in value:
        out["awsLogicalDeviceId"] = value["aws_logical_device_id"]
    if "route_installed_at" in value:
        import capo_direct_connect.types.route_installed_at

        out["routeInstalledAt"] = (
            capo_direct_connect.types.route_installed_at.serialize_aws_json_1_1(
                value["route_installed_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Route:
    out: Route = {}  # type: ignore[typeddict-item]
    if data.get("cidr") is not None:
        out["cidr"] = data["cidr"]
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
    if data.get("asPath") is not None:
        import capo_direct_connect.types.as_path_segment_list

        out["as_path"] = (
            capo_direct_connect.types.as_path_segment_list.deserialize_aws_json_1_1(
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
    if data.get("awsLogicalDeviceId") is not None:
        out["aws_logical_device_id"] = data["awsLogicalDeviceId"]
    if data.get("routeInstalledAt") is not None:
        import capo_direct_connect.types.route_installed_at

        out["route_installed_at"] = (
            capo_direct_connect.types.route_installed_at.deserialize_aws_json_1_1(
                data["routeInstalledAt"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Route) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["cidr"] = value["cidr"]
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
    if "as_path" in value:
        import capo_direct_connect.types.as_path_segment_list

        out["asPath"] = capo_direct_connect.types.as_path_segment_list.serialize_cbor(
            value["as_path"]
        )
    if "communities" in value:
        import capo_direct_connect.types.community_list

        out["communities"] = capo_direct_connect.types.community_list.serialize_cbor(
            value["communities"]
        )
    if "aws_logical_device_id" in value:
        out["awsLogicalDeviceId"] = value["aws_logical_device_id"]
    if "route_installed_at" in value:
        import capo_direct_connect.types.route_installed_at

        out["routeInstalledAt"] = (
            capo_direct_connect.types.route_installed_at.serialize_cbor(
                value["route_installed_at"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Route:
    out: Route = {}  # type: ignore[typeddict-item]
    if data.get("cidr") is not None:
        out["cidr"] = data["cidr"]
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
    if data.get("asPath") is not None:
        import capo_direct_connect.types.as_path_segment_list

        out["as_path"] = (
            capo_direct_connect.types.as_path_segment_list.deserialize_cbor(
                data["asPath"]
            )
        )
    if data.get("communities") is not None:
        import capo_direct_connect.types.community_list

        out["communities"] = capo_direct_connect.types.community_list.deserialize_cbor(
            data["communities"]
        )
    if data.get("awsLogicalDeviceId") is not None:
        out["aws_logical_device_id"] = data["awsLogicalDeviceId"]
    if data.get("routeInstalledAt") is not None:
        import capo_direct_connect.types.route_installed_at

        out["route_installed_at"] = (
            capo_direct_connect.types.route_installed_at.deserialize_cbor(
                data["routeInstalledAt"]
            )
        )
    return out
