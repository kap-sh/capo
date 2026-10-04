"""Generated from Smithy shape ``com.amazonaws.glue#StartColumnStatisticsTaskRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.column_name_list
    import capo_glue.types.name_string
    import capo_glue.types.sample_size_percentage


class StartColumnStatisticsTaskRunRequest(TypedDict, closed=True):
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the database where the table resides.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the table to generate statistics.</p>"""
    column_name_list: NotRequired["capo_glue.types.column_name_list.ColumnNameList"]
    """<p>A list of the column names to generate statistics. If none is supplied, all column names for the table will be used by default.</p>"""
    role: "capo_glue.types.name_string.NameString"
    """<p>The IAM role that the service assumes to generate statistics.</p>"""
    sample_size: "capo_glue.types.sample_size_percentage.SampleSizePercentage"
    """<p>The percentage of rows used to generate statistics. If none is supplied, the entire table will be used to generate stats.</p>"""
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the table reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>"""
    security_configuration: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>Name of the security configuration that is used to encrypt CloudWatch logs for the column stats task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartColumnStatisticsTaskRunRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "column_name_list" in value:
        import capo_glue.types.column_name_list

        out["ColumnNameList"] = capo_glue.types.column_name_list.serialize_aws_json_1_1(
            value["column_name_list"]
        )
    out["Role"] = value["role"]
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


def deserialize_aws_json_1_1(data: dict) -> StartColumnStatisticsTaskRunRequest:
    out: StartColumnStatisticsTaskRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "StartColumnStatisticsTaskRunRequest.database_name required"
        )
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "StartColumnStatisticsTaskRunRequest.table_name required"
        )
    if data.get("ColumnNameList") is not None:
        import capo_glue.types.column_name_list

        out["column_name_list"] = (
            capo_glue.types.column_name_list.deserialize_aws_json_1_1(
                data["ColumnNameList"]
            )
        )
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    else:
        raise DeserializationError("StartColumnStatisticsTaskRunRequest.role required")
    if data.get("SampleSize") is not None:
        out["sample_size"] = float(data["SampleSize"])
    else:
        out["sample_size"] = 0
    if data.get("CatalogID") is not None:
        out["catalog_id"] = data["CatalogID"]
    if data.get("SecurityConfiguration") is not None:
        out["security_configuration"] = data["SecurityConfiguration"]
    return out
