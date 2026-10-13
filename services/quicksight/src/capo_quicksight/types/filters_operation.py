"""Generated from Smithy shape ``com.amazonaws.quicksight#FiltersOperation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.filter_operation_list
    import capo_quicksight.types.transform_operation_alias
    import capo_quicksight.types.transform_operation_source


class FiltersOperation(TypedDict, closed=True):
    alias: "capo_quicksight.types.transform_operation_alias.TransformOperationAlias"
    """<p>Alias for this operation.</p>"""
    source: "capo_quicksight.types.transform_operation_source.TransformOperationSource"
    """<p>The source transform operation that provides input data for filtering.</p>"""
    filter_operations: "capo_quicksight.types.filter_operation_list.FilterOperationList"
    """<p>The list of filter operations to apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FiltersOperation) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    import capo_quicksight.types.transform_operation_source

    out["Source"] = capo_quicksight.types.transform_operation_source.serialize_json(
        value["source"]
    )
    import capo_quicksight.types.filter_operation_list

    out["FilterOperations"] = (
        capo_quicksight.types.filter_operation_list.serialize_json(
            value["filter_operations"]
        )
    )
    return out


def deserialize_json(data: dict) -> FiltersOperation:
    out: FiltersOperation = {}  # type: ignore[typeddict-item]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("FiltersOperation.alias required")
    if data.get("Source") is not None:
        import capo_quicksight.types.transform_operation_source

        out["source"] = (
            capo_quicksight.types.transform_operation_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("FiltersOperation.source required")
    if data.get("FilterOperations") is not None:
        import capo_quicksight.types.filter_operation_list

        out["filter_operations"] = (
            capo_quicksight.types.filter_operation_list.deserialize_json(
                data["FilterOperations"]
            )
        )
    else:
        raise DeserializationError("FiltersOperation.filter_operations required")
    return out


def redact_sensitive(value: FiltersOperation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filter_operations" in value:
        import capo_quicksight.types.filter_operation_list

        out["filter_operations"] = (
            capo_quicksight.types.filter_operation_list.redact_sensitive(
                value["filter_operations"]
            )
        )
    return out
