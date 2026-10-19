"""Generated from Smithy shape ``com.amazonaws.pipes#MultiMeasureAttributeMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.measure_value
    import capo_pipes.types.measure_value_type
    import capo_pipes.types.multi_measure_attribute_name


class MultiMeasureAttributeMapping(TypedDict, closed=True):
    measure_value: "capo_pipes.types.measure_value.MeasureValue"
    """<p>Dynamic path to the measurement attribute in the source event.</p>"""
    measure_value_type: "capo_pipes.types.measure_value_type.MeasureValueType"
    """<p>Data type of the measurement attribute in the source event.</p>"""
    multi_measure_attribute_name: (
        "capo_pipes.types.multi_measure_attribute_name.MultiMeasureAttributeName"
    )
    """<p>Target measure name to be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiMeasureAttributeMapping) -> dict:
    out: dict = {}
    out["MeasureValue"] = value["measure_value"]
    out["MeasureValueType"] = value["measure_value_type"]
    out["MultiMeasureAttributeName"] = value["multi_measure_attribute_name"]
    return out


def deserialize_json(data: dict) -> MultiMeasureAttributeMapping:
    out: MultiMeasureAttributeMapping = {}  # type: ignore[typeddict-item]
    if data.get("MeasureValue") is not None:
        out["measure_value"] = data["MeasureValue"]
    else:
        out["measure_value"] = ""
    if data.get("MeasureValueType") is not None:
        out["measure_value_type"] = data["MeasureValueType"]
    else:
        out["measure_value_type"] = ""
    if data.get("MultiMeasureAttributeName") is not None:
        out["multi_measure_attribute_name"] = data["MultiMeasureAttributeName"]
    else:
        out["multi_measure_attribute_name"] = ""
    return out
