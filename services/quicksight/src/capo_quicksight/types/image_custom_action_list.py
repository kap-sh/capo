"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageCustomActionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.image_custom_action

ImageCustomActionList: TypeAlias = list[
    "capo_quicksight.types.image_custom_action.ImageCustomAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageCustomActionList) -> list:
    import capo_quicksight.types.image_custom_action

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.image_custom_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImageCustomActionList:
    import capo_quicksight.types.image_custom_action

    out: ImageCustomActionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.image_custom_action.deserialize_json(item))
    return out


def redact_sensitive(value: ImageCustomActionList) -> list[Any]:
    import capo_quicksight.types.image_custom_action

    return [
        capo_quicksight.types.image_custom_action.redact_sensitive(item)
        for item in value
    ]
