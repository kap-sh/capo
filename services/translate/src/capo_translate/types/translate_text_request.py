"""Generated from Smithy shape ``com.amazonaws.translate#TranslateTextRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_translate.errors import DeserializationError

if TYPE_CHECKING:
    import capo_translate.types.bounded_length_string
    import capo_translate.types.language_code_string
    import capo_translate.types.resource_name_list
    import capo_translate.types.translation_settings


class TranslateTextRequest(TypedDict, closed=True):
    text: "capo_translate.types.bounded_length_string.BoundedLengthString"
    """<p>The text to translate. The text string can be a maximum of 10,000 bytes long. Depending on your character set, this may be fewer than 10,000 characters.</p>"""
    terminology_names: NotRequired[
        "capo_translate.types.resource_name_list.ResourceNameList"
    ]
    """<p>The name of a terminology list file to add to the translation job. This file provides source terms and the desired translation for each term. A terminology list can contain a maximum of 256 terms. You can use one custom terminology resource in your translation request.</p> <p>Use the <a>ListTerminologies</a> operation to get the available terminology lists.</p> <p>For more information about custom terminology lists, see <a href="https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html">Custom terminology</a>.</p>"""
    source_language_code: "capo_translate.types.language_code_string.LanguageCodeString"
    """<p>The language code for the language of the source text. For a list of language codes, see <a href="https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html">Supported languages</a>.</p> <p>To have Amazon Translate determine the source language of your text, you can specify <code>auto</code> in the <code>SourceLanguageCode</code> field. If you specify <code>auto</code>, Amazon Translate will call <a href="https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-general.html">Amazon Comprehend</a> to determine the source language.</p> <note> <p>If you specify <code>auto</code>, you must send the <code>TranslateText</code> request in a region that supports Amazon Comprehend. Otherwise, the request returns an error indicating that autodetect is not supported. </p> </note>"""
    target_language_code: "capo_translate.types.language_code_string.LanguageCodeString"
    """<p>The language code requested for the language of the target text. For a list of language codes, see <a href="https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html">Supported languages</a>.</p>"""
    settings: NotRequired[
        "capo_translate.types.translation_settings.TranslationSettings"
    ]
    """<p>Settings to configure your translation output. You can configure the following options:</p> <ul> <li> <p>Brevity: reduces the length of the translated output for most translations.</p> </li> <li> <p>Formality: sets the formality level of the output text.</p> </li> <li> <p>Profanity: masks profane words and phrases in your translation output.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TranslateTextRequest) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    if "terminology_names" in value:
        import capo_translate.types.resource_name_list

        out["TerminologyNames"] = (
            capo_translate.types.resource_name_list.serialize_aws_json_1_1(
                value["terminology_names"]
            )
        )
    out["SourceLanguageCode"] = value["source_language_code"]
    out["TargetLanguageCode"] = value["target_language_code"]
    if "settings" in value:
        import capo_translate.types.translation_settings

        out["Settings"] = (
            capo_translate.types.translation_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TranslateTextRequest:
    out: TranslateTextRequest = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("TranslateTextRequest.text required")
    if data.get("TerminologyNames") is not None:
        import capo_translate.types.resource_name_list

        out["terminology_names"] = (
            capo_translate.types.resource_name_list.deserialize_aws_json_1_1(
                data["TerminologyNames"]
            )
        )
    if data.get("SourceLanguageCode") is not None:
        out["source_language_code"] = data["SourceLanguageCode"]
    else:
        raise DeserializationError("TranslateTextRequest.source_language_code required")
    if data.get("TargetLanguageCode") is not None:
        out["target_language_code"] = data["TargetLanguageCode"]
    else:
        raise DeserializationError("TranslateTextRequest.target_language_code required")
    if data.get("Settings") is not None:
        import capo_translate.types.translation_settings

        out["settings"] = (
            capo_translate.types.translation_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    return out
