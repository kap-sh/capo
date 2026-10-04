"""Generated from Smithy shape ``com.amazonaws.glue#ListMaterializedViewRefreshTaskRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.page_size
    import capo_glue.types.token


class ListMaterializedViewRefreshTaskRunsRequest(TypedDict, closed=True):
    catalog_id: "capo_glue.types.catalog_id_string.CatalogIdString"
    """<p>The ID of the Data Catalog where the table resides. If none is supplied, the account ID is used by default.</p>"""
    database_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The database where the table resides.</p>"""
    table_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the materialized view.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum size of the response.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMaterializedViewRefreshTaskRunsRequest) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMaterializedViewRefreshTaskRunsRequest:
    out: ListMaterializedViewRefreshTaskRunsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    else:
        raise DeserializationError(
            "ListMaterializedViewRefreshTaskRunsRequest.catalog_id required"
        )
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
