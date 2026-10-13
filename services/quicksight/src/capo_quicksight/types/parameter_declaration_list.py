"""Generated from Smithy shape ``com.amazonaws.quicksight#ParameterDeclarationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.parameter_declaration

ParameterDeclarationList: TypeAlias = list[
    "capo_quicksight.types.parameter_declaration.ParameterDeclaration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParameterDeclarationList) -> list:
    import capo_quicksight.types.parameter_declaration

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.parameter_declaration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParameterDeclarationList:
    import capo_quicksight.types.parameter_declaration

    out: ParameterDeclarationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.parameter_declaration.deserialize_json(item))
    return out


def redact_sensitive(value: ParameterDeclarationList) -> list[Any]:
    import capo_quicksight.types.parameter_declaration

    return [
        capo_quicksight.types.parameter_declaration.redact_sensitive(item)
        for item in value
    ]
