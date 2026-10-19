"""Generated from Smithy shape ``com.amazonaws.glue#UpdateColumnStatisticsForPartitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.update_column_statistics_list
    import capo_glue.types.value_string_list


class UpdateColumnStatisticsForPartitionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the catalog database where the partitions reside.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the partitions' table.</p>"""
    partition_values: "capo_glue.types.value_string_list.ValueStringList"
    """<p>A list of partition values identifying the partition.</p>"""
    column_statistics_list: (
        "capo_glue.types.update_column_statistics_list.UpdateColumnStatisticsList"
    )
    """<p>A list of the column statistics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateColumnStatisticsForPartitionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_glue.types.value_string_list

    out["PartitionValues"] = capo_glue.types.value_string_list.serialize_aws_json_1_1(
        value["partition_values"]
    )
    import capo_glue.types.update_column_statistics_list

    out["ColumnStatisticsList"] = (
        capo_glue.types.update_column_statistics_list.serialize_aws_json_1_1(
            value["column_statistics_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateColumnStatisticsForPartitionRequest:
    out: UpdateColumnStatisticsForPartitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("PartitionValues") is not None:
        import capo_glue.types.value_string_list

        out["partition_values"] = (
            capo_glue.types.value_string_list.deserialize_aws_json_1_1(
                data["PartitionValues"]
            )
        )
    else:
        out["partition_values"] = []
    if data.get("ColumnStatisticsList") is not None:
        import capo_glue.types.update_column_statistics_list

        out["column_statistics_list"] = (
            capo_glue.types.update_column_statistics_list.deserialize_aws_json_1_1(
                data["ColumnStatisticsList"]
            )
        )
    else:
        out["column_statistics_list"] = []
    return out
