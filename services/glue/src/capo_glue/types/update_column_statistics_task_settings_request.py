"""Generated from Smithy shape ``com.amazonaws.glue#UpdateColumnStatisticsTaskSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.column_name_list
    import capo_glue.types.cron_expression
    import capo_glue.types.name_string
    import capo_glue.types.sample_size_percentage


class UpdateColumnStatisticsTaskSettingsRequest(TypedDict, closed=True):
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the database where the table resides.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the table for which to generate column statistics.</p>"""
    role: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The role used for running the column statistics.</p>"""
    schedule: NotRequired["capo_glue.types.cron_expression.CronExpression"]
    """<p>A schedule for running the column statistics, specified in CRON syntax.</p>"""
    column_name_list: NotRequired["capo_glue.types.column_name_list.ColumnNameList"]
    """<p>A list of column names for which to run statistics.</p>"""
    sample_size: "capo_glue.types.sample_size_percentage.SampleSizePercentage"
    """<p>The percentage of data to sample.</p>"""
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the database resides.</p>"""
    security_configuration: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>Name of the security configuration that is used to encrypt CloudWatch logs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateColumnStatisticsTaskSettingsRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "role" in value:
        out["Role"] = value["role"]
    if "schedule" in value:
        out["Schedule"] = value["schedule"]
    if "column_name_list" in value:
        import capo_glue.types.column_name_list

        out["ColumnNameList"] = capo_glue.types.column_name_list.serialize_aws_json_1_1(
            value["column_name_list"]
        )
    out["SampleSize"] = (
        "NaN"
        if value.get("sample_size", 0) != value.get("sample_size", 0)
        else "Infinity"
        if value.get("sample_size", 0) == float("inf")
        else "-Infinity"
        if value.get("sample_size", 0) == float("-inf")
        else value.get("sample_size", 0)
    )
    if "catalog_id" in value:
        out["CatalogID"] = value["catalog_id"]
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateColumnStatisticsTaskSettingsRequest:
    out: UpdateColumnStatisticsTaskSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "UpdateColumnStatisticsTaskSettingsRequest.database_name required"
        )
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "UpdateColumnStatisticsTaskSettingsRequest.table_name required"
        )
    if data.get("Role") is not None:
        out["role"] = data["Role"]
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
    else:
        out["sample_size"] = 0
    if data.get("CatalogID") is not None:
        out["catalog_id"] = data["CatalogID"]
    if data.get("SecurityConfiguration") is not None:
        out["security_configuration"] = data["SecurityConfiguration"]
    return out
