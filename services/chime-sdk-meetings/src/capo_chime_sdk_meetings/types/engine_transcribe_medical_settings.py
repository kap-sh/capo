"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#EngineTranscribeMedicalSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.string
    import capo_chime_sdk_meetings.types.transcribe_medical_content_identification_type
    import capo_chime_sdk_meetings.types.transcribe_medical_language_code
    import capo_chime_sdk_meetings.types.transcribe_medical_region
    import capo_chime_sdk_meetings.types.transcribe_medical_specialty
    import capo_chime_sdk_meetings.types.transcribe_medical_type


class EngineTranscribeMedicalSettings(TypedDict, closed=True):
    language_code: "capo_chime_sdk_meetings.types.transcribe_medical_language_code.TranscribeMedicalLanguageCode"
    """<p>The language code specified for the Amazon Transcribe Medical engine.</p>"""
    specialty: "capo_chime_sdk_meetings.types.transcribe_medical_specialty.TranscribeMedicalSpecialty"
    """<p>The specialty specified for the Amazon Transcribe Medical engine.</p>"""
    type: "capo_chime_sdk_meetings.types.transcribe_medical_type.TranscribeMedicalType"
    """<p>The type of transcription.</p>"""
    vocabulary_name: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    """<p>The name of the vocabulary passed to Amazon Transcribe Medical.</p>"""
    region: NotRequired[
        "capo_chime_sdk_meetings.types.transcribe_medical_region.TranscribeMedicalRegion"
    ]
    """<p>The Amazon Web Services Region passed to Amazon Transcribe Medical. If you don't specify a Region, Amazon Chime uses the meeting's Region. </p>"""
    content_identification_type: NotRequired[
        "capo_chime_sdk_meetings.types.transcribe_medical_content_identification_type.TranscribeMedicalContentIdentificationType"
    ]
    """<p>Set this field to <code>PHI</code> to identify personal health information in the transcription output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EngineTranscribeMedicalSettings) -> dict:
    out: dict = {}
    import capo_chime_sdk_meetings.types.transcribe_medical_language_code

    out["LanguageCode"] = (
        capo_chime_sdk_meetings.types.transcribe_medical_language_code.serialize_json(
            value["language_code"]
        )
    )
    import capo_chime_sdk_meetings.types.transcribe_medical_specialty

    out["Specialty"] = (
        capo_chime_sdk_meetings.types.transcribe_medical_specialty.serialize_json(
            value["specialty"]
        )
    )
    import capo_chime_sdk_meetings.types.transcribe_medical_type

    out["Type"] = capo_chime_sdk_meetings.types.transcribe_medical_type.serialize_json(
        value["type"]
    )
    if "vocabulary_name" in value:
        out["VocabularyName"] = value["vocabulary_name"]
    if "region" in value:
        import capo_chime_sdk_meetings.types.transcribe_medical_region

        out["Region"] = (
            capo_chime_sdk_meetings.types.transcribe_medical_region.serialize_json(
                value["region"]
            )
        )
    if "content_identification_type" in value:
        import capo_chime_sdk_meetings.types.transcribe_medical_content_identification_type

        out["ContentIdentificationType"] = (
            capo_chime_sdk_meetings.types.transcribe_medical_content_identification_type.serialize_json(
                value["content_identification_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> EngineTranscribeMedicalSettings:
    out: EngineTranscribeMedicalSettings = {}  # type: ignore[typeddict-item]
    if data.get("LanguageCode") is not None:
        import capo_chime_sdk_meetings.types.transcribe_medical_language_code

        out["language_code"] = (
            capo_chime_sdk_meetings.types.transcribe_medical_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    else:
        import typing

        out["language_code"] = typing.cast(
            "capo_chime_sdk_meetings.types.transcribe_medical_language_code.TranscribeMedicalLanguageCode",
            "",
        )
    if data.get("Specialty") is not None:
        import capo_chime_sdk_meetings.types.transcribe_medical_specialty

        out["specialty"] = (
            capo_chime_sdk_meetings.types.transcribe_medical_specialty.deserialize_json(
                data["Specialty"]
            )
        )
    else:
        import typing

        out["specialty"] = typing.cast(
            "capo_chime_sdk_meetings.types.transcribe_medical_specialty.TranscribeMedicalSpecialty",
            "",
        )
    if data.get("Type") is not None:
        import capo_chime_sdk_meetings.types.transcribe_medical_type

        out["type"] = (
            capo_chime_sdk_meetings.types.transcribe_medical_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_chime_sdk_meetings.types.transcribe_medical_type.TranscribeMedicalType",
            "",
        )
    if data.get("VocabularyName") is not None:
        out["vocabulary_name"] = data["VocabularyName"]
    if data.get("Region") is not None:
        import capo_chime_sdk_meetings.types.transcribe_medical_region

        out["region"] = (
            capo_chime_sdk_meetings.types.transcribe_medical_region.deserialize_json(
                data["Region"]
            )
        )
    if data.get("ContentIdentificationType") is not None:
        import capo_chime_sdk_meetings.types.transcribe_medical_content_identification_type

        out["content_identification_type"] = (
            capo_chime_sdk_meetings.types.transcribe_medical_content_identification_type.deserialize_json(
                data["ContentIdentificationType"]
            )
        )
    return out
