"""Generated from Smithy shape ``com.amazonaws.notifications#AggregationKey``."""

from typing_extensions import TypedDict


class AggregationKey(TypedDict, closed=True):
    name: "str"
    """<p>Indicates the type of aggregation key.</p>"""
    value: "str"
    """<p>Indicates the value associated with the aggregation key name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationKey) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AggregationKey:
    out: AggregationKey = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
