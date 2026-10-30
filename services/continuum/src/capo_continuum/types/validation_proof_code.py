"""Generated from Smithy shape ``com.amazonaws.continuum#ValidationProofCode``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.validation_proof_materials


class ValidationProofCode(TypedDict, closed=True):
    proof_code: (
        "capo_continuum.types.validation_proof_materials.ValidationProofMaterials"
    )
    """Proof program files, main file first, in their retained order."""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationProofCode) -> dict:
    out: dict = {}
    import capo_continuum.types.validation_proof_materials

    out["proofCode"] = capo_continuum.types.validation_proof_materials.serialize_json(
        value["proof_code"]
    )
    return out


def deserialize_json(data: dict) -> ValidationProofCode:
    out: ValidationProofCode = {}  # type: ignore[typeddict-item]
    if data.get("proofCode") is not None:
        import capo_continuum.types.validation_proof_materials

        out["proof_code"] = (
            capo_continuum.types.validation_proof_materials.deserialize_json(
                data["proofCode"]
            )
        )
    else:
        out["proof_code"] = []
    return out
