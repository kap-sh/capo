"""Generated from Smithy shape ``com.amazonaws.quicksight#LogicalTable``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.logical_table_alias
    import capo_quicksight.types.logical_table_source
    import capo_quicksight.types.transform_operation_list


class LogicalTable(TypedDict, closed=True):
    alias: "capo_quicksight.types.logical_table_alias.LogicalTableAlias"
    """<p>A display name for the logical table.</p>"""
    data_transforms: NotRequired[
        "capo_quicksight.types.transform_operation_list.TransformOperationList"
    ]
    """<p>Transform operations that act on this logical table. For this structure to be valid, only one of the attributes can be non-null. </p>"""
    source: "capo_quicksight.types.logical_table_source.LogicalTableSource"
    """<p>Source of this logical table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogicalTable) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    if "data_transforms" in value:
        import capo_quicksight.types.transform_operation_list

        out["DataTransforms"] = (
            capo_quicksight.types.transform_operation_list.serialize_json(
                value["data_transforms"]
            )
        )
    import capo_quicksight.types.logical_table_source

    out["Source"] = capo_quicksight.types.logical_table_source.serialize_json(
        value["source"]
    )
    return out


def deserialize_json(data: dict) -> LogicalTable:
    out: LogicalTable = {}  # type: ignore[typeddict-item]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("LogicalTable.alias required")
    if data.get("DataTransforms") is not None:
        import capo_quicksight.types.transform_operation_list

        out["data_transforms"] = (
            capo_quicksight.types.transform_operation_list.deserialize_json(
                data["DataTransforms"]
            )
        )
    if data.get("Source") is not None:
        import capo_quicksight.types.logical_table_source

        out["source"] = capo_quicksight.types.logical_table_source.deserialize_json(
            data["Source"]
        )
    else:
        raise DeserializationError("LogicalTable.source required")
    return out


def redact_sensitive(value: LogicalTable) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_transforms" in value:
        import capo_quicksight.types.transform_operation_list

        out["data_transforms"] = (
            capo_quicksight.types.transform_operation_list.redact_sensitive(
                value["data_transforms"]
            )
        )
    return out
