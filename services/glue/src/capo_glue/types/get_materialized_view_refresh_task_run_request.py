"""Generated from Smithy shape ``com.amazonaws.glue#GetMaterializedViewRefreshTaskRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.uui_dv4


class GetMaterializedViewRefreshTaskRunRequest(TypedDict, closed=True):
    catalog_id: "capo_glue.types.catalog_id_string.CatalogIdString"
    """<p>The ID of the Data Catalog where the table resides. If none is supplied, the account ID is used by default.</p>"""
    materialized_view_refresh_task_run_id: "capo_glue.types.uui_dv4.UUIDv4"
    """<p>The identifier for the particular materialized view refresh task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMaterializedViewRefreshTaskRunRequest) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    out["MaterializedViewRefreshTaskRunId"] = value[
        "materialized_view_refresh_task_run_id"
    ]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMaterializedViewRefreshTaskRunRequest:
    out: GetMaterializedViewRefreshTaskRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    else:
        raise DeserializationError(
            "GetMaterializedViewRefreshTaskRunRequest.catalog_id required"
        )
    if data.get("MaterializedViewRefreshTaskRunId") is not None:
        out["materialized_view_refresh_task_run_id"] = data[
            "MaterializedViewRefreshTaskRunId"
        ]
    else:
        raise DeserializationError(
            "GetMaterializedViewRefreshTaskRunRequest.materialized_view_refresh_task_run_id required"
        )
    return out
