"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputMessage``."""

from typing_extensions import TypedDict


class RouterInputMessage(TypedDict, closed=True):
    code: "str"
    """<p>The code associated with the router input message.</p>"""
    message: "str"
    """<p>The message text associated with the router input message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputMessage) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RouterInputMessage:
    out: RouterInputMessage = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
