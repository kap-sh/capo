"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomColorsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.custom_color

CustomColorsList: TypeAlias = list["capo_quicksight.types.custom_color.CustomColor"]


# --- restJson1 ser/de ---
def serialize_json(value: CustomColorsList) -> list:
    import capo_quicksight.types.custom_color

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.custom_color.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomColorsList:
    import capo_quicksight.types.custom_color

    out: CustomColorsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.custom_color.deserialize_json(item))
    return out


def redact_sensitive(value: CustomColorsList) -> list[Any]:
    import capo_quicksight.types.custom_color

    return [capo_quicksight.types.custom_color.redact_sensitive(item) for item in value]
