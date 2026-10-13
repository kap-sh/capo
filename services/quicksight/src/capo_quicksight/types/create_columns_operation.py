"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateColumnsOperation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.calculated_column_list
    import capo_quicksight.types.transform_operation_alias
    import capo_quicksight.types.transform_operation_source


class CreateColumnsOperation(TypedDict, closed=True):
    alias: NotRequired[
        "capo_quicksight.types.transform_operation_alias.TransformOperationAlias"
    ]
    """<p>Alias for this operation.</p>"""
    source: NotRequired[
        "capo_quicksight.types.transform_operation_source.TransformOperationSource"
    ]
    """<p>The source transform operation that provides input data for creating new calculated columns.</p>"""
    columns: "capo_quicksight.types.calculated_column_list.CalculatedColumnList"
    """<p>Calculated columns to create.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateColumnsOperation) -> dict:
    out: dict = {}
    if "alias" in value:
        out["Alias"] = value["alias"]
    if "source" in value:
        import capo_quicksight.types.transform_operation_source

        out["Source"] = capo_quicksight.types.transform_operation_source.serialize_json(
            value["source"]
        )
    import capo_quicksight.types.calculated_column_list

    out["Columns"] = capo_quicksight.types.calculated_column_list.serialize_json(
        value["columns"]
    )
    return out


def deserialize_json(data: dict) -> CreateColumnsOperation:
    out: CreateColumnsOperation = {}  # type: ignore[typeddict-item]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    if data.get("Source") is not None:
        import capo_quicksight.types.transform_operation_source

        out["source"] = (
            capo_quicksight.types.transform_operation_source.deserialize_json(
                data["Source"]
            )
        )
    if data.get("Columns") is not None:
        import capo_quicksight.types.calculated_column_list

        out["columns"] = capo_quicksight.types.calculated_column_list.deserialize_json(
            data["Columns"]
        )
    else:
        raise DeserializationError("CreateColumnsOperation.columns required")
    return out


def redact_sensitive(value: CreateColumnsOperation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "columns" in value:
        import capo_quicksight.types.calculated_column_list

        out["columns"] = capo_quicksight.types.calculated_column_list.redact_sensitive(
            value["columns"]
        )
    return out
