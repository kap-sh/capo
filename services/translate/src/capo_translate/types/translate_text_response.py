"""Generated from Smithy shape ``com.amazonaws.translate#TranslateTextResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.applied_terminology_list
    import capo_translate.types.language_code_string
    import capo_translate.types.translated_text_string
    import capo_translate.types.translation_settings


class TranslateTextResponse(TypedDict, closed=True):
    translated_text: "capo_translate.types.translated_text_string.TranslatedTextString"
    """<p>The translated text.</p>"""
    source_language_code: "capo_translate.types.language_code_string.LanguageCodeString"
    """<p>The language code for the language of the source text.</p>"""
    target_language_code: "capo_translate.types.language_code_string.LanguageCodeString"
    """<p>The language code for the language of the target text. </p>"""
    applied_terminologies: NotRequired[
        "capo_translate.types.applied_terminology_list.AppliedTerminologyList"
    ]
    """<p>The names of the custom terminologies applied to the input text by Amazon Translate for the translated text response.</p>"""
    applied_settings: NotRequired[
        "capo_translate.types.translation_settings.TranslationSettings"
    ]
    """<p>Optional settings that modify the translation output.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TranslateTextResponse) -> dict:
    out: dict = {}
    out["TranslatedText"] = value["translated_text"]
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


def deserialize_aws_json_1_1(data: dict) -> TranslateTextResponse:
    out: TranslateTextResponse = {}  # type: ignore[typeddict-item]
    if data.get("TranslatedText") is not None:
        out["translated_text"] = data["TranslatedText"]
    else:
        out["translated_text"] = ""
    if data.get("SourceLanguageCode") is not None:
        out["source_language_code"] = data["SourceLanguageCode"]
    else:
        out["source_language_code"] = ""
    if data.get("TargetLanguageCode") is not None:
        out["target_language_code"] = data["TargetLanguageCode"]
    else:
        out["target_language_code"] = ""
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
