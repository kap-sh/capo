"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DataModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.dimension_mappings
    import capo_timestream_write.types.mixed_measure_mapping_list
    import capo_timestream_write.types.multi_measure_mappings
    import capo_timestream_write.types.string_value256
    import capo_timestream_write.types.time_unit


class DataModel(TypedDict, closed=True):
    time_column: NotRequired[
        "capo_timestream_write.types.string_value256.StringValue256"
    ]
    """<p>Source column to be mapped to time.</p>"""
    time_unit: NotRequired["capo_timestream_write.types.time_unit.TimeUnit"]
    """<p> The granularity of the timestamp unit. It indicates if the time value is in seconds, milliseconds, nanoseconds, or other supported values. Default is <code>MILLISECONDS</code>. </p>"""
    dimension_mappings: (
        "capo_timestream_write.types.dimension_mappings.DimensionMappings"
    )
    """<p>Source to target mappings for dimensions.</p>"""
    multi_measure_mappings: NotRequired[
        "capo_timestream_write.types.multi_measure_mappings.MultiMeasureMappings"
    ]
    """<p>Source to target mappings for multi-measure records.</p>"""
    mixed_measure_mappings: NotRequired[
        "capo_timestream_write.types.mixed_measure_mapping_list.MixedMeasureMappingList"
    ]
    """<p>Source to target mappings for measures.</p>"""
    measure_name_column: NotRequired[
        "capo_timestream_write.types.string_value256.StringValue256"
    ]
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataModel) -> dict:
    out: dict = {}
    if "time_column" in value:
        out["TimeColumn"] = value["time_column"]
    if "time_unit" in value:
        import capo_timestream_write.types.time_unit

        out["TimeUnit"] = capo_timestream_write.types.time_unit.serialize_aws_json_1_0(
            value["time_unit"]
        )
    import capo_timestream_write.types.dimension_mappings

    out["DimensionMappings"] = (
        capo_timestream_write.types.dimension_mappings.serialize_aws_json_1_0(
            value["dimension_mappings"]
        )
    )
    if "multi_measure_mappings" in value:
        import capo_timestream_write.types.multi_measure_mappings

        out["MultiMeasureMappings"] = (
            capo_timestream_write.types.multi_measure_mappings.serialize_aws_json_1_0(
                value["multi_measure_mappings"]
            )
        )
    if "mixed_measure_mappings" in value:
        import capo_timestream_write.types.mixed_measure_mapping_list

        out["MixedMeasureMappings"] = (
            capo_timestream_write.types.mixed_measure_mapping_list.serialize_aws_json_1_0(
                value["mixed_measure_mappings"]
            )
        )
    if "measure_name_column" in value:
        out["MeasureNameColumn"] = value["measure_name_column"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DataModel:
    out: DataModel = {}  # type: ignore[typeddict-item]
    if data.get("TimeColumn") is not None:
        out["time_column"] = data["TimeColumn"]
    if data.get("TimeUnit") is not None:
        import capo_timestream_write.types.time_unit

        out["time_unit"] = (
            capo_timestream_write.types.time_unit.deserialize_aws_json_1_0(
                data["TimeUnit"]
            )
        )
    if data.get("DimensionMappings") is not None:
        import capo_timestream_write.types.dimension_mappings

        out["dimension_mappings"] = (
            capo_timestream_write.types.dimension_mappings.deserialize_aws_json_1_0(
                data["DimensionMappings"]
            )
        )
    else:
        out["dimension_mappings"] = []
    if data.get("MultiMeasureMappings") is not None:
        import capo_timestream_write.types.multi_measure_mappings

        out["multi_measure_mappings"] = (
            capo_timestream_write.types.multi_measure_mappings.deserialize_aws_json_1_0(
                data["MultiMeasureMappings"]
            )
        )
    if data.get("MixedMeasureMappings") is not None:
        import capo_timestream_write.types.mixed_measure_mapping_list

        out["mixed_measure_mappings"] = (
            capo_timestream_write.types.mixed_measure_mapping_list.deserialize_aws_json_1_0(
                data["MixedMeasureMappings"]
            )
        )
    if data.get("MeasureNameColumn") is not None:
        out["measure_name_column"] = data["MeasureNameColumn"]
    return out
