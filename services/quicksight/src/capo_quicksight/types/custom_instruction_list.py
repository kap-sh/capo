"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomInstructionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.custom_instruction

CustomInstructionList: TypeAlias = list[
    "capo_quicksight.types.custom_instruction.CustomInstruction"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomInstructionList) -> list:
    import capo_quicksight.types.custom_instruction

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.custom_instruction.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomInstructionList:
    import capo_quicksight.types.custom_instruction

    out: CustomInstructionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.custom_instruction.deserialize_json(item))
    return out


def redact_sensitive(value: CustomInstructionList) -> list[Any]:
    import capo_quicksight.types.custom_instruction

    return [
        capo_quicksight.types.custom_instruction.redact_sensitive(item)
        for item in value
    ]
