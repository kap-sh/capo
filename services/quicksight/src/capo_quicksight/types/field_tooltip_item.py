"""Generated from Smithy shape ``com.amazonaws.quicksight#FieldTooltipItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.field_id
    import capo_quicksight.types.string
    import capo_quicksight.types.tooltip_target
    import capo_quicksight.types.visibility


class FieldTooltipItem(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The unique ID of the field that is targeted by the tooltip.</p>"""
    label: NotRequired["capo_quicksight.types.string.String"]
    """<p>The label of the tooltip item.</p>"""
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the tooltip item.</p>"""
    tooltip_target: NotRequired["capo_quicksight.types.tooltip_target.TooltipTarget"]
    """<p>Determines the target of the field tooltip item in a combo chart visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldTooltipItem) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "label" in value:
        out["Label"] = value["label"]
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "tooltip_target" in value:
        import capo_quicksight.types.tooltip_target

        out["TooltipTarget"] = capo_quicksight.types.tooltip_target.serialize_json(
            value["tooltip_target"]
        )
    return out


def deserialize_json(data: dict) -> FieldTooltipItem:
    out: FieldTooltipItem = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = ""
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    if data.get("Visibility") is not None:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if data.get("TooltipTarget") is not None:
        import capo_quicksight.types.tooltip_target

        out["tooltip_target"] = capo_quicksight.types.tooltip_target.deserialize_json(
            data["TooltipTarget"]
        )
    return out
