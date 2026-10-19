"""Generated from Smithy shape ``com.amazonaws.quicksight#RelationalTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.input_column_list
    import capo_quicksight.types.relational_table_catalog
    import capo_quicksight.types.relational_table_name
    import capo_quicksight.types.relational_table_schema


class RelationalTable(TypedDict, closed=True):
    data_source_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the data source.</p>"""
    catalog: NotRequired[
        "capo_quicksight.types.relational_table_catalog.RelationalTableCatalog"
    ]
    """<p>The catalog associated with a table.</p>"""
    schema: NotRequired[
        "capo_quicksight.types.relational_table_schema.RelationalTableSchema"
    ]
    """<p>The schema name. This name applies to certain relational database engines.</p>"""
    name: "capo_quicksight.types.relational_table_name.RelationalTableName"
    """<p>The name of the relational table.</p>"""
    input_columns: "capo_quicksight.types.input_column_list.InputColumnList"
    """<p>The column schema of the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelationalTable) -> dict:
    out: dict = {}
    out["DataSourceArn"] = value["data_source_arn"]
    if "catalog" in value:
        out["Catalog"] = value["catalog"]
    if "schema" in value:
        out["Schema"] = value["schema"]
    out["Name"] = value["name"]
    import capo_quicksight.types.input_column_list

    out["InputColumns"] = capo_quicksight.types.input_column_list.serialize_json(
        value["input_columns"]
    )
    return out


def deserialize_json(data: dict) -> RelationalTable:
    out: RelationalTable = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceArn") is not None:
        out["data_source_arn"] = data["DataSourceArn"]
    else:
        out["data_source_arn"] = ""
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    if data.get("Schema") is not None:
        out["schema"] = data["Schema"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("InputColumns") is not None:
        import capo_quicksight.types.input_column_list

        out["input_columns"] = capo_quicksight.types.input_column_list.deserialize_json(
            data["InputColumns"]
        )
    else:
        out["input_columns"] = []
    return out
