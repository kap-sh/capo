"""Generated from Smithy shape ``com.amazonaws.timestreamquery#TimestreamConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.dimension_mapping_list
    import capo_timestream_query.types.mixed_measure_mapping_list
    import capo_timestream_query.types.multi_measure_mappings
    import capo_timestream_query.types.resource_name
    import capo_timestream_query.types.schema_name


class TimestreamConfiguration(TypedDict, closed=True):
    database_name: "capo_timestream_query.types.resource_name.ResourceName"
    """<p>Name of Timestream database to which the query result will be written.</p>"""
    table_name: "capo_timestream_query.types.resource_name.ResourceName"
    """<p>Name of Timestream table that the query result will be written to. The table should be within the same database that is provided in Timestream configuration.</p>"""
    time_column: "capo_timestream_query.types.schema_name.SchemaName"
    """<p>Column from query result that should be used as the time column in destination table. Column type for this should be TIMESTAMP.</p>"""
    dimension_mappings: (
        "capo_timestream_query.types.dimension_mapping_list.DimensionMappingList"
    )
    """<p> This is to allow mapping column(s) from the query result to the dimension in the destination table. </p>"""
    multi_measure_mappings: NotRequired[
        "capo_timestream_query.types.multi_measure_mappings.MultiMeasureMappings"
    ]
    """<p>Multi-measure mappings.</p>"""
    mixed_measure_mappings: NotRequired[
        "capo_timestream_query.types.mixed_measure_mapping_list.MixedMeasureMappingList"
    ]
    """<p>Specifies how to map measures to multi-measure records.</p>"""
    measure_name_column: NotRequired[
        "capo_timestream_query.types.schema_name.SchemaName"
    ]
    """<p>Name of the measure column.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimestreamConfiguration) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    out["TimeColumn"] = value["time_column"]
    import capo_timestream_query.types.dimension_mapping_list

    out["DimensionMappings"] = (
        capo_timestream_query.types.dimension_mapping_list.serialize_aws_json_1_0(
            value["dimension_mappings"]
        )
    )
    if "multi_measure_mappings" in value:
        import capo_timestream_query.types.multi_measure_mappings

        out["MultiMeasureMappings"] = (
            capo_timestream_query.types.multi_measure_mappings.serialize_aws_json_1_0(
                value["multi_measure_mappings"]
            )
        )
    if "mixed_measure_mappings" in value:
        import capo_timestream_query.types.mixed_measure_mapping_list

        out["MixedMeasureMappings"] = (
            capo_timestream_query.types.mixed_measure_mapping_list.serialize_aws_json_1_0(
                value["mixed_measure_mappings"]
            )
        )
    if "measure_name_column" in value:
        out["MeasureNameColumn"] = value["measure_name_column"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TimestreamConfiguration:
    out: TimestreamConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("TimeColumn") is not None:
        out["time_column"] = data["TimeColumn"]
    else:
        out["time_column"] = ""
    if data.get("DimensionMappings") is not None:
        import capo_timestream_query.types.dimension_mapping_list

        out["dimension_mappings"] = (
            capo_timestream_query.types.dimension_mapping_list.deserialize_aws_json_1_0(
                data["DimensionMappings"]
            )
        )
    else:
        out["dimension_mappings"] = []
    if data.get("MultiMeasureMappings") is not None:
        import capo_timestream_query.types.multi_measure_mappings

        out["multi_measure_mappings"] = (
            capo_timestream_query.types.multi_measure_mappings.deserialize_aws_json_1_0(
                data["MultiMeasureMappings"]
            )
        )
    if data.get("MixedMeasureMappings") is not None:
        import capo_timestream_query.types.mixed_measure_mapping_list

        out["mixed_measure_mappings"] = (
            capo_timestream_query.types.mixed_measure_mapping_list.deserialize_aws_json_1_0(
                data["MixedMeasureMappings"]
            )
        )
    if data.get("MeasureNameColumn") is not None:
        out["measure_name_column"] = data["MeasureNameColumn"]
    return out
