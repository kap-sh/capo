"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribePostStreamActionSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connecthealth.types.clinical_note_generation_settings_response
    import capo_connecthealth.types.medical_code_generation_settings_response
    import capo_connecthealth.types.s3_uri


class MedicalScribePostStreamActionSettingsResponse(TypedDict, closed=True):
    output_s3_uri: "capo_connecthealth.types.s3_uri.S3Uri"
    """<p/>"""
    clinical_note_generation_settings: "capo_connecthealth.types.clinical_note_generation_settings_response.ClinicalNoteGenerationSettingsResponse"
    """<p>Settings for clinical note generation</p>"""
    medical_code_generation_settings: NotRequired[
        "capo_connecthealth.types.medical_code_generation_settings_response.MedicalCodeGenerationSettingsResponse"
    ]
    """<p>Settings for medical code generation. Returned only if you specified medicalCodeGenerationSettings when you started the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribePostStreamActionSettingsResponse) -> dict:
    out: dict = {}
    out["outputS3Uri"] = value["output_s3_uri"]
    import capo_connecthealth.types.clinical_note_generation_settings_response

    out["clinicalNoteGenerationSettings"] = (
        capo_connecthealth.types.clinical_note_generation_settings_response.serialize_json(
            value["clinical_note_generation_settings"]
        )
    )
    if "medical_code_generation_settings" in value:
        import capo_connecthealth.types.medical_code_generation_settings_response

        out["medicalCodeGenerationSettings"] = (
            capo_connecthealth.types.medical_code_generation_settings_response.serialize_json(
                value["medical_code_generation_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribePostStreamActionSettingsResponse:
    out: MedicalScribePostStreamActionSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("outputS3Uri") is not None:
        out["output_s3_uri"] = data["outputS3Uri"]
    else:
        out["output_s3_uri"] = ""
    if data.get("clinicalNoteGenerationSettings") is not None:
        import capo_connecthealth.types.clinical_note_generation_settings_response

        out["clinical_note_generation_settings"] = (
            capo_connecthealth.types.clinical_note_generation_settings_response.deserialize_json(
                data["clinicalNoteGenerationSettings"]
            )
        )
    else:
        raise DeserializationError(
            "MedicalScribePostStreamActionSettingsResponse.clinical_note_generation_settings required"
        )
    if data.get("medicalCodeGenerationSettings") is not None:
        import capo_connecthealth.types.medical_code_generation_settings_response

        out["medical_code_generation_settings"] = (
            capo_connecthealth.types.medical_code_generation_settings_response.deserialize_json(
                data["medicalCodeGenerationSettings"]
            )
        )
    return out
