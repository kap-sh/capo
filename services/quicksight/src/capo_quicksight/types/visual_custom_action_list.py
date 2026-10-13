"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualCustomActionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.visual_custom_action

VisualCustomActionList: TypeAlias = list[
    "capo_quicksight.types.visual_custom_action.VisualCustomAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: VisualCustomActionList) -> list:
    import capo_quicksight.types.visual_custom_action

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.visual_custom_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> VisualCustomActionList:
    import capo_quicksight.types.visual_custom_action

    out: VisualCustomActionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.visual_custom_action.deserialize_json(item))
    return out


def redact_sensitive(value: VisualCustomActionList) -> list[Any]:
    import capo_quicksight.types.visual_custom_action

    return [
        capo_quicksight.types.visual_custom_action.redact_sensitive(item)
        for item in value
    ]
