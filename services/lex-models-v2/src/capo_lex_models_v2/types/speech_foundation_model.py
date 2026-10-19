"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SpeechFoundationModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bedrock_model_arn
    import capo_lex_models_v2.types.voice_id


class SpeechFoundationModel(TypedDict, closed=True):
    model_arn: "capo_lex_models_v2.types.bedrock_model_arn.BedrockModelArn"
    """<p>The Amazon Resource Name (ARN) of the foundation model used for speech processing.</p>"""
    voice_id: NotRequired["capo_lex_models_v2.types.voice_id.VoiceId"]
    """<p>The identifier of the voice to use for speech synthesis with the foundation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpeechFoundationModel) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    if "voice_id" in value:
        out["voiceId"] = value["voice_id"]
    return out


def deserialize_json(data: dict) -> SpeechFoundationModel:
    out: SpeechFoundationModel = {}  # type: ignore[typeddict-item]
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        out["model_arn"] = ""
    if data.get("voiceId") is not None:
        out["voice_id"] = data["voiceId"]
    return out
