"""Generated from Smithy shape ``com.amazonaws.quicksight#SaaSTable``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.input_column_list
    import capo_quicksight.types.table_path_element_list


class SaaSTable(TypedDict, closed=True):
    data_source_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the SaaS data source.</p>"""
    table_path: "capo_quicksight.types.table_path_element_list.TablePathElementList"
    """<p>The hierarchical path to the table within the SaaS data source.</p>"""
    input_columns: "capo_quicksight.types.input_column_list.InputColumnList"
    """<p>The list of input columns available from the SaaS table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SaaSTable) -> dict:
    out: dict = {}
    out["DataSourceArn"] = value["data_source_arn"]
    import capo_quicksight.types.table_path_element_list

    out["TablePath"] = capo_quicksight.types.table_path_element_list.serialize_json(
        value["table_path"]
    )
    import capo_quicksight.types.input_column_list

    out["InputColumns"] = capo_quicksight.types.input_column_list.serialize_json(
        value["input_columns"]
    )
    return out


def deserialize_json(data: dict) -> SaaSTable:
    out: SaaSTable = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceArn") is not None:
        out["data_source_arn"] = data["DataSourceArn"]
    else:
        out["data_source_arn"] = ""
    if data.get("TablePath") is not None:
        import capo_quicksight.types.table_path_element_list

        out["table_path"] = (
            capo_quicksight.types.table_path_element_list.deserialize_json(
                data["TablePath"]
            )
        )
    else:
        out["table_path"] = []
    if data.get("InputColumns") is not None:
        import capo_quicksight.types.input_column_list

        out["input_columns"] = capo_quicksight.types.input_column_list.deserialize_json(
            data["InputColumns"]
        )
    else:
        out["input_columns"] = []
    return out
