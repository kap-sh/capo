"""Generated from Smithy shape ``com.amazonaws.pipes#SingleMeasureMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.measure_name
    import capo_pipes.types.measure_value
    import capo_pipes.types.measure_value_type


class SingleMeasureMapping(TypedDict, closed=True):
    measure_value: "capo_pipes.types.measure_value.MeasureValue"
    """<p>Dynamic path of the source field to map to the measure in the record.</p>"""
    measure_value_type: "capo_pipes.types.measure_value_type.MeasureValueType"
    """<p>Data type of the source field.</p>"""
    measure_name: "capo_pipes.types.measure_name.MeasureName"
    """<p>Target measure name for the measurement attribute in the Timestream table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SingleMeasureMapping) -> dict:
    out: dict = {}
    out["MeasureValue"] = value["measure_value"]
    out["MeasureValueType"] = value["measure_value_type"]
    out["MeasureName"] = value["measure_name"]
    return out


def deserialize_json(data: dict) -> SingleMeasureMapping:
    out: SingleMeasureMapping = {}  # type: ignore[typeddict-item]
    if data.get("MeasureValue") is not None:
        out["measure_value"] = data["MeasureValue"]
    else:
        out["measure_value"] = ""
    if data.get("MeasureValueType") is not None:
        out["measure_value_type"] = data["MeasureValueType"]
    else:
        out["measure_value_type"] = ""
    if data.get("MeasureName") is not None:
        out["measure_name"] = data["MeasureName"]
    else:
        out["measure_name"] = ""
    return out
