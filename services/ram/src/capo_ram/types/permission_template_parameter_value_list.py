"""Generated from Smithy shape ``com.amazonaws.ram#PermissionTemplateParameterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.string

PermissionTemplateParameterValueList: TypeAlias = list["capo_ram.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionTemplateParameterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> PermissionTemplateParameterValueList:
    return [item for item in data if item is not None]
