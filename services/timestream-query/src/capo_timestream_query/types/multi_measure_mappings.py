"""Generated from Smithy shape ``com.amazonaws.timestreamquery#MultiMeasureMappings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.multi_measure_attribute_mapping_list
    import capo_timestream_query.types.schema_name


class MultiMeasureMappings(TypedDict, closed=True):
    target_multi_measure_name: NotRequired[
        "capo_timestream_query.types.schema_name.SchemaName"
    ]
    """<p>The name of the target multi-measure name in the derived table. This input is required when measureNameColumn is not provided. If MeasureNameColumn is provided, then value from that column will be used as multi-measure name.</p>"""
    multi_measure_attribute_mappings: "capo_timestream_query.types.multi_measure_attribute_mapping_list.MultiMeasureAttributeMappingList"
    """<p>Required. Attribute mappings to be used for mapping query results to ingest data for multi-measure attributes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MultiMeasureMappings) -> dict:
    out: dict = {}
    if "target_multi_measure_name" in value:
        out["TargetMultiMeasureName"] = value["target_multi_measure_name"]
    import capo_timestream_query.types.multi_measure_attribute_mapping_list

    out["MultiMeasureAttributeMappings"] = (
        capo_timestream_query.types.multi_measure_attribute_mapping_list.serialize_aws_json_1_0(
            value["multi_measure_attribute_mappings"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> MultiMeasureMappings:
    out: MultiMeasureMappings = {}  # type: ignore[typeddict-item]
    if data.get("TargetMultiMeasureName") is not None:
        out["target_multi_measure_name"] = data["TargetMultiMeasureName"]
    if data.get("MultiMeasureAttributeMappings") is not None:
        import capo_timestream_query.types.multi_measure_attribute_mapping_list

        out["multi_measure_attribute_mappings"] = (
            capo_timestream_query.types.multi_measure_attribute_mapping_list.deserialize_aws_json_1_0(
                data["MultiMeasureAttributeMappings"]
            )
        )
    else:
        out["multi_measure_attribute_mappings"] = []
    return out
