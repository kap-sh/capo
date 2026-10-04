"""Generated from Smithy shape ``com.amazonaws.glue#StartMaterializedViewRefreshTaskRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.nullable_boolean


class StartMaterializedViewRefreshTaskRunRequest(TypedDict, closed=True):
    catalog_id: "capo_glue.types.catalog_id_string.CatalogIdString"
    """<p>The ID of the Data Catalog where the table reside. If none is supplied, the account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the database where the table resides.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the materialized view to run the refresh task for.</p>"""
    full_refresh: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether this is a full refresh of the task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMaterializedViewRefreshTaskRunRequest) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "full_refresh" in value:
        out["FullRefresh"] = value["full_refresh"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMaterializedViewRefreshTaskRunRequest:
    out: StartMaterializedViewRefreshTaskRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    else:
        raise DeserializationError(
            "StartMaterializedViewRefreshTaskRunRequest.catalog_id required"
        )
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "StartMaterializedViewRefreshTaskRunRequest.database_name required"
        )
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "StartMaterializedViewRefreshTaskRunRequest.table_name required"
        )
    if data.get("FullRefresh") is not None:
        out["full_refresh"] = data["FullRefresh"]
    return out
