"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#QueryField``."""

from typing_extensions import TypedDict


class QueryField(TypedDict, closed=True):
    name: "str"
    """<p>The name of the column.</p>"""
    type: "str"
    """<p>The data type of the values in the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> QueryField:
    out: QueryField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    return out
