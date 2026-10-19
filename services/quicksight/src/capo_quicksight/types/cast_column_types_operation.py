"""Generated from Smithy shape ``com.amazonaws.quicksight#CastColumnTypesOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.cast_column_type_operation_list
    import capo_quicksight.types.transform_operation_alias
    import capo_quicksight.types.transform_operation_source


class CastColumnTypesOperation(TypedDict, closed=True):
    alias: "capo_quicksight.types.transform_operation_alias.TransformOperationAlias"
    """<p>Alias for this operation.</p>"""
    source: "capo_quicksight.types.transform_operation_source.TransformOperationSource"
    """<p>The source transform operation that provides input data for the type casting.</p>"""
    cast_column_type_operations: "capo_quicksight.types.cast_column_type_operation_list.CastColumnTypeOperationList"
    """<p>The list of column type casting operations to perform.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CastColumnTypesOperation) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    import capo_quicksight.types.transform_operation_source

    out["Source"] = capo_quicksight.types.transform_operation_source.serialize_json(
        value["source"]
    )
    import capo_quicksight.types.cast_column_type_operation_list

    out["CastColumnTypeOperations"] = (
        capo_quicksight.types.cast_column_type_operation_list.serialize_json(
            value["cast_column_type_operations"]
        )
    )
    return out


def deserialize_json(data: dict) -> CastColumnTypesOperation:
    out: CastColumnTypesOperation = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("CastColumnTypesOperation.source required")
    if data.get("CastColumnTypeOperations") is not None:
        import capo_quicksight.types.cast_column_type_operation_list

        out["cast_column_type_operations"] = (
            capo_quicksight.types.cast_column_type_operation_list.deserialize_json(
                data["CastColumnTypeOperations"]
            )
        )
    else:
        out["cast_column_type_operations"] = []
    return out
