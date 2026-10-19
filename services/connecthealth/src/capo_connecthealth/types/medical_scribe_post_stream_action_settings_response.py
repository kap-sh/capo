"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribePostStreamActionSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connecthealth.types.clinical_note_generation_settings_response
    import capo_connecthealth.types.s3_uri


class MedicalScribePostStreamActionSettingsResponse(TypedDict, closed=True):
    output_s3_uri: "capo_connecthealth.types.s3_uri.S3Uri"
    """<p/>"""
    clinical_note_generation_settings: "capo_connecthealth.types.clinical_note_generation_settings_response.ClinicalNoteGenerationSettingsResponse"
    """<p>Settings for clinical note generation</p>"""


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
    return out
