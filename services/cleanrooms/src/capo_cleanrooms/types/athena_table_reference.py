"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AthenaTableReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.athena_catalog_name
    import capo_cleanrooms.types.athena_database_name
    import capo_cleanrooms.types.athena_output_location
    import capo_cleanrooms.types.athena_table_name
    import capo_cleanrooms.types.athena_work_group
    import capo_cleanrooms.types.commercial_region


class AthenaTableReference(TypedDict, closed=True):
    region: NotRequired["capo_cleanrooms.types.commercial_region.CommercialRegion"]
    """<p>The Amazon Web Services Region where the Athena table is located. This parameter is required to uniquely identify and access tables across different Regions.</p>"""
    work_group: "capo_cleanrooms.types.athena_work_group.AthenaWorkGroup"
    """<p> The workgroup of the Athena table reference.</p>"""
    output_location: NotRequired[
        "capo_cleanrooms.types.athena_output_location.AthenaOutputLocation"
    ]
    """<p> The output location for the Athena table.</p>"""
    database_name: "capo_cleanrooms.types.athena_database_name.AthenaDatabaseName"
    """<p> The database name.</p>"""
    table_name: "capo_cleanrooms.types.athena_table_name.AthenaTableName"
    """<p> The table reference.</p>"""
    catalog_name: NotRequired[
        "capo_cleanrooms.types.athena_catalog_name.AthenaCatalogName"
    ]
    """<p> The catalog name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AthenaTableReference) -> dict:
    out: dict = {}
    if "region" in value:
        import capo_cleanrooms.types.commercial_region

        out["region"] = capo_cleanrooms.types.commercial_region.serialize_json(
            value["region"]
        )
    out["workGroup"] = value["work_group"]
    if "output_location" in value:
        out["outputLocation"] = value["output_location"]
    out["databaseName"] = value["database_name"]
    out["tableName"] = value["table_name"]
    if "catalog_name" in value:
        out["catalogName"] = value["catalog_name"]
    return out


def deserialize_json(data: dict) -> AthenaTableReference:
    out: AthenaTableReference = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        import capo_cleanrooms.types.commercial_region

        out["region"] = capo_cleanrooms.types.commercial_region.deserialize_json(
            data["region"]
        )
    if data.get("workGroup") is not None:
        out["work_group"] = data["workGroup"]
    else:
        out["work_group"] = ""
    if data.get("outputLocation") is not None:
        out["output_location"] = data["outputLocation"]
    if data.get("databaseName") is not None:
        out["database_name"] = data["databaseName"]
    else:
        out["database_name"] = ""
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        out["table_name"] = ""
    if data.get("catalogName") is not None:
        out["catalog_name"] = data["catalogName"]
    return out
