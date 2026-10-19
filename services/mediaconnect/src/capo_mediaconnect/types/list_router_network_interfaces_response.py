"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListRouterNetworkInterfacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.listed_router_network_interface_list


class ListRouterNetworkInterfacesResponse(TypedDict, closed=True):
    router_network_interfaces: "capo_mediaconnect.types.listed_router_network_interface_list.ListedRouterNetworkInterfaceList"
    """<p>The summary information for the retrieved router network interfaces.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRouterNetworkInterfacesResponse) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.listed_router_network_interface_list

    out["routerNetworkInterfaces"] = (
        capo_mediaconnect.types.listed_router_network_interface_list.serialize_json(
            value["router_network_interfaces"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRouterNetworkInterfacesResponse:
    out: ListRouterNetworkInterfacesResponse = {}  # type: ignore[typeddict-item]
    if data.get("routerNetworkInterfaces") is not None:
        import capo_mediaconnect.types.listed_router_network_interface_list

        out["router_network_interfaces"] = (
            capo_mediaconnect.types.listed_router_network_interface_list.deserialize_json(
                data["routerNetworkInterfaces"]
            )
        )
    else:
        out["router_network_interfaces"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
