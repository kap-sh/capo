"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListTableStorageOptimizersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.optimizer_type
    import capo_lakeformation.types.page_size
    import capo_lakeformation.types.token


class ListTableStorageOptimizersRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The Catalog ID of the table.</p>"""
    database_name: "capo_lakeformation.types.name_string.NameString"
    """<p>Name of the database where the table is present.</p>"""
    table_name: "capo_lakeformation.types.name_string.NameString"
    """<p>Name of the table.</p>"""
    storage_optimizer_type: NotRequired[
        "capo_lakeformation.types.optimizer_type.OptimizerType"
    ]
    """<p>The specific type of storage optimizers to list. The supported value is <code>compaction</code>.</p>"""
    max_results: NotRequired["capo_lakeformation.types.page_size.PageSize"]
    """<p>The number of storage optimizers to return on each call.</p>"""
    next_token: NotRequired["capo_lakeformation.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTableStorageOptimizersRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "storage_optimizer_type" in value:
        import capo_lakeformation.types.optimizer_type

        out["StorageOptimizerType"] = (
            capo_lakeformation.types.optimizer_type.serialize_json(
                value["storage_optimizer_type"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTableStorageOptimizersRequest:
    out: ListTableStorageOptimizersRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("StorageOptimizerType") is not None:
        import capo_lakeformation.types.optimizer_type

        out["storage_optimizer_type"] = (
            capo_lakeformation.types.optimizer_type.deserialize_json(
                data["StorageOptimizerType"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
