"""Generated from Smithy shape ``com.amazonaws.rtbfabric#HeaderTagAction``."""

from typing_extensions import TypedDict


class HeaderTagAction(TypedDict, closed=True):
    name: "str"
    """<p>The name of the bid action.</p>"""
    value: "str"
    """<p>The value of the bid action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HeaderTagAction) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> HeaderTagAction:
    out: HeaderTagAction = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
