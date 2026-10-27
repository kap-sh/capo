"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointMessage``."""

from typing_extensions import TypedDict


class DestinationEndpointMessage(TypedDict, closed=True):
    code: "str"
    """<p>The message code.</p>"""
    message: "str"
    """<p>The message text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpointMessage) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DestinationEndpointMessage:
    out: DestinationEndpointMessage = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
