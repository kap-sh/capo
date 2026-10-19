"""Generated from Smithy shape ``com.amazonaws.timestreamquery#MixedMeasureMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.measure_value_type
    import capo_timestream_query.types.multi_measure_attribute_mapping_list
    import capo_timestream_query.types.schema_name


class MixedMeasureMapping(TypedDict, closed=True):
    measure_name: NotRequired["capo_timestream_query.types.schema_name.SchemaName"]
    """<p>Refers to the value of measure_name in a result row. This field is required if MeasureNameColumn is provided.</p>"""
    source_column: NotRequired["capo_timestream_query.types.schema_name.SchemaName"]
    """<p>This field refers to the source column from which measure-value is to be read for result materialization.</p>"""
    target_measure_name: NotRequired[
        "capo_timestream_query.types.schema_name.SchemaName"
    ]
    """<p>Target measure name to be used. If not provided, the target measure name by default would be measure-name if provided, or sourceColumn otherwise. </p>"""
    measure_value_type: (
        "capo_timestream_query.types.measure_value_type.MeasureValueType"
    )
    """<p>Type of the value that is to be read from sourceColumn. If the mapping is for MULTI, use MeasureValueType.MULTI.</p>"""
    multi_measure_attribute_mappings: NotRequired[
        "capo_timestream_query.types.multi_measure_attribute_mapping_list.MultiMeasureAttributeMappingList"
    ]
    """<p>Required when measureValueType is MULTI. Attribute mappings for MULTI value measures.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MixedMeasureMapping) -> dict:
    out: dict = {}
    if "measure_name" in value:
        out["MeasureName"] = value["measure_name"]
    if "source_column" in value:
        out["SourceColumn"] = value["source_column"]
    if "target_measure_name" in value:
        out["TargetMeasureName"] = value["target_measure_name"]
    import capo_timestream_query.types.measure_value_type

    out["MeasureValueType"] = (
        capo_timestream_query.types.measure_value_type.serialize_aws_json_1_0(
            value["measure_value_type"]
        )
    )
    if "multi_measure_attribute_mappings" in value:
        import capo_timestream_query.types.multi_measure_attribute_mapping_list

        out["MultiMeasureAttributeMappings"] = (
            capo_timestream_query.types.multi_measure_attribute_mapping_list.serialize_aws_json_1_0(
                value["multi_measure_attribute_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MixedMeasureMapping:
    out: MixedMeasureMapping = {}  # type: ignore[typeddict-item]
    if data.get("MeasureName") is not None:
        out["measure_name"] = data["MeasureName"]
    if data.get("SourceColumn") is not None:
        out["source_column"] = data["SourceColumn"]
    if data.get("TargetMeasureName") is not None:
        out["target_measure_name"] = data["TargetMeasureName"]
    if data.get("MeasureValueType") is not None:
        import capo_timestream_query.types.measure_value_type

        out["measure_value_type"] = (
            capo_timestream_query.types.measure_value_type.deserialize_aws_json_1_0(
                data["MeasureValueType"]
            )
        )
    else:
        import typing

        out["measure_value_type"] = typing.cast(
            "capo_timestream_query.types.measure_value_type.MeasureValueType", ""
        )
    if data.get("MultiMeasureAttributeMappings") is not None:
        import capo_timestream_query.types.multi_measure_attribute_mapping_list

        out["multi_measure_attribute_mappings"] = (
            capo_timestream_query.types.multi_measure_attribute_mapping_list.deserialize_aws_json_1_0(
                data["MultiMeasureAttributeMappings"]
            )
        )
    return out
