"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#MultiMeasureAttributeMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.scalar_measure_value_type
    import capo_timestream_write.types.schema_name


class MultiMeasureAttributeMapping(TypedDict, closed=True):
    source_column: "capo_timestream_write.types.schema_name.SchemaName"
    """<p></p>"""
    target_multi_measure_attribute_name: NotRequired[
        "capo_timestream_write.types.schema_name.SchemaName"
    ]
    """<p></p>"""
    measure_value_type: NotRequired[
        "capo_timestream_write.types.scalar_measure_value_type.ScalarMeasureValueType"
    ]
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MultiMeasureAttributeMapping) -> dict:
    out: dict = {}
    out["SourceColumn"] = value["source_column"]
    if "target_multi_measure_attribute_name" in value:
        out["TargetMultiMeasureAttributeName"] = value[
            "target_multi_measure_attribute_name"
        ]
    if "measure_value_type" in value:
        import capo_timestream_write.types.scalar_measure_value_type

        out["MeasureValueType"] = (
            capo_timestream_write.types.scalar_measure_value_type.serialize_aws_json_1_0(
                value["measure_value_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MultiMeasureAttributeMapping:
    out: MultiMeasureAttributeMapping = {}  # type: ignore[typeddict-item]
    if data.get("SourceColumn") is not None:
        out["source_column"] = data["SourceColumn"]
    else:
        out["source_column"] = ""
    if data.get("TargetMultiMeasureAttributeName") is not None:
        out["target_multi_measure_attribute_name"] = data[
            "TargetMultiMeasureAttributeName"
        ]
    if data.get("MeasureValueType") is not None:
        import capo_timestream_write.types.scalar_measure_value_type

        out["measure_value_type"] = (
            capo_timestream_write.types.scalar_measure_value_type.deserialize_aws_json_1_0(
                data["MeasureValueType"]
            )
        )
    return out
