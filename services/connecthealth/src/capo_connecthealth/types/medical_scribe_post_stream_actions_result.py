"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribePostStreamActionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.clinical_note_generation_result
    import capo_connecthealth.types.medical_code_generation_result


class MedicalScribePostStreamActionsResult(TypedDict, closed=True):
    clinical_note_generation_result: NotRequired[
        "capo_connecthealth.types.clinical_note_generation_result.ClinicalNoteGenerationResult"
    ]
    """<p>Results of clinical note generation</p>"""
    medical_code_generation_result: NotRequired[
        "capo_connecthealth.types.medical_code_generation_result.MedicalCodeGenerationResult"
    ]
    """<p>Results of medical code generation. Returned if medical code generation runs for the session. Not returned if you set enabled to false in medicalCodeGenerationSettings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribePostStreamActionsResult) -> dict:
    out: dict = {}
    if "clinical_note_generation_result" in value:
        import capo_connecthealth.types.clinical_note_generation_result

        out["clinicalNoteGenerationResult"] = (
            capo_connecthealth.types.clinical_note_generation_result.serialize_json(
                value["clinical_note_generation_result"]
            )
        )
    if "medical_code_generation_result" in value:
        import capo_connecthealth.types.medical_code_generation_result

        out["medicalCodeGenerationResult"] = (
            capo_connecthealth.types.medical_code_generation_result.serialize_json(
                value["medical_code_generation_result"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribePostStreamActionsResult:
    out: MedicalScribePostStreamActionsResult = {}  # type: ignore[typeddict-item]
    if data.get("clinicalNoteGenerationResult") is not None:
        import capo_connecthealth.types.clinical_note_generation_result

        out["clinical_note_generation_result"] = (
            capo_connecthealth.types.clinical_note_generation_result.deserialize_json(
                data["clinicalNoteGenerationResult"]
            )
        )
    if data.get("medicalCodeGenerationResult") is not None:
        import capo_connecthealth.types.medical_code_generation_result

        out["medical_code_generation_result"] = (
            capo_connecthealth.types.medical_code_generation_result.deserialize_json(
                data["medicalCodeGenerationResult"]
            )
        )
    return out
