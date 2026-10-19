"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#MapMatchingConfig``."""

from typing_extensions import TypedDict


class MapMatchingConfig(TypedDict, closed=True):
    id_attribute_name: "str"
    """<p>The field name for the data that describes the identifier representing a collection of GPS points belonging to an individual trace.</p>"""
    y_attribute_name: "str"
    """<p>The name of the Y-attribute</p>"""
    x_attribute_name: "str"
    """<p>The name of the X-attribute</p>"""
    timestamp_attribute_name: "str"
    """<p>The name of the timestamp attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MapMatchingConfig) -> dict:
    out: dict = {}
    out["IdAttributeName"] = value["id_attribute_name"]
    out["YAttributeName"] = value["y_attribute_name"]
    out["XAttributeName"] = value["x_attribute_name"]
    out["TimestampAttributeName"] = value["timestamp_attribute_name"]
    return out


def deserialize_json(data: dict) -> MapMatchingConfig:
    out: MapMatchingConfig = {}  # type: ignore[typeddict-item]
    if data.get("IdAttributeName") is not None:
        out["id_attribute_name"] = data["IdAttributeName"]
    else:
        out["id_attribute_name"] = ""
    if data.get("YAttributeName") is not None:
        out["y_attribute_name"] = data["YAttributeName"]
    else:
        out["y_attribute_name"] = ""
    if data.get("XAttributeName") is not None:
        out["x_attribute_name"] = data["XAttributeName"]
    else:
        out["x_attribute_name"] = ""
    if data.get("TimestampAttributeName") is not None:
        out["timestamp_attribute_name"] = data["TimestampAttributeName"]
    else:
        out["timestamp_attribute_name"] = ""
    return out
