"""Generated from Smithy shape ``com.amazonaws.translate#TranslationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.brevity
    import capo_translate.types.formality
    import capo_translate.types.profanity


class TranslationSettings(TypedDict, closed=True):
    formality: NotRequired["capo_translate.types.formality.Formality"]
    """<p>You can specify the desired level of formality for translations to supported target languages. The formality setting controls the level of formal language usage (also known as <a href="https://en.wikipedia.org/wiki/Register_(sociolinguistics)">register</a>) in the translation output. You can set the value to informal or formal. If you don't specify a value for formality, or if the target language doesn't support formality, the translation will ignore the formality setting.</p> <p> If you specify multiple target languages for the job, translate ignores the formality setting for any unsupported target language.</p> <p>For a list of target languages that support formality, see <a href="https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-formality.html#customizing-translations-formality-languages">Supported languages</a> in the Amazon Translate Developer Guide.</p>"""
    profanity: NotRequired["capo_translate.types.profanity.Profanity"]
    """<p>You can enable the profanity setting if you want to mask profane words and phrases in your translation output.</p> <p>To mask profane words and phrases, Amazon Translate replaces them with the grawlix string “?$#@$“. This 5-character sequence is used for each profane word or phrase, regardless of the length or number of words.</p> <p>Amazon Translate doesn't detect profanity in all of its supported languages. For languages that don't support profanity detection, see <a href="https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-profanity.html#customizing-translations-profanity-languages">Unsupported languages</a> in the Amazon Translate Developer Guide.</p> <p>If you specify multiple target languages for the job, all the target languages must support profanity masking. If any of the target languages don't support profanity masking, the translation job won't mask profanity for any target language.</p>"""
    brevity: NotRequired["capo_translate.types.brevity.Brevity"]
    """<p>When you turn on brevity, Amazon Translate reduces the length of the translation output for most translations (when compared with the same translation with brevity turned off). By default, brevity is turned off.</p> <p>If you turn on brevity for a translation request with an unsupported language pair, the translation proceeds with the brevity setting turned off.</p> <p>For the language pairs that brevity supports, see <a href="https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-brevity">Using brevity</a> in the Amazon Translate Developer Guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TranslationSettings) -> dict:
    out: dict = {}
    if "formality" in value:
        import capo_translate.types.formality

        out["Formality"] = capo_translate.types.formality.serialize_aws_json_1_1(
            value["formality"]
        )
    if "profanity" in value:
        import capo_translate.types.profanity

        out["Profanity"] = capo_translate.types.profanity.serialize_aws_json_1_1(
            value["profanity"]
        )
    if "brevity" in value:
        import capo_translate.types.brevity

        out["Brevity"] = capo_translate.types.brevity.serialize_aws_json_1_1(
            value["brevity"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TranslationSettings:
    out: TranslationSettings = {}  # type: ignore[typeddict-item]
    if data.get("Formality") is not None:
        import capo_translate.types.formality

        out["formality"] = capo_translate.types.formality.deserialize_aws_json_1_1(
            data["Formality"]
        )
    if data.get("Profanity") is not None:
        import capo_translate.types.profanity

        out["profanity"] = capo_translate.types.profanity.deserialize_aws_json_1_1(
            data["Profanity"]
        )
    if data.get("Brevity") is not None:
        import capo_translate.types.brevity

        out["brevity"] = capo_translate.types.brevity.deserialize_aws_json_1_1(
            data["Brevity"]
        )
    return out
