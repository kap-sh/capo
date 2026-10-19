"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Tag``."""

from typing_extensions import TypedDict


class Tag(TypedDict, closed=True):
    key: "str"
    """<p>The key of the tag.</p>"""
    value: "str"
    """<p>The value of the tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
