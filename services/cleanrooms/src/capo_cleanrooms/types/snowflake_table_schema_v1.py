"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SnowflakeTableSchemaV1``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.column_name
    import capo_cleanrooms.types.column_type_string


class SnowflakeTableSchemaV1(TypedDict, closed=True):
    column_name: "capo_cleanrooms.types.column_name.ColumnName"
    """<p> The column name.</p>"""
    column_type: "capo_cleanrooms.types.column_type_string.ColumnTypeString"
    """<p> The column's data type. Supported data types: <code>ARRAY</code>, <code>BIGINT</code>, <code>BOOLEAN</code>, <code>CHAR</code>, <code>DATE</code>, <code>DECIMAL</code>, <code>DOUBLE</code>, <code>DOUBLE PRECISION</code>, <code>FLOAT</code>, <code>FLOAT4</code>, <code>INT</code>, <code>INTEGER</code>, <code>MAP</code>, <code>NUMERIC</code>, <code>NUMBER</code>, <code>REAL</code>, <code>SMALLINT</code>, <code>STRING</code>, <code>TIMESTAMP</code>, <code>TIMESTAMP_LTZ</code>, <code>TIMESTAMP_NTZ</code>, <code>DATETIME</code>, <code>TINYINT</code>, <code>VARCHAR</code>, <code>TEXT</code>, <code>CHARACTER</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakeTableSchemaV1) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    out["columnType"] = value["column_type"]
    return out


def deserialize_json(data: dict) -> SnowflakeTableSchemaV1:
    out: SnowflakeTableSchemaV1 = {}  # type: ignore[typeddict-item]
    if data.get("columnName") is not None:
        out["column_name"] = data["columnName"]
    else:
        out["column_name"] = ""
    if data.get("columnType") is not None:
        out["column_type"] = data["columnType"]
    else:
        out["column_type"] = ""
    return out
