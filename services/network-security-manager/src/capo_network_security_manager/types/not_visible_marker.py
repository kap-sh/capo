"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#NotVisibleMarker``."""

from typing_extensions import TypedDict

from capo_network_security_manager.errors import DeserializationError


class NotVisibleMarker(TypedDict, closed=True):
    reason: "str"
    """<p>The reason the details are not visible.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotVisibleMarker) -> dict:
    out: dict = {}
    out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> NotVisibleMarker:
    out: NotVisibleMarker = {}  # type: ignore[typeddict-item]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    else:
        raise DeserializationError("NotVisibleMarker.reason required")
    return out
