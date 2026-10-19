"""Generated from Smithy shape ``com.amazonaws.pipes#MultiMeasureMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.multi_measure_attribute_mappings
    import capo_pipes.types.multi_measure_name


class MultiMeasureMapping(TypedDict, closed=True):
    multi_measure_name: "capo_pipes.types.multi_measure_name.MultiMeasureName"
    """<p>The name of the multiple measurements per record (multi-measure).</p>"""
    multi_measure_attribute_mappings: "capo_pipes.types.multi_measure_attribute_mappings.MultiMeasureAttributeMappings"
    """<p>Mappings that represent multiple source event fields mapped to measures in the same Timestream for LiveAnalytics record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiMeasureMapping) -> dict:
    out: dict = {}
    out["MultiMeasureName"] = value["multi_measure_name"]
    import capo_pipes.types.multi_measure_attribute_mappings

    out["MultiMeasureAttributeMappings"] = (
        capo_pipes.types.multi_measure_attribute_mappings.serialize_json(
            value["multi_measure_attribute_mappings"]
        )
    )
    return out


def deserialize_json(data: dict) -> MultiMeasureMapping:
    out: MultiMeasureMapping = {}  # type: ignore[typeddict-item]
    if data.get("MultiMeasureName") is not None:
        out["multi_measure_name"] = data["MultiMeasureName"]
    else:
        out["multi_measure_name"] = ""
    if data.get("MultiMeasureAttributeMappings") is not None:
        import capo_pipes.types.multi_measure_attribute_mappings

        out["multi_measure_attribute_mappings"] = (
            capo_pipes.types.multi_measure_attribute_mappings.deserialize_json(
                data["MultiMeasureAttributeMappings"]
            )
        )
    else:
        out["multi_measure_attribute_mappings"] = []
    return out
