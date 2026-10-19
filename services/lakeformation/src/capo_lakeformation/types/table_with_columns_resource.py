"""Generated from Smithy shape ``com.amazonaws.lakeformation#TableWithColumnsResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.column_names
    import capo_lakeformation.types.column_wildcard
    import capo_lakeformation.types.name_string


class TableWithColumnsResource(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, it is the account ID of the caller.</p>"""
    database_name: "capo_lakeformation.types.name_string.NameString"
    """<p>The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal. </p>"""
    name: "capo_lakeformation.types.name_string.NameString"
    """<p>The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal. </p>"""
    column_names: NotRequired["capo_lakeformation.types.column_names.ColumnNames"]
    """<p>The list of column names for the table. At least one of <code>ColumnNames</code> or <code>ColumnWildcard</code> is required.</p>"""
    column_wildcard: NotRequired[
        "capo_lakeformation.types.column_wildcard.ColumnWildcard"
    ]
    """<p>A wildcard specified by a <code>ColumnWildcard</code> object. At least one of <code>ColumnNames</code> or <code>ColumnWildcard</code> is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableWithColumnsResource) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["Name"] = value["name"]
    if "column_names" in value:
        import capo_lakeformation.types.column_names

        out["ColumnNames"] = capo_lakeformation.types.column_names.serialize_json(
            value["column_names"]
        )
    if "column_wildcard" in value:
        import capo_lakeformation.types.column_wildcard

        out["ColumnWildcard"] = capo_lakeformation.types.column_wildcard.serialize_json(
            value["column_wildcard"]
        )
    return out


def deserialize_json(data: dict) -> TableWithColumnsResource:
    out: TableWithColumnsResource = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ColumnNames") is not None:
        import capo_lakeformation.types.column_names

        out["column_names"] = capo_lakeformation.types.column_names.deserialize_json(
            data["ColumnNames"]
        )
    if data.get("ColumnWildcard") is not None:
        import capo_lakeformation.types.column_wildcard

        out["column_wildcard"] = (
            capo_lakeformation.types.column_wildcard.deserialize_json(
                data["ColumnWildcard"]
            )
        )
    return out
