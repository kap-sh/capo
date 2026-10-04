"""Generated from Smithy shape ``com.amazonaws.glue#ViewDefinitionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.arn_string
    import capo_glue.types.last_refresh_type
    import capo_glue.types.nullable_boolean
    import capo_glue.types.refresh_seconds
    import capo_glue.types.spark_pipeline_info_map
    import capo_glue.types.sub_objects_statistics_list
    import capo_glue.types.table_version_id
    import capo_glue.types.version_string
    import capo_glue.types.view_representation_input_list
    import capo_glue.types.view_sub_object_version_ids_list
    import capo_glue.types.view_sub_objects_list


class ViewDefinitionInput(TypedDict, closed=True):
    is_protected: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>You can set this flag as true to instruct the engine not to push user-provided operations into the logical plan of the view during query planning. However, setting this flag does not guarantee that the engine will comply. Refer to the engine's documentation to understand the guarantees provided, if any.</p>"""
    is_managed: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether the materialized view is managed by Glue.</p>"""
    definer: NotRequired["capo_glue.types.arn_string.ArnString"]
    """<p>The definer of a view in SQL.</p>"""
    representations: NotRequired[
        "capo_glue.types.view_representation_input_list.ViewRepresentationInputList"
    ]
    """<p>A list of structures that contains the dialect of the view, and the query that defines the view.</p>"""
    view_version_id: "capo_glue.types.table_version_id.TableVersionId"
    """<p>The ID value that identifies this view's version. For materialized views, the version ID is the Apache Iceberg table's snapshot ID. </p>"""
    view_version_token: NotRequired["capo_glue.types.version_string.VersionString"]
    """<p>The version ID of the Apache Iceberg table.</p>"""
    refresh_seconds: NotRequired["capo_glue.types.refresh_seconds.RefreshSeconds"]
    """<p>Auto refresh interval in seconds for the materialized view. If not specified, the view will not automatically refresh.</p>"""
    last_refresh_type: NotRequired["capo_glue.types.last_refresh_type.LastRefreshType"]
    """<p>The type of the materialized view's last refresh. Valid values: <code>Full</code>, <code>Incremental</code>.</p>"""
    sub_objects: NotRequired["capo_glue.types.view_sub_objects_list.ViewSubObjectsList"]
    """<p>A list of base table ARNs that make up the view.</p>"""
    sub_object_version_ids: NotRequired[
        "capo_glue.types.view_sub_object_version_ids_list.ViewSubObjectVersionIdsList"
    ]
    """<p>List of the Apache Iceberg table versions referenced by the materialized view.</p>"""
    sub_objects_statistics: NotRequired[
        "capo_glue.types.sub_objects_statistics_list.SubObjectsStatisticsList"
    ]
    """<p>Statistics for each sub-object referenced by the materialized view, such as the source type, Glue version ID, and the partition, file, and byte counts. Each entry describes one sub-object, identified by its source type.</p>"""
    spark_pipeline_info: NotRequired[
        "capo_glue.types.spark_pipeline_info_map.SparkPipelineInfoMap"
    ]
    """<p>A map of key-value pairs containing Spark Declarative Pipelines (SDP) information for the materialized view.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViewDefinitionInput) -> dict:
    out: dict = {}
    if "is_protected" in value:
        out["IsProtected"] = value["is_protected"]
    if "is_managed" in value:
        out["IsManaged"] = value["is_managed"]
    if "definer" in value:
        out["Definer"] = value["definer"]
    if "representations" in value:
        import capo_glue.types.view_representation_input_list

        out["Representations"] = (
            capo_glue.types.view_representation_input_list.serialize_aws_json_1_1(
                value["representations"]
            )
        )
    out["ViewVersionId"] = value.get("view_version_id", 0)
    if "view_version_token" in value:
        out["ViewVersionToken"] = value["view_version_token"]
    if "refresh_seconds" in value:
        out["RefreshSeconds"] = value["refresh_seconds"]
    if "last_refresh_type" in value:
        import capo_glue.types.last_refresh_type

        out["LastRefreshType"] = (
            capo_glue.types.last_refresh_type.serialize_aws_json_1_1(
                value["last_refresh_type"]
            )
        )
    if "sub_objects" in value:
        import capo_glue.types.view_sub_objects_list

        out["SubObjects"] = (
            capo_glue.types.view_sub_objects_list.serialize_aws_json_1_1(
                value["sub_objects"]
            )
        )
    if "sub_object_version_ids" in value:
        import capo_glue.types.view_sub_object_version_ids_list

        out["SubObjectVersionIds"] = (
            capo_glue.types.view_sub_object_version_ids_list.serialize_aws_json_1_1(
                value["sub_object_version_ids"]
            )
        )
    if "sub_objects_statistics" in value:
        import capo_glue.types.sub_objects_statistics_list

        out["SubObjectsStatistics"] = (
            capo_glue.types.sub_objects_statistics_list.serialize_aws_json_1_1(
                value["sub_objects_statistics"]
            )
        )
    if "spark_pipeline_info" in value:
        import capo_glue.types.spark_pipeline_info_map

        out["SparkPipelineInfo"] = (
            capo_glue.types.spark_pipeline_info_map.serialize_aws_json_1_1(
                value["spark_pipeline_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ViewDefinitionInput:
    out: ViewDefinitionInput = {}  # type: ignore[typeddict-item]
    if data.get("IsProtected") is not None:
        out["is_protected"] = data["IsProtected"]
    if data.get("IsManaged") is not None:
        out["is_managed"] = data["IsManaged"]
    if data.get("Definer") is not None:
        out["definer"] = data["Definer"]
    if data.get("Representations") is not None:
        import capo_glue.types.view_representation_input_list

        out["representations"] = (
            capo_glue.types.view_representation_input_list.deserialize_aws_json_1_1(
                data["Representations"]
            )
        )
    if data.get("ViewVersionId") is not None:
        out["view_version_id"] = data["ViewVersionId"]
    else:
        out["view_version_id"] = 0
    if data.get("ViewVersionToken") is not None:
        out["view_version_token"] = data["ViewVersionToken"]
    if data.get("RefreshSeconds") is not None:
        out["refresh_seconds"] = data["RefreshSeconds"]
    if data.get("LastRefreshType") is not None:
        import capo_glue.types.last_refresh_type

        out["last_refresh_type"] = (
            capo_glue.types.last_refresh_type.deserialize_aws_json_1_1(
                data["LastRefreshType"]
            )
        )
    if data.get("SubObjects") is not None:
        import capo_glue.types.view_sub_objects_list

        out["sub_objects"] = (
            capo_glue.types.view_sub_objects_list.deserialize_aws_json_1_1(
                data["SubObjects"]
            )
        )
    if data.get("SubObjectVersionIds") is not None:
        import capo_glue.types.view_sub_object_version_ids_list

        out["sub_object_version_ids"] = (
            capo_glue.types.view_sub_object_version_ids_list.deserialize_aws_json_1_1(
                data["SubObjectVersionIds"]
            )
        )
    if data.get("SubObjectsStatistics") is not None:
        import capo_glue.types.sub_objects_statistics_list

        out["sub_objects_statistics"] = (
            capo_glue.types.sub_objects_statistics_list.deserialize_aws_json_1_1(
                data["SubObjectsStatistics"]
            )
        )
    if data.get("SparkPipelineInfo") is not None:
        import capo_glue.types.spark_pipeline_info_map

        out["spark_pipeline_info"] = (
            capo_glue.types.spark_pipeline_info_map.deserialize_aws_json_1_1(
                data["SparkPipelineInfo"]
            )
        )
    return out
