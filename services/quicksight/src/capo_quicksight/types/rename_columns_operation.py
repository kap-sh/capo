"""Generated from Smithy shape ``com.amazonaws.quicksight#RenameColumnsOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.rename_column_operation_list
    import capo_quicksight.types.transform_operation_alias
    import capo_quicksight.types.transform_operation_source


class RenameColumnsOperation(TypedDict, closed=True):
    alias: "capo_quicksight.types.transform_operation_alias.TransformOperationAlias"
    """<p>Alias for this operation.</p>"""
    source: "capo_quicksight.types.transform_operation_source.TransformOperationSource"
    """<p>The source transform operation that provides input data for column renaming.</p>"""
    rename_column_operations: (
        "capo_quicksight.types.rename_column_operation_list.RenameColumnOperationList"
    )
    """<p>The list of column rename operations to perform, specifying old and new column names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RenameColumnsOperation) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    import capo_quicksight.types.transform_operation_source

    out["Source"] = capo_quicksight.types.transform_operation_source.serialize_json(
        value["source"]
    )
    import capo_quicksight.types.rename_column_operation_list

    out["RenameColumnOperations"] = (
        capo_quicksight.types.rename_column_operation_list.serialize_json(
            value["rename_column_operations"]
        )
    )
    return out


def deserialize_json(data: dict) -> RenameColumnsOperation:
    out: RenameColumnsOperation = {}  # type: ignore[typeddict-item]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    else:
        out["alias"] = ""
    if data.get("Source") is not None:
        import capo_quicksight.types.transform_operation_source

        out["source"] = (
            capo_quicksight.types.transform_operation_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("RenameColumnsOperation.source required")
    if data.get("RenameColumnOperations") is not None:
        import capo_quicksight.types.rename_column_operation_list

        out["rename_column_operations"] = (
            capo_quicksight.types.rename_column_operation_list.deserialize_json(
                data["RenameColumnOperations"]
            )
        )
    else:
        out["rename_column_operations"] = []
    return out
