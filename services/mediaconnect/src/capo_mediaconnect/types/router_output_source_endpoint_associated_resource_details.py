"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputSourceEndpointAssociatedResourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_output_messages
    import capo_mediaconnect.types.router_output_state


class RouterOutputSourceEndpointAssociatedResourceDetails(TypedDict, closed=True):
    name: "str"
    """<p>The name of the router output.</p>"""
    maximum_bitrate: "int"
    """<p>The maximum bitrate of the router output, in bits per second.</p>"""
    state: "capo_mediaconnect.types.router_output_state.RouterOutputState"
    """<p>The state of the router output.</p>"""
    messages: "capo_mediaconnect.types.router_output_messages.RouterOutputMessages"
    """<p>The status messages for the router output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputSourceEndpointAssociatedResourceDetails) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["maximumBitrate"] = value["maximum_bitrate"]
    import capo_mediaconnect.types.router_output_state

    out["state"] = capo_mediaconnect.types.router_output_state.serialize_json(
        value["state"]
    )
    import capo_mediaconnect.types.router_output_messages

    out["messages"] = capo_mediaconnect.types.router_output_messages.serialize_json(
        value["messages"]
    )
    return out


def deserialize_json(data: dict) -> RouterOutputSourceEndpointAssociatedResourceDetails:
    out: RouterOutputSourceEndpointAssociatedResourceDetails = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("maximumBitrate") is not None:
        out["maximum_bitrate"] = data["maximumBitrate"]
    else:
        out["maximum_bitrate"] = 0
    if data.get("state") is not None:
        import capo_mediaconnect.types.router_output_state

        out["state"] = capo_mediaconnect.types.router_output_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_mediaconnect.types.router_output_state.RouterOutputState", ""
        )
    if data.get("messages") is not None:
        import capo_mediaconnect.types.router_output_messages

        out["messages"] = (
            capo_mediaconnect.types.router_output_messages.deserialize_json(
                data["messages"]
            )
        )
    else:
        out["messages"] = []
    return out
