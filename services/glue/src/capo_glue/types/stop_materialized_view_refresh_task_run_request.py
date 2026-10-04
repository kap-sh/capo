"""Generated from Smithy shape ``com.amazonaws.glue#StopMaterializedViewRefreshTaskRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string


class StopMaterializedViewRefreshTaskRunRequest(TypedDict, closed=True):
    catalog_id: "capo_glue.types.catalog_id_string.CatalogIdString"
    """<p>The ID of the Data Catalog where the table reside. If none is supplied, the account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the database where the table resides.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the materialized view.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopMaterializedViewRefreshTaskRunRequest) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopMaterializedViewRefreshTaskRunRequest:
    out: StopMaterializedViewRefreshTaskRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    else:
        raise DeserializationError(
            "StopMaterializedViewRefreshTaskRunRequest.catalog_id required"
        )
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "StopMaterializedViewRefreshTaskRunRequest.database_name required"
        )
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "StopMaterializedViewRefreshTaskRunRequest.table_name required"
        )
    return out
