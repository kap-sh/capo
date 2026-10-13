"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageCustomActionOperationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.image_custom_action_operation

ImageCustomActionOperationList: TypeAlias = list[
    "capo_quicksight.types.image_custom_action_operation.ImageCustomActionOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageCustomActionOperationList) -> list:
    import capo_quicksight.types.image_custom_action_operation

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.image_custom_action_operation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ImageCustomActionOperationList:
    import capo_quicksight.types.image_custom_action_operation

    out: ImageCustomActionOperationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.image_custom_action_operation.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ImageCustomActionOperationList) -> list[Any]:
    import capo_quicksight.types.image_custom_action_operation

    return [
        capo_quicksight.types.image_custom_action_operation.redact_sensitive(item)
        for item in value
    ]
