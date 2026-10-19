"""Generated from Smithy shape ``com.amazonaws.quicksight#AppendOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.appended_column_list
    import capo_quicksight.types.transform_operation_alias
    import capo_quicksight.types.transform_operation_source


class AppendOperation(TypedDict, closed=True):
    alias: "capo_quicksight.types.transform_operation_alias.TransformOperationAlias"
    """<p>Alias for this operation.</p>"""
    first_source: NotRequired[
        "capo_quicksight.types.transform_operation_source.TransformOperationSource"
    ]
    """<p>The first data source to be included in the append operation.</p>"""
    second_source: NotRequired[
        "capo_quicksight.types.transform_operation_source.TransformOperationSource"
    ]
    """<p>The second data source to be appended to the first source.</p>"""
    appended_columns: "capo_quicksight.types.appended_column_list.AppendedColumnList"
    """<p>The list of columns to include in the appended result, mapping columns from both sources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppendOperation) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    if "first_source" in value:
        import capo_quicksight.types.transform_operation_source

        out["FirstSource"] = (
            capo_quicksight.types.transform_operation_source.serialize_json(
                value["first_source"]
            )
        )
    if "second_source" in value:
        import capo_quicksight.types.transform_operation_source

        out["SecondSource"] = (
            capo_quicksight.types.transform_operation_source.serialize_json(
                value["second_source"]
            )
        )
    import capo_quicksight.types.appended_column_list

    out["AppendedColumns"] = capo_quicksight.types.appended_column_list.serialize_json(
        value["appended_columns"]
    )
    return out


def deserialize_json(data: dict) -> AppendOperation:
    out: AppendOperation = {}  # type: ignore[typeddict-item]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    else:
        out["alias"] = ""
    if data.get("FirstSource") is not None:
        import capo_quicksight.types.transform_operation_source

        out["first_source"] = (
            capo_quicksight.types.transform_operation_source.deserialize_json(
                data["FirstSource"]
            )
        )
    if data.get("SecondSource") is not None:
        import capo_quicksight.types.transform_operation_source

        out["second_source"] = (
            capo_quicksight.types.transform_operation_source.deserialize_json(
                data["SecondSource"]
            )
        )
    if data.get("AppendedColumns") is not None:
        import capo_quicksight.types.appended_column_list

        out["appended_columns"] = (
            capo_quicksight.types.appended_column_list.deserialize_json(
                data["AppendedColumns"]
            )
        )
    else:
        out["appended_columns"] = []
    return out
