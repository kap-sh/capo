"""Generated from Smithy shape ``com.amazonaws.lakeformation#DataCellsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.column_names
    import capo_lakeformation.types.column_wildcard
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.row_filter
    import capo_lakeformation.types.version_string


class DataCellsFilter(TypedDict, closed=True):
    table_catalog_id: "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    """<p>The ID of the catalog to which the table belongs.</p>"""
    database_name: "capo_lakeformation.types.name_string.NameString"
    """<p>A database in the Glue Data Catalog.</p>"""
    table_name: "capo_lakeformation.types.name_string.NameString"
    """<p>A table in the database.</p>"""
    name: "capo_lakeformation.types.name_string.NameString"
    """<p>The name given by the user to the data filter cell.</p>"""
    row_filter: NotRequired["capo_lakeformation.types.row_filter.RowFilter"]
    """<p>A PartiQL predicate.</p>"""
    column_names: NotRequired["capo_lakeformation.types.column_names.ColumnNames"]
    """<p>A list of column names and/or nested column attributes. When specifying nested attributes, use a qualified dot (.) delimited format such as "address"."zip". Nested attributes within this list may not exceed a depth of 5.</p>"""
    column_wildcard: NotRequired[
        "capo_lakeformation.types.column_wildcard.ColumnWildcard"
    ]
    """<p>A wildcard with exclusions.</p> <p>You must specify either a <code>ColumnNames</code> list or the <code>ColumnWildCard</code>. </p>"""
    version_id: NotRequired["capo_lakeformation.types.version_string.VersionString"]
    """<p>The ID of the data cells filter version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataCellsFilter) -> dict:
    out: dict = {}
    out["TableCatalogId"] = value["table_catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    out["Name"] = value["name"]
    if "row_filter" in value:
        import capo_lakeformation.types.row_filter

        out["RowFilter"] = capo_lakeformation.types.row_filter.serialize_json(
            value["row_filter"]
        )
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
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> DataCellsFilter:
    out: DataCellsFilter = {}  # type: ignore[typeddict-item]
    if data.get("TableCatalogId") is not None:
        out["table_catalog_id"] = data["TableCatalogId"]
    else:
        raise DeserializationError("DataCellsFilter.table_catalog_id required")
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("DataCellsFilter.database_name required")
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("DataCellsFilter.table_name required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DataCellsFilter.name required")
    if data.get("RowFilter") is not None:
        import capo_lakeformation.types.row_filter

        out["row_filter"] = capo_lakeformation.types.row_filter.deserialize_json(
            data["RowFilter"]
        )
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
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
    return out
