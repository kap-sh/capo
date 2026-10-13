"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableFieldCollapseStateTarget``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_path_value_list
    import capo_quicksight.types.string


class PivotTableFieldCollapseStateTarget(TypedDict, closed=True):
    field_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The field ID of the pivot table that the collapse state needs to be set to.</p>"""
    field_data_path_values: NotRequired[
        "capo_quicksight.types.data_path_value_list.DataPathValueList"
    ]
    """<p>The data path of the pivot table's header. Used to set the collapse state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableFieldCollapseStateTarget) -> dict:
    out: dict = {}
    if "field_id" in value:
        out["FieldId"] = value["field_id"]
    if "field_data_path_values" in value:
        import capo_quicksight.types.data_path_value_list

        out["FieldDataPathValues"] = (
            capo_quicksight.types.data_path_value_list.serialize_json(
                value["field_data_path_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableFieldCollapseStateTarget:
    out: PivotTableFieldCollapseStateTarget = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    if data.get("FieldDataPathValues") is not None:
        import capo_quicksight.types.data_path_value_list

        out["field_data_path_values"] = (
            capo_quicksight.types.data_path_value_list.deserialize_json(
                data["FieldDataPathValues"]
            )
        )
    return out


def redact_sensitive(value: PivotTableFieldCollapseStateTarget) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_data_path_values" in value:
        import capo_quicksight.types.data_path_value_list

        out["field_data_path_values"] = (
            capo_quicksight.types.data_path_value_list.redact_sensitive(
                value["field_data_path_values"]
            )
        )
    return out
