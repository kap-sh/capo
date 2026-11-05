"""Generated from Smithy shape ``com.amazonaws.taxsettings#ColombiaResponsabilidadesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_taxsettings.types.colombia_responsabilidad_code

ColombiaResponsabilidadesList: TypeAlias = list[
    "capo_taxsettings.types.colombia_responsabilidad_code.ColombiaResponsabilidadCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColombiaResponsabilidadesList) -> list:
    return list(value)


def deserialize_json(data: list) -> ColombiaResponsabilidadesList:
    return [item for item in data if item is not None]
