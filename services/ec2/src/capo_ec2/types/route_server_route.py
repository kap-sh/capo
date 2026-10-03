"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.as_path
    import capo_ec2.types.integer
    import capo_ec2.types.route_server_endpoint_id
    import capo_ec2.types.route_server_peer_id
    import capo_ec2.types.route_server_route_installation_details
    import capo_ec2.types.route_server_route_status
    import capo_ec2.types.string


class RouteServerRoute(TypedDict, closed=True):
    route_server_endpoint_id: NotRequired[
        "capo_ec2.types.route_server_endpoint_id.RouteServerEndpointId"
    ]
    """<p>The ID of the route server endpoint that received this route.</p>"""
    route_server_peer_id: NotRequired[
        "capo_ec2.types.route_server_peer_id.RouteServerPeerId"
    ]
    """<p>The ID of the route server peer that advertised this route.</p>"""
    route_installation_details: NotRequired[
        "capo_ec2.types.route_server_route_installation_details.RouteServerRouteInstallationDetails"
    ]
    """<p>Details about the installation status of this route in route tables.</p>"""
    route_status: NotRequired[
        "capo_ec2.types.route_server_route_status.RouteServerRouteStatus"
    ]
    """<p>The current status of the route in the routing database. Values are <code>in-rib</code> or <code>in-fib</code> depending on if the routes are in the RIB or the FIB database.</p> <p>The <a href="https://en.wikipedia.org/wiki/Routing_table">Routing Information Base (RIB)</a> serves as a database that stores all the routing information and network topology data collected by a router or routing system, such as routes learned from BGP peers. The RIB is constantly updated as new routing information is received or existing routes change. This ensures that the route server always has the most current view of the network topology and can make optimal routing decisions.</p> <p>The <a href="https://en.wikipedia.org/wiki/Forwarding_information_base">Forwarding Information Base (FIB)</a> serves as a forwarding table for what route server has determined are the best-path routes in the RIB after evaluating all available routing information and policies. The FIB routes are installed on the route tables. The FIB is recomputed whenever there are changes to the RIB.</p>"""
    prefix: NotRequired["capo_ec2.types.string.String"]
    """<p>The destination CIDR block of the route.</p>"""
    as_paths: NotRequired["capo_ec2.types.as_path.AsPath"]
    """<p>The AS path attributes of the BGP route.</p>"""
    med: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The Multi-Exit Discriminator (MED) value of the BGP route.</p>"""
    next_hop_ip: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address for the next hop.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerRoute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "route_server_endpoint_id" in value:
        pairs.append(
            (
                f"{key_prefix}RouteServerEndpointId",
                str(value["route_server_endpoint_id"]),
            )
        )
    if "route_server_peer_id" in value:
        pairs.append(
            (f"{key_prefix}RouteServerPeerId", str(value["route_server_peer_id"]))
        )
    if "route_installation_details" in value:
        import capo_ec2.types.route_server_route_installation_details

        capo_ec2.types.route_server_route_installation_details.serialize_ec2_query(
            value["route_installation_details"],
            pairs,
            f"{key_prefix}RouteInstallationDetailSet",
        )
    if "route_status" in value:
        import capo_ec2.types.route_server_route_status

        capo_ec2.types.route_server_route_status.serialize_ec2_query(
            value["route_status"], pairs, f"{key_prefix}RouteStatus"
        )
    if "prefix" in value:
        pairs.append((f"{key_prefix}Prefix", str(value["prefix"])))
    if "as_paths" in value:
        import capo_ec2.types.as_path

        capo_ec2.types.as_path.serialize_ec2_query(
            value["as_paths"], pairs, f"{key_prefix}AsPathSet"
        )
    if "med" in value:
        pairs.append((f"{key_prefix}Med", str(value["med"])))
    if "next_hop_ip" in value:
        pairs.append((f"{key_prefix}NextHopIp", str(value["next_hop_ip"])))


def deserialize_ec2_query(el: Element) -> RouteServerRoute:
    out: RouteServerRoute = {}  # type: ignore[typeddict-item]
    child_route_server_endpoint_id = el.find("routeServerEndpointId")
    if child_route_server_endpoint_id is not None:
        out["route_server_endpoint_id"] = str(child_route_server_endpoint_id.text or "")
    child_route_server_peer_id = el.find("routeServerPeerId")
    if child_route_server_peer_id is not None:
        out["route_server_peer_id"] = str(child_route_server_peer_id.text or "")
    child_route_installation_details = el.find("routeInstallationDetailSet")
    if child_route_installation_details is not None:
        import capo_ec2.types.route_server_route_installation_details

        out["route_installation_details"] = (
            capo_ec2.types.route_server_route_installation_details.deserialize_ec2_query(
                child_route_installation_details
            )
        )
    child_route_status = el.find("routeStatus")
    if child_route_status is not None:
        import capo_ec2.types.route_server_route_status

        out["route_status"] = (
            capo_ec2.types.route_server_route_status.deserialize_ec2_query(
                child_route_status
            )
        )
    child_prefix = el.find("prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_as_paths = el.find("asPathSet")
    if child_as_paths is not None:
        import capo_ec2.types.as_path

        out["as_paths"] = capo_ec2.types.as_path.deserialize_ec2_query(child_as_paths)
    child_med = el.find("med")
    if child_med is not None:
        out["med"] = int(child_med.text or "")
    child_next_hop_ip = el.find("nextHopIp")
    if child_next_hop_ip is not None:
        out["next_hop_ip"] = str(child_next_hop_ip.text or "")
    return out
