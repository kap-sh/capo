"""Generated from Smithy shape ``com.amazonaws.deadline#OpenjdExtensionNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.openjd_extension_name

OpenjdExtensionNameList: TypeAlias = list[
    "capo_deadline.types.openjd_extension_name.OpenjdExtensionName"
]


# --- restJson1 ser/de ---
def serialize_json(value: OpenjdExtensionNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> OpenjdExtensionNameList:
    return [item for item in data if item is not None]
