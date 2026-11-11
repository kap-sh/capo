"""Generated from Smithy shape ``com.amazonaws.ram#PermissionTemplateParameterDeclarationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.permission_template_parameter_declaration

PermissionTemplateParameterDeclarationList: TypeAlias = list[
    "capo_ram.types.permission_template_parameter_declaration.PermissionTemplateParameterDeclaration"
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionTemplateParameterDeclarationList) -> list:
    import capo_ram.types.permission_template_parameter_declaration

    out: list = []
    for item in value:
        out.append(
            capo_ram.types.permission_template_parameter_declaration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PermissionTemplateParameterDeclarationList:
    import capo_ram.types.permission_template_parameter_declaration

    out: PermissionTemplateParameterDeclarationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ram.types.permission_template_parameter_declaration.deserialize_json(
                item
            )
        )
    return out
