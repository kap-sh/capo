"""Generated from Smithy shape ``com.amazonaws.ram#PermissionTemplateParameterType``."""

from typing import Literal, TypeAlias, cast

PermissionTemplateParameterType: TypeAlias = Literal[
    "STRING",
    "STRING_LIST",
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionTemplateParameterType) -> str:
    return value


def deserialize_json(data: str) -> PermissionTemplateParameterType:
    return cast(PermissionTemplateParameterType, data)
