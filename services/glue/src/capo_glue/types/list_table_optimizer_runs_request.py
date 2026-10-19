"""Generated from Smithy shape ``com.amazonaws.glue#ListTableOptimizerRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.list_table_optimizer_runs_token
    import capo_glue.types.max_list_table_optimizer_runs_token_results
    import capo_glue.types.name_string
    import capo_glue.types.table_optimizer_type


class ListTableOptimizerRunsRequest(TypedDict, closed=True):
    catalog_id: "capo_glue.types.catalog_id_string.CatalogIdString"
    """<p>The Catalog ID of the table.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the database in the catalog in which the table resides.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the table.</p>"""
    type: "capo_glue.types.table_optimizer_type.TableOptimizerType"
    """<p>The type of table optimizer.</p>"""
    max_results: NotRequired[
        "capo_glue.types.max_list_table_optimizer_runs_token_results.MaxListTableOptimizerRunsTokenResults"
    ]
    """<p>The maximum number of optimizer runs to return on each call.</p>"""
    next_token: NotRequired[
        "capo_glue.types.list_table_optimizer_runs_token.ListTableOptimizerRunsToken"
    ]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTableOptimizerRunsRequest) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_glue.types.table_optimizer_type

    out["Type"] = capo_glue.types.table_optimizer_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTableOptimizerRunsRequest:
    out: ListTableOptimizerRunsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    else:
        out["catalog_id"] = ""
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("Type") is not None:
        import capo_glue.types.table_optimizer_type

        out["type"] = capo_glue.types.table_optimizer_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_glue.types.table_optimizer_type.TableOptimizerType", ""
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
