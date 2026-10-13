"""Generated from Smithy shape ``com.amazonaws.quicksight#LayerCustomActionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.layer_custom_action

LayerCustomActionList: TypeAlias = list[
    "capo_quicksight.types.layer_custom_action.LayerCustomAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: LayerCustomActionList) -> list:
    import capo_quicksight.types.layer_custom_action

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.layer_custom_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> LayerCustomActionList:
    import capo_quicksight.types.layer_custom_action

    out: LayerCustomActionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.layer_custom_action.deserialize_json(item))
    return out


def redact_sensitive(value: LayerCustomActionList) -> list[Any]:
    import capo_quicksight.types.layer_custom_action

    return [
        capo_quicksight.types.layer_custom_action.redact_sensitive(item)
        for item in value
    ]
