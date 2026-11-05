"""Generated from Smithy shape ``com.amazonaws.s3tables#GlueTableSource``."""

from typing_extensions import TypedDict


class GlueTableSource(TypedDict, closed=True):
    catalog_id: "str"
    """<p>The ID of the Data Catalog that contains the table. It must be your account ID.</p>"""
    database_name: "str"
    """<p>The name of the database that contains the table.</p>"""
    table_name: "str"
    """<p>The name of the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlueTableSource) -> dict:
    out: dict = {}
    out["catalogId"] = value["catalog_id"]
    out["databaseName"] = value["database_name"]
    out["tableName"] = value["table_name"]
    return out


def deserialize_json(data: dict) -> GlueTableSource:
    out: GlueTableSource = {}  # type: ignore[typeddict-item]
    if data.get("catalogId") is not None:
        out["catalog_id"] = data["catalogId"]
    else:
        out["catalog_id"] = ""
    if data.get("databaseName") is not None:
        out["database_name"] = data["databaseName"]
    else:
        out["database_name"] = ""
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        out["table_name"] = ""
    return out
