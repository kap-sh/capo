"""Generated from Smithy shape ``com.amazonaws.ram#PermissionTemplateParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.permission_template_parameter

PermissionTemplateParameterList: TypeAlias = list[
    "capo_ram.types.permission_template_parameter.PermissionTemplateParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionTemplateParameterList) -> list:
    import capo_ram.types.permission_template_parameter

    out: list = []
    for item in value:
        out.append(capo_ram.types.permission_template_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> PermissionTemplateParameterList:
    import capo_ram.types.permission_template_parameter

    out: PermissionTemplateParameterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ram.types.permission_template_parameter.deserialize_json(item))
    return out
