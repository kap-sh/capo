"""Generated from Smithy shape ``com.amazonaws.quicksight#LayerCustomActionOperationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.layer_custom_action_operation

LayerCustomActionOperationList: TypeAlias = list[
    "capo_quicksight.types.layer_custom_action_operation.LayerCustomActionOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: LayerCustomActionOperationList) -> list:
    import capo_quicksight.types.layer_custom_action_operation

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.layer_custom_action_operation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LayerCustomActionOperationList:
    import capo_quicksight.types.layer_custom_action_operation

    out: LayerCustomActionOperationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.layer_custom_action_operation.deserialize_json(item)
        )
    return out


def redact_sensitive(value: LayerCustomActionOperationList) -> list[Any]:
    import capo_quicksight.types.layer_custom_action_operation

    return [
        capo_quicksight.types.layer_custom_action_operation.redact_sensitive(item)
        for item in value
    ]
