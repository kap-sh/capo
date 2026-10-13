"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeContext``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.medical_scribe_patient_context


class MedicalScribeContext(TypedDict, closed=True):
    patient_context: NotRequired[
        "capo_transcribe.types.medical_scribe_patient_context.MedicalScribePatientContext"
    ]
    """<p>Contains patient-specific information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalScribeContext) -> dict:
    out: dict = {}
    if "patient_context" in value:
        import capo_transcribe.types.medical_scribe_patient_context

        out["PatientContext"] = (
            capo_transcribe.types.medical_scribe_patient_context.serialize_aws_json_1_1(
                value["patient_context"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MedicalScribeContext:
    out: MedicalScribeContext = {}  # type: ignore[typeddict-item]
    if data.get("PatientContext") is not None:
        import capo_transcribe.types.medical_scribe_patient_context

        out["patient_context"] = (
            capo_transcribe.types.medical_scribe_patient_context.deserialize_aws_json_1_1(
                data["PatientContext"]
            )
        )
    return out


def redact_sensitive(value: MedicalScribeContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "patient_context" in value:
        import capo_transcribe.types.medical_scribe_patient_context

        out["patient_context"] = (
            capo_transcribe.types.medical_scribe_patient_context.redact_sensitive(
                value["patient_context"]
            )
        )
    return out
