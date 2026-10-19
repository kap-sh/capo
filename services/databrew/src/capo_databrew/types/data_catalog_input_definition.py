"""Generated from Smithy shape ``com.amazonaws.databrew#DataCatalogInputDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.catalog_id
    import capo_databrew.types.database_name
    import capo_databrew.types.s3_location
    import capo_databrew.types.table_name


class DataCatalogInputDefinition(TypedDict, closed=True):
    catalog_id: NotRequired["capo_databrew.types.catalog_id.CatalogId"]
    """<p>The unique identifier of the Amazon Web Services account that holds the Data Catalog that stores the data.</p>"""
    database_name: "capo_databrew.types.database_name.DatabaseName"
    """<p>The name of a database in the Data Catalog.</p>"""
    table_name: "capo_databrew.types.table_name.TableName"
    """<p>The name of a database table in the Data Catalog. This table corresponds to a DataBrew dataset.</p>"""
    temp_directory: NotRequired["capo_databrew.types.s3_location.S3Location"]
    """<p>Represents an Amazon location where DataBrew can store intermediate results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataCatalogInputDefinition) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "temp_directory" in value:
        import capo_databrew.types.s3_location

        out["TempDirectory"] = capo_databrew.types.s3_location.serialize_json(
            value["temp_directory"]
        )
    return out


def deserialize_json(data: dict) -> DataCatalogInputDefinition:
    out: DataCatalogInputDefinition = {}  # type: ignore[typeddict-item]
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
    if data.get("TempDirectory") is not None:
        import capo_databrew.types.s3_location

        out["temp_directory"] = capo_databrew.types.s3_location.deserialize_json(
            data["TempDirectory"]
        )
    return out
