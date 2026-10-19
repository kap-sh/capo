"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterNetworkInterfaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.batch_get_router_network_interface_error_list
    import capo_mediaconnect.types.router_network_interface_list


class BatchGetRouterNetworkInterfaceResponse(TypedDict, closed=True):
    router_network_interfaces: "capo_mediaconnect.types.router_network_interface_list.RouterNetworkInterfaceList"
    """<p>An array of router network interfaces that were successfully retrieved.</p>"""
    errors: "capo_mediaconnect.types.batch_get_router_network_interface_error_list.BatchGetRouterNetworkInterfaceErrorList"
    """<p>An array of errors that occurred when retrieving the requested router network interfaces.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterNetworkInterfaceResponse) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.router_network_interface_list

    out["routerNetworkInterfaces"] = (
        capo_mediaconnect.types.router_network_interface_list.serialize_json(
            value["router_network_interfaces"]
        )
    )
    import capo_mediaconnect.types.batch_get_router_network_interface_error_list

    out["errors"] = (
        capo_mediaconnect.types.batch_get_router_network_interface_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetRouterNetworkInterfaceResponse:
    out: BatchGetRouterNetworkInterfaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("routerNetworkInterfaces") is not None:
        import capo_mediaconnect.types.router_network_interface_list

        out["router_network_interfaces"] = (
            capo_mediaconnect.types.router_network_interface_list.deserialize_json(
                data["routerNetworkInterfaces"]
            )
        )
    else:
        out["router_network_interfaces"] = []
    if data.get("errors") is not None:
        import capo_mediaconnect.types.batch_get_router_network_interface_error_list

        out["errors"] = (
            capo_mediaconnect.types.batch_get_router_network_interface_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out
