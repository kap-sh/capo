"""Generated from Smithy shape ``com.amazonaws.evs#ConnectivityInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_evs.types.route_server_peering_list


class ConnectivityInfo(TypedDict, closed=True):
    private_route_server_peerings: (
        "capo_evs.types.route_server_peering_list.RouteServerPeeringList"
    )
    """<p>The unique IDs for private route server peers.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectivityInfo) -> dict:
    out: dict = {}
    import capo_evs.types.route_server_peering_list

    out["privateRouteServerPeerings"] = (
        capo_evs.types.route_server_peering_list.serialize_aws_json_1_0(
            value["private_route_server_peerings"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConnectivityInfo:
    out: ConnectivityInfo = {}  # type: ignore[typeddict-item]
    if data.get("privateRouteServerPeerings") is not None:
        import capo_evs.types.route_server_peering_list

        out["private_route_server_peerings"] = (
            capo_evs.types.route_server_peering_list.deserialize_aws_json_1_0(
                data["privateRouteServerPeerings"]
            )
        )
    else:
        out["private_route_server_peerings"] = []
    return out
