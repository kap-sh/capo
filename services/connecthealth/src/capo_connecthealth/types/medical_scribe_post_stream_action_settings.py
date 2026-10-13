"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribePostStreamActionSettings``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connecthealth.types.clinical_note_generation_settings
    import capo_connecthealth.types.s3_uri


class MedicalScribePostStreamActionSettings(TypedDict, closed=True):
    output_s3_uri: "capo_connecthealth.types.s3_uri.S3Uri"
    """<p/>"""
    clinical_note_generation_settings: "capo_connecthealth.types.clinical_note_generation_settings.ClinicalNoteGenerationSettings"
    """<p>Settings for clinical note generation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribePostStreamActionSettings) -> dict:
    out: dict = {}
    out["outputS3Uri"] = value["output_s3_uri"]
    import capo_connecthealth.types.clinical_note_generation_settings

    out["clinicalNoteGenerationSettings"] = (
        capo_connecthealth.types.clinical_note_generation_settings.serialize_json(
            value["clinical_note_generation_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> MedicalScribePostStreamActionSettings:
    out: MedicalScribePostStreamActionSettings = {}  # type: ignore[typeddict-item]
    if data.get("outputS3Uri") is not None:
        out["output_s3_uri"] = data["outputS3Uri"]
    else:
        raise DeserializationError(
            "MedicalScribePostStreamActionSettings.output_s3_uri required"
        )
    if data.get("clinicalNoteGenerationSettings") is not None:
        import capo_connecthealth.types.clinical_note_generation_settings

        out["clinical_note_generation_settings"] = (
            capo_connecthealth.types.clinical_note_generation_settings.deserialize_json(
                data["clinicalNoteGenerationSettings"]
            )
        )
    else:
        raise DeserializationError(
            "MedicalScribePostStreamActionSettings.clinical_note_generation_settings required"
        )
    return out


def redact_sensitive(value: MedicalScribePostStreamActionSettings) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "clinical_note_generation_settings" in value:
        import capo_connecthealth.types.clinical_note_generation_settings

        out["clinical_note_generation_settings"] = (
            capo_connecthealth.types.clinical_note_generation_settings.redact_sensitive(
                value["clinical_note_generation_settings"]
            )
        )
    return out
