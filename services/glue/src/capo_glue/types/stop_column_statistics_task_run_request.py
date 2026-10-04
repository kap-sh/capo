"""Generated from Smithy shape ``com.amazonaws.glue#StopColumnStatisticsTaskRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.database_name
    import capo_glue.types.name_string


class StopColumnStatisticsTaskRunRequest(TypedDict, closed=True):
    database_name: "capo_glue.types.database_name.DatabaseName"
    """<p>The name of the database where the table resides.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the table.</p>"""
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the table resides. If none is supplied, the Amazon Web Services account ID is used by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopColumnStatisticsTaskRunRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "catalog_id" in value:
        out["CatalogID"] = value["catalog_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopColumnStatisticsTaskRunRequest:
    out: StopColumnStatisticsTaskRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "StopColumnStatisticsTaskRunRequest.database_name required"
        )
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "StopColumnStatisticsTaskRunRequest.table_name required"
        )
    if data.get("CatalogID") is not None:
        out["catalog_id"] = data["CatalogID"]
    return out
