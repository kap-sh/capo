"""Generated from Smithy shape ``com.amazonaws.qconnect#BedrockFoundationModelConfigurationForParsing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.bedrock_model_arn_for_parsing
    import capo_qconnect.types.parsing_prompt


class BedrockFoundationModelConfigurationForParsing(TypedDict, closed=True):
    model_arn: (
        "capo_qconnect.types.bedrock_model_arn_for_parsing.BedrockModelArnForParsing"
    )
    """<p>The ARN of the foundation model.</p>"""
    parsing_prompt: NotRequired["capo_qconnect.types.parsing_prompt.ParsingPrompt"]
    """<p>Instructions for interpreting the contents of a document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockFoundationModelConfigurationForParsing) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    if "parsing_prompt" in value:
        import capo_qconnect.types.parsing_prompt

        out["parsingPrompt"] = capo_qconnect.types.parsing_prompt.serialize_json(
            value["parsing_prompt"]
        )
    return out


def deserialize_json(data: dict) -> BedrockFoundationModelConfigurationForParsing:
    out: BedrockFoundationModelConfigurationForParsing = {}  # type: ignore[typeddict-item]
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        out["model_arn"] = ""
    if data.get("parsingPrompt") is not None:
        import capo_qconnect.types.parsing_prompt

        out["parsing_prompt"] = capo_qconnect.types.parsing_prompt.deserialize_json(
            data["parsingPrompt"]
        )
    return out
