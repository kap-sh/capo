"""Generated from Smithy shape ``com.amazonaws.translate#TranslateDocumentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_translate.errors import DeserializationError

if TYPE_CHECKING:
    import capo_translate.types.applied_terminology_list
    import capo_translate.types.language_code_string
    import capo_translate.types.translated_document
    import capo_translate.types.translation_settings


class TranslateDocumentResponse(TypedDict, closed=True):
    translated_document: "capo_translate.types.translated_document.TranslatedDocument"
    """<p>The document containing the translated content. The document format matches the source document format.</p>"""
    source_language_code: "capo_translate.types.language_code_string.LanguageCodeString"
    """<p>The language code of the source document.</p>"""
    target_language_code: "capo_translate.types.language_code_string.LanguageCodeString"
    """<p>The language code of the translated document. </p>"""
    applied_terminologies: NotRequired[
        "capo_translate.types.applied_terminology_list.AppliedTerminologyList"
    ]
    """<p>The names of the custom terminologies applied to the input text by Amazon Translate to produce the translated text document.</p>"""
    applied_settings: NotRequired[
        "capo_translate.types.translation_settings.TranslationSettings"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TranslateDocumentResponse) -> dict:
    out: dict = {}
    import capo_translate.types.translated_document

    out["TranslatedDocument"] = (
        capo_translate.types.translated_document.serialize_aws_json_1_1(
            value["translated_document"]
        )
    )
    out["SourceLanguageCode"] = value["source_language_code"]
    out["TargetLanguageCode"] = value["target_language_code"]
    if "applied_terminologies" in value:
        import capo_translate.types.applied_terminology_list

        out["AppliedTerminologies"] = (
            capo_translate.types.applied_terminology_list.serialize_aws_json_1_1(
                value["applied_terminologies"]
            )
        )
    if "applied_settings" in value:
        import capo_translate.types.translation_settings

        out["AppliedSettings"] = (
            capo_translate.types.translation_settings.serialize_aws_json_1_1(
                value["applied_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TranslateDocumentResponse:
    out: TranslateDocumentResponse = {}  # type: ignore[typeddict-item]
    if data.get("TranslatedDocument") is not None:
        import capo_translate.types.translated_document

        out["translated_document"] = (
            capo_translate.types.translated_document.deserialize_aws_json_1_1(
                data["TranslatedDocument"]
            )
        )
    else:
        raise DeserializationError(
            "TranslateDocumentResponse.translated_document required"
        )
    if data.get("SourceLanguageCode") is not None:
        out["source_language_code"] = data["SourceLanguageCode"]
    else:
        raise DeserializationError(
            "TranslateDocumentResponse.source_language_code required"
        )
    if data.get("TargetLanguageCode") is not None:
        out["target_language_code"] = data["TargetLanguageCode"]
    else:
        raise DeserializationError(
            "TranslateDocumentResponse.target_language_code required"
        )
    if data.get("AppliedTerminologies") is not None:
        import capo_translate.types.applied_terminology_list

        out["applied_terminologies"] = (
            capo_translate.types.applied_terminology_list.deserialize_aws_json_1_1(
                data["AppliedTerminologies"]
            )
        )
    if data.get("AppliedSettings") is not None:
        import capo_translate.types.translation_settings

        out["applied_settings"] = (
            capo_translate.types.translation_settings.deserialize_aws_json_1_1(
                data["AppliedSettings"]
            )
        )
    return out


def redact_sensitive(value: TranslateDocumentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "translated_document" in value:
        import capo_translate.types.translated_document

        out["translated_document"] = (
            capo_translate.types.translated_document.redact_sensitive(
                value["translated_document"]
            )
        )
    return out
