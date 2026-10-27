"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.network_route_destination_list
    import capo_networkmanager.types.route_state
    import capo_networkmanager.types.route_type


class NetworkRoute(TypedDict, closed=True):
    destination_cidr_block: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>A unique identifier for the route, such as a CIDR block.</p>"""
    destinations: NotRequired[
        "capo_networkmanager.types.network_route_destination_list.NetworkRouteDestinationList"
    ]
    """<p>The destinations.</p>"""
    prefix_list_id: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The ID of the prefix list.</p>"""
    state: NotRequired["capo_networkmanager.types.route_state.RouteState"]
    """<p>The route state. The possible values are <code>active</code> and <code>blackhole</code>.</p>"""
    type: NotRequired["capo_networkmanager.types.route_type.RouteType"]
    """<p>The route type. The possible values are <code>PROPAGATED</code>, <code>STATIC</code>, and <code>SYSTEM</code>. A <code>SYSTEM</code> route is installed by the core network for the NAT CIDR block of an attachment's NAT rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkRoute) -> dict:
    out: dict = {}
    if "destination_cidr_block" in value:
        out["DestinationCidrBlock"] = value["destination_cidr_block"]
    if "destinations" in value:
        import capo_networkmanager.types.network_route_destination_list

        out["Destinations"] = (
            capo_networkmanager.types.network_route_destination_list.serialize_json(
                value["destinations"]
            )
        )
    if "prefix_list_id" in value:
        out["PrefixListId"] = value["prefix_list_id"]
    if "state" in value:
        import capo_networkmanager.types.route_state

        out["State"] = capo_networkmanager.types.route_state.serialize_json(
            value["state"]
        )
    if "type" in value:
        import capo_networkmanager.types.route_type

        out["Type"] = capo_networkmanager.types.route_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> NetworkRoute:
    out: NetworkRoute = {}  # type: ignore[typeddict-item]
    if data.get("DestinationCidrBlock") is not None:
        out["destination_cidr_block"] = data["DestinationCidrBlock"]
    if data.get("Destinations") is not None:
        import capo_networkmanager.types.network_route_destination_list

        out["destinations"] = (
            capo_networkmanager.types.network_route_destination_list.deserialize_json(
                data["Destinations"]
            )
        )
    if data.get("PrefixListId") is not None:
        out["prefix_list_id"] = data["PrefixListId"]
    if data.get("State") is not None:
        import capo_networkmanager.types.route_state

        out["state"] = capo_networkmanager.types.route_state.deserialize_json(
            data["State"]
        )
    if data.get("Type") is not None:
        import capo_networkmanager.types.route_type

        out["type"] = capo_networkmanager.types.route_type.deserialize_json(
            data["Type"]
        )
    return out
