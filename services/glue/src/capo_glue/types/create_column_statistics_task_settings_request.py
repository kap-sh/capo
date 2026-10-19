"""Generated from Smithy shape ``com.amazonaws.glue#CreateColumnStatisticsTaskSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.column_name_list
    import capo_glue.types.cron_expression
    import capo_glue.types.name_string
    import capo_glue.types.sample_size_percentage
    import capo_glue.types.tags_map


class CreateColumnStatisticsTaskSettingsRequest(TypedDict, closed=True):
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the database where the table resides.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the table for which to generate column statistics.</p>"""
    role: "capo_glue.types.name_string.NameString"
    """<p>The role used for running the column statistics.</p>"""
    schedule: NotRequired["capo_glue.types.cron_expression.CronExpression"]
    """<p>A schedule for running the column statistics, specified in CRON syntax.</p>"""
    column_name_list: NotRequired["capo_glue.types.column_name_list.ColumnNameList"]
    """<p>A list of column names for which to run statistics.</p>"""
    sample_size: NotRequired[
        "capo_glue.types.sample_size_percentage.SampleSizePercentage"
    ]
    """<p>The percentage of data to sample.</p>"""
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the database resides.</p>"""
    security_configuration: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>Name of the security configuration that is used to encrypt CloudWatch logs.</p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>A map of tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateColumnStatisticsTaskSettingsRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    out["Role"] = value["role"]
    if "schedule" in value:
        out["Schedule"] = value["schedule"]
    if "column_name_list" in value:
        import capo_glue.types.column_name_list

        out["ColumnNameList"] = capo_glue.types.column_name_list.serialize_aws_json_1_1(
            value["column_name_list"]
        )
    if "sample_size" in value:
        out["SampleSize"] = (
            "NaN"
            if value["sample_size"] != value["sample_size"]
            else "Infinity"
            if value["sample_size"] == float("inf")
            else "-Infinity"
            if value["sample_size"] == float("-inf")
            else value["sample_size"]
        )
    if "catalog_id" in value:
        out["CatalogID"] = value["catalog_id"]
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateColumnStatisticsTaskSettingsRequest:
    out: CreateColumnStatisticsTaskSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    else:
        out["role"] = ""
    if data.get("Schedule") is not None:
        out["schedule"] = data["Schedule"]
    if data.get("ColumnNameList") is not None:
        import capo_glue.types.column_name_list

        out["column_name_list"] = (
            capo_glue.types.column_name_list.deserialize_aws_json_1_1(
                data["ColumnNameList"]
            )
        )
    if data.get("SampleSize") is not None:
        out["sample_size"] = float(data["SampleSize"])
    if data.get("CatalogID") is not None:
        out["catalog_id"] = data["CatalogID"]
    if data.get("SecurityConfiguration") is not None:
        out["security_configuration"] = data["SecurityConfiguration"]
    if data.get("Tags") is not None:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
