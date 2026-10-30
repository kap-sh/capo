"""Generated from Smithy shape ``com.amazonaws.continuum#ValidationProofMaterials``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.validation_proof_material

ValidationProofMaterials: TypeAlias = list[
    "capo_continuum.types.validation_proof_material.ValidationProofMaterial"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationProofMaterials) -> list:
    import capo_continuum.types.validation_proof_material

    out: list = []
    for item in value:
        out.append(capo_continuum.types.validation_proof_material.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValidationProofMaterials:
    import capo_continuum.types.validation_proof_material

    out: ValidationProofMaterials = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_continuum.types.validation_proof_material.deserialize_json(item)
        )
    return out
