"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomSql``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.custom_sql_name
    import capo_quicksight.types.input_column_list
    import capo_quicksight.types.sql_query


class CustomSql(TypedDict, closed=True):
    data_source_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the data source.</p>"""
    name: "capo_quicksight.types.custom_sql_name.CustomSqlName"
    """<p>A display name for the SQL query result.</p>"""
    sql_query: "capo_quicksight.types.sql_query.SqlQuery"
    """<p>The SQL query.</p>"""
    columns: NotRequired["capo_quicksight.types.input_column_list.InputColumnList"]
    """<p>The column schema from the SQL query result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomSql) -> dict:
    out: dict = {}
    out["DataSourceArn"] = value["data_source_arn"]
    out["Name"] = value["name"]
    out["SqlQuery"] = value["sql_query"]
    if "columns" in value:
        import capo_quicksight.types.input_column_list

        out["Columns"] = capo_quicksight.types.input_column_list.serialize_json(
            value["columns"]
        )
    return out


def deserialize_json(data: dict) -> CustomSql:
    out: CustomSql = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceArn") is not None:
        out["data_source_arn"] = data["DataSourceArn"]
    else:
        raise DeserializationError("CustomSql.data_source_arn required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CustomSql.name required")
    if data.get("SqlQuery") is not None:
        out["sql_query"] = data["SqlQuery"]
    else:
        raise DeserializationError("CustomSql.sql_query required")
    if data.get("Columns") is not None:
        import capo_quicksight.types.input_column_list

        out["columns"] = capo_quicksight.types.input_column_list.deserialize_json(
            data["Columns"]
        )
    return out


def redact_sensitive(value: CustomSql) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sql_query" in value:
        out["sql_query"] = "*** Sensitive Data Redacted ***"
    return out
