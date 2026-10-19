"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledControlParameterSummary``."""

from typing_extensions import TypedDict


class EnabledControlParameterSummary(TypedDict, closed=True):
    key: "str"
    """<p>The key of a key/value pair.</p>"""
    value: "object"
    """<p>The value of a key/value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledControlParameterSummary) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> EnabledControlParameterSummary:
    out: EnabledControlParameterSummary = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = None
    return out
