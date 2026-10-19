"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetDataCellsFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.name_string


class GetDataCellsFilterRequest(TypedDict, closed=True):
    table_catalog_id: "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    """<p>The ID of the catalog to which the table belongs.</p>"""
    database_name: "capo_lakeformation.types.name_string.NameString"
    """<p>A database in the Glue Data Catalog.</p>"""
    table_name: "capo_lakeformation.types.name_string.NameString"
    """<p>A table in the database.</p>"""
    name: "capo_lakeformation.types.name_string.NameString"
    """<p>The name given by the user to the data filter cell.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataCellsFilterRequest) -> dict:
    out: dict = {}
    out["TableCatalogId"] = value["table_catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> GetDataCellsFilterRequest:
    out: GetDataCellsFilterRequest = {}  # type: ignore[typeddict-item]
    if data.get("TableCatalogId") is not None:
        out["table_catalog_id"] = data["TableCatalogId"]
    else:
        out["table_catalog_id"] = ""
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
