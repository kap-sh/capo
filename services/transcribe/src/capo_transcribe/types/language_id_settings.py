"""Generated from Smithy shape ``com.amazonaws.transcribe#LanguageIdSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.model_name
    import capo_transcribe.types.vocabulary_filter_name
    import capo_transcribe.types.vocabulary_name


class LanguageIdSettings(TypedDict, closed=True):
    vocabulary_name: NotRequired["capo_transcribe.types.vocabulary_name.VocabularyName"]
    """<p>The name of the custom vocabulary you want to use when processing your transcription job. Custom vocabulary names are case sensitive.</p> <p>The language of the specified custom vocabulary must match the language code that you specify in your transcription request. If the languages do not match, the custom vocabulary isn't applied. There are no errors or warnings associated with a language mismatch.</p>"""
    vocabulary_filter_name: NotRequired[
        "capo_transcribe.types.vocabulary_filter_name.VocabularyFilterName"
    ]
    """<p>The name of the custom vocabulary filter you want to use when processing your transcription job. Custom vocabulary filter names are case sensitive.</p> <p>The language of the specified custom vocabulary filter must match the language code that you specify in your transcription request. If the languages do not match, the custom vocabulary filter isn't applied. There are no errors or warnings associated with a language mismatch.</p> <p>Note that if you include <code>VocabularyFilterName</code> in your request, you must also include <code>VocabularyFilterMethod</code>.</p>"""
    language_model_name: NotRequired["capo_transcribe.types.model_name.ModelName"]
    """<p>The name of the custom language model you want to use when processing your transcription job. Note that custom language model names are case sensitive.</p> <p>The language of the specified custom language model must match the language code that you specify in your transcription request. If the languages do not match, the custom language model isn't applied. There are no errors or warnings associated with a language mismatch.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LanguageIdSettings) -> dict:
    out: dict = {}
    if "vocabulary_name" in value:
        out["VocabularyName"] = value["vocabulary_name"]
    if "vocabulary_filter_name" in value:
        out["VocabularyFilterName"] = value["vocabulary_filter_name"]
    if "language_model_name" in value:
        out["LanguageModelName"] = value["language_model_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LanguageIdSettings:
    out: LanguageIdSettings = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyName") is not None:
        out["vocabulary_name"] = data["VocabularyName"]
    if data.get("VocabularyFilterName") is not None:
        out["vocabulary_filter_name"] = data["VocabularyFilterName"]
    if data.get("LanguageModelName") is not None:
        out["language_model_name"] = data["LanguageModelName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LanguageIdSettings) -> dict:
    out: dict = {}
    if "vocabulary_name" in value:
        out["VocabularyName"] = value["vocabulary_name"]
    if "vocabulary_filter_name" in value:
        out["VocabularyFilterName"] = value["vocabulary_filter_name"]
    if "language_model_name" in value:
        out["LanguageModelName"] = value["language_model_name"]
    return out


def deserialize_cbor(data: dict) -> LanguageIdSettings:
    out: LanguageIdSettings = {}  # type: ignore[typeddict-item]
    if data.get("VocabularyName") is not None:
        out["vocabulary_name"] = data["VocabularyName"]
    if data.get("VocabularyFilterName") is not None:
        out["vocabulary_filter_name"] = data["VocabularyFilterName"]
    if data.get("LanguageModelName") is not None:
        out["language_model_name"] = data["LanguageModelName"]
    return out
