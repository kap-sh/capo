"""Generated from Smithy shape ``com.amazonaws.athena#ColumnInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.boolean
    import capo_athena.types.column_nullable
    import capo_athena.types.integer
    import capo_athena.types.string


class ColumnInfo(TypedDict, closed=True):
    catalog_name: NotRequired["capo_athena.types.string.String"]
    """<p>The catalog to which the query results belong.</p>"""
    schema_name: NotRequired["capo_athena.types.string.String"]
    """<p>The schema name (database name) to which the query results belong.</p>"""
    table_name: NotRequired["capo_athena.types.string.String"]
    """<p>The table name for the query results.</p>"""
    name: "capo_athena.types.string.String"
    """<p>The name of the column.</p>"""
    label: NotRequired["capo_athena.types.string.String"]
    """<p>A column label.</p>"""
    type: "capo_athena.types.string.String"
    """<p>The data type of the column.</p>"""
    precision: "capo_athena.types.integer.Integer"
    """<p>For <code>DECIMAL</code> data types, specifies the total number of digits, up to 38. For performance reasons, we recommend up to 18 digits.</p>"""
    scale: "capo_athena.types.integer.Integer"
    """<p>For <code>DECIMAL</code> data types, specifies the total number of digits in the fractional part of the value. Defaults to 0.</p>"""
    nullable: NotRequired["capo_athena.types.column_nullable.ColumnNullable"]
    """<p>Unsupported constraint. This value always shows as <code>UNKNOWN</code>.</p>"""
    case_sensitive: "capo_athena.types.boolean.Boolean"
    """<p>Indicates whether values in the column are case-sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnInfo) -> dict:
    out: dict = {}
    if "catalog_name" in value:
        out["CatalogName"] = value["catalog_name"]
    if "schema_name" in value:
        out["SchemaName"] = value["schema_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    out["Name"] = value["name"]
    if "label" in value:
        out["Label"] = value["label"]
    out["Type"] = value["type"]
    out["Precision"] = value.get("precision", 0)
    out["Scale"] = value.get("scale", 0)
    if "nullable" in value:
        import capo_athena.types.column_nullable

        out["Nullable"] = capo_athena.types.column_nullable.serialize_aws_json_1_1(
            value["nullable"]
        )
    out["CaseSensitive"] = value.get("case_sensitive", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ColumnInfo:
    out: ColumnInfo = {}  # type: ignore[typeddict-item]
    if data.get("CatalogName") is not None:
        out["catalog_name"] = data["CatalogName"]
    if data.get("SchemaName") is not None:
        out["schema_name"] = data["SchemaName"]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    if data.get("Precision") is not None:
        out["precision"] = data["Precision"]
    else:
        out["precision"] = 0
    if data.get("Scale") is not None:
        out["scale"] = data["Scale"]
    else:
        out["scale"] = 0
    if data.get("Nullable") is not None:
        import capo_athena.types.column_nullable

        out["nullable"] = capo_athena.types.column_nullable.deserialize_aws_json_1_1(
            data["Nullable"]
        )
    if data.get("CaseSensitive") is not None:
        out["case_sensitive"] = data["CaseSensitive"]
    else:
        out["case_sensitive"] = False
    return out
