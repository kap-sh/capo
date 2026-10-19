"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeleteRouterNetworkInterfaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_network_interface_arn
    import capo_mediaconnect.types.router_network_interface_state


class DeleteRouterNetworkInterfaceResponse(TypedDict, closed=True):
    arn: (
        "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    )
    """<p>The ARN of the deleted router network interface.</p>"""
    name: "str"
    """<p>The name of the deleted router network interface.</p>"""
    state: "capo_mediaconnect.types.router_network_interface_state.RouterNetworkInterfaceState"
    """<p>The current state of the deleted router network interface, indicating where it is in the deletion process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRouterNetworkInterfaceResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import capo_mediaconnect.types.router_network_interface_state

    out["state"] = (
        capo_mediaconnect.types.router_network_interface_state.serialize_json(
            value["state"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteRouterNetworkInterfaceResponse:
    out: DeleteRouterNetworkInterfaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("state") is not None:
        import capo_mediaconnect.types.router_network_interface_state

        out["state"] = (
            capo_mediaconnect.types.router_network_interface_state.deserialize_json(
                data["state"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_mediaconnect.types.router_network_interface_state.RouterNetworkInterfaceState",
            "",
        )
    return out
