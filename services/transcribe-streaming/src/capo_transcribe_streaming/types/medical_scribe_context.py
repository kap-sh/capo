"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeContext``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.medical_scribe_patient_context


class MedicalScribeContext(TypedDict, closed=True):
    patient_context: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_patient_context.MedicalScribePatientContext"
    ]
    """<p>Contains patient-specific information used to customize the clinical note generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeContext) -> dict:
    out: dict = {}
    if "patient_context" in value:
        import capo_transcribe_streaming.types.medical_scribe_patient_context

        out["PatientContext"] = (
            capo_transcribe_streaming.types.medical_scribe_patient_context.serialize_json(
                value["patient_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribeContext:
    out: MedicalScribeContext = {}  # type: ignore[typeddict-item]
    if data.get("PatientContext") is not None:
        import capo_transcribe_streaming.types.medical_scribe_patient_context

        out["patient_context"] = (
            capo_transcribe_streaming.types.medical_scribe_patient_context.deserialize_json(
                data["PatientContext"]
            )
        )
    return out


def redact_sensitive(value: MedicalScribeContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "patient_context" in value:
        import capo_transcribe_streaming.types.medical_scribe_patient_context

        out["patient_context"] = (
            capo_transcribe_streaming.types.medical_scribe_patient_context.redact_sensitive(
                value["patient_context"]
            )
        )
    return out
