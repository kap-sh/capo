"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputDestinationEndpointAssociatedResourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_messages
    import capo_mediaconnect.types.router_input_state


class RouterInputDestinationEndpointAssociatedResourceDetails(TypedDict, closed=True):
    name: "str"
    """<p>The name of the router input.</p>"""
    maximum_bitrate: "int"
    """<p>The maximum bitrate of the router input, in bits per second.</p>"""
    state: "capo_mediaconnect.types.router_input_state.RouterInputState"
    """<p>The state of the router input.</p>"""
    messages: "capo_mediaconnect.types.router_input_messages.RouterInputMessages"
    """<p>The status messages for the router input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: RouterInputDestinationEndpointAssociatedResourceDetails,
) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["maximumBitrate"] = value["maximum_bitrate"]
    import capo_mediaconnect.types.router_input_state

    out["state"] = capo_mediaconnect.types.router_input_state.serialize_json(
        value["state"]
    )
    import capo_mediaconnect.types.router_input_messages

    out["messages"] = capo_mediaconnect.types.router_input_messages.serialize_json(
        value["messages"]
    )
    return out


def deserialize_json(
    data: dict,
) -> RouterInputDestinationEndpointAssociatedResourceDetails:
    out: RouterInputDestinationEndpointAssociatedResourceDetails = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("maximumBitrate") is not None:
        out["maximum_bitrate"] = data["maximumBitrate"]
    else:
        out["maximum_bitrate"] = 0
    if data.get("state") is not None:
        import capo_mediaconnect.types.router_input_state

        out["state"] = capo_mediaconnect.types.router_input_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_mediaconnect.types.router_input_state.RouterInputState", ""
        )
    if data.get("messages") is not None:
        import capo_mediaconnect.types.router_input_messages

        out["messages"] = (
            capo_mediaconnect.types.router_input_messages.deserialize_json(
                data["messages"]
            )
        )
    else:
        out["messages"] = []
    return out
