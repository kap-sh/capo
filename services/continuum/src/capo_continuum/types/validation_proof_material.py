"""Generated from Smithy shape ``com.amazonaws.continuum#ValidationProofMaterial``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.validation_proof_material_text


class ValidationProofMaterial(TypedDict, closed=True):
    content: "capo_continuum.types.validation_proof_material_text.ValidationProofMaterialText"
    """The file's non-blank text, exactly as retained."""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationProofMaterial) -> dict:
    out: dict = {}
    out["content"] = value["content"]
    return out


def deserialize_json(data: dict) -> ValidationProofMaterial:
    out: ValidationProofMaterial = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        out["content"] = data["content"]
    else:
        out["content"] = ""
    return out
