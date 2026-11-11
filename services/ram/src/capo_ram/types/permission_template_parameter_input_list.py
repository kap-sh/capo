"""Generated from Smithy shape ``com.amazonaws.ram#PermissionTemplateParameterInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.permission_template_parameter_input

PermissionTemplateParameterInputList: TypeAlias = list[
    "capo_ram.types.permission_template_parameter_input.PermissionTemplateParameterInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionTemplateParameterInputList) -> list:
    import capo_ram.types.permission_template_parameter_input

    out: list = []
    for item in value:
        out.append(
            capo_ram.types.permission_template_parameter_input.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PermissionTemplateParameterInputList:
    import capo_ram.types.permission_template_parameter_input

    out: PermissionTemplateParameterInputList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ram.types.permission_template_parameter_input.deserialize_json(item)
        )
    return out
