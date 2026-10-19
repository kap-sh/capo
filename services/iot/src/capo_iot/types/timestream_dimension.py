"""Generated from Smithy shape ``com.amazonaws.iot#TimestreamDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.timestream_dimension_name
    import capo_iot.types.timestream_dimension_value


class TimestreamDimension(TypedDict, closed=True):
    name: "capo_iot.types.timestream_dimension_name.TimestreamDimensionName"
    """<p>The metadata dimension name. This is the name of the column in the Amazon Timestream database table record.</p> <p>Dimensions cannot be named: <code>measure_name</code>, <code>measure_value</code>, or <code>time</code>. These names are reserved. Dimension names cannot start with <code>ts_</code> or <code>measure_value</code> and they cannot contain the colon (<code>:</code>) character.</p>"""
    value: "capo_iot.types.timestream_dimension_value.TimestreamDimensionValue"
    """<p>The value to write in this column of the database record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimestreamDimension) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TimestreamDimension:
    out: TimestreamDimension = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
