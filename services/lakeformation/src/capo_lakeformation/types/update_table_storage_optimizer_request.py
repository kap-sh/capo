"""Generated from Smithy shape ``com.amazonaws.lakeformation#UpdateTableStorageOptimizerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.storage_optimizer_config_map


class UpdateTableStorageOptimizerRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The Catalog ID of the table.</p>"""
    database_name: "capo_lakeformation.types.name_string.NameString"
    """<p>Name of the database where the table is present.</p>"""
    table_name: "capo_lakeformation.types.name_string.NameString"
    """<p>Name of the table for which to enable the storage optimizer.</p>"""
    storage_optimizer_config: "capo_lakeformation.types.storage_optimizer_config_map.StorageOptimizerConfigMap"
    """<p>Name of the configuration for the storage optimizer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTableStorageOptimizerRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_lakeformation.types.storage_optimizer_config_map

    out["StorageOptimizerConfig"] = (
        capo_lakeformation.types.storage_optimizer_config_map.serialize_json(
            value["storage_optimizer_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateTableStorageOptimizerRequest:
    out: UpdateTableStorageOptimizerRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("StorageOptimizerConfig") is not None:
        import capo_lakeformation.types.storage_optimizer_config_map

        out["storage_optimizer_config"] = (
            capo_lakeformation.types.storage_optimizer_config_map.deserialize_json(
                data["StorageOptimizerConfig"]
            )
        )
    else:
        out["storage_optimizer_config"] = {}
    return out
