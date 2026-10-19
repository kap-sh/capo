"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ReverseGeocodingConfig``."""

from typing_extensions import TypedDict


class ReverseGeocodingConfig(TypedDict, closed=True):
    y_attribute_name: "str"
    """<p>The field name for the data that describes y-axis coordinate, eg. latitude of a point.</p>"""
    x_attribute_name: "str"
    """<p>The field name for the data that describes x-axis coordinate, eg. longitude of a point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReverseGeocodingConfig) -> dict:
    out: dict = {}
    out["YAttributeName"] = value["y_attribute_name"]
    out["XAttributeName"] = value["x_attribute_name"]
    return out


def deserialize_json(data: dict) -> ReverseGeocodingConfig:
    out: ReverseGeocodingConfig = {}  # type: ignore[typeddict-item]
    if data.get("YAttributeName") is not None:
        out["y_attribute_name"] = data["YAttributeName"]
    else:
        out["y_attribute_name"] = ""
    if data.get("XAttributeName") is not None:
        out["x_attribute_name"] = data["XAttributeName"]
    else:
        out["x_attribute_name"] = ""
    return out
