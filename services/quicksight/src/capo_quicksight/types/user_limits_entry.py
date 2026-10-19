"""Generated from Smithy shape ``com.amazonaws.quicksight#UserLimitsEntry``."""

from typing_extensions import TypedDict


class UserLimitsEntry(TypedDict, closed=True):
    user_name: "str"
    """<p>The name of the user.</p>"""
    namespace: "str"
    """<p>The namespace of the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserLimitsEntry) -> dict:
    out: dict = {}
    out["userName"] = value["user_name"]
    out["namespace"] = value["namespace"]
    return out


def deserialize_json(data: dict) -> UserLimitsEntry:
    out: UserLimitsEntry = {}  # type: ignore[typeddict-item]
    if data.get("userName") is not None:
        out["user_name"] = data["userName"]
    else:
        out["user_name"] = ""
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    else:
        out["namespace"] = ""
    return out
