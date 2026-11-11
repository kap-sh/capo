"""Generated from Smithy shape ``com.amazonaws.ram#PermissionArnAndTemplateParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.permission_arn_and_template_parameters

PermissionArnAndTemplateParametersList: TypeAlias = list[
    "capo_ram.types.permission_arn_and_template_parameters.PermissionArnAndTemplateParameters"
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionArnAndTemplateParametersList) -> list:
    import capo_ram.types.permission_arn_and_template_parameters

    out: list = []
    for item in value:
        out.append(
            capo_ram.types.permission_arn_and_template_parameters.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PermissionArnAndTemplateParametersList:
    import capo_ram.types.permission_arn_and_template_parameters

    out: PermissionArnAndTemplateParametersList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ram.types.permission_arn_and_template_parameters.deserialize_json(item)
        )
    return out
