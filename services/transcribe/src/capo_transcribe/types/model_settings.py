"""Generated from Smithy shape ``com.amazonaws.transcribe#ModelSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.model_name


class ModelSettings(TypedDict, closed=True):
    language_model_name: NotRequired["capo_transcribe.types.model_name.ModelName"]
    """<p>The name of the custom language model you want to use when processing your transcription job. Note that custom language model names are case sensitive.</p> <p>The language of the specified custom language model must match the language code that you specify in your transcription request. If the languages do not match, the custom language model isn't applied. There are no errors or warnings associated with a language mismatch.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelSettings) -> dict:
    out: dict = {}
    if "language_model_name" in value:
        out["LanguageModelName"] = value["language_model_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelSettings:
    out: ModelSettings = {}  # type: ignore[typeddict-item]
    if data.get("LanguageModelName") is not None:
        out["language_model_name"] = data["LanguageModelName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModelSettings) -> dict:
    out: dict = {}
    if "language_model_name" in value:
        out["LanguageModelName"] = value["language_model_name"]
    return out


def deserialize_cbor(data: dict) -> ModelSettings:
    out: ModelSettings = {}  # type: ignore[typeddict-item]
    if data.get("LanguageModelName") is not None:
        out["language_model_name"] = data["LanguageModelName"]
    return out
