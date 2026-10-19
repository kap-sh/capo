"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableFieldOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.custom_label
    import capo_quicksight.types.field_id
    import capo_quicksight.types.visibility


class PivotTableFieldOption(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The field ID of the pivot table field.</p>"""
    custom_label: NotRequired["capo_quicksight.types.custom_label.CustomLabel"]
    """<p>The custom label of the pivot table field.</p>"""
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the pivot table field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableFieldOption) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "custom_label" in value:
        out["CustomLabel"] = value["custom_label"]
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    return out


def deserialize_json(data: dict) -> PivotTableFieldOption:
    out: PivotTableFieldOption = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = ""
    if data.get("CustomLabel") is not None:
        out["custom_label"] = data["CustomLabel"]
    if data.get("Visibility") is not None:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    return out
