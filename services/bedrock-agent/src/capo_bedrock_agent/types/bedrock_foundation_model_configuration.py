"""Generated from Smithy shape ``com.amazonaws.bedrockagent#BedrockFoundationModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.bedrock_model_arn
    import capo_bedrock_agent.types.parsing_modality
    import capo_bedrock_agent.types.parsing_prompt


class BedrockFoundationModelConfiguration(TypedDict, closed=True):
    model_arn: "capo_bedrock_agent.types.bedrock_model_arn.BedrockModelArn"
    """<p>The ARN of the foundation model to use for parsing.</p>"""
    parsing_prompt: NotRequired["capo_bedrock_agent.types.parsing_prompt.ParsingPrompt"]
    """<p>Instructions for interpreting the contents of a document.</p>"""
    parsing_modality: NotRequired[
        "capo_bedrock_agent.types.parsing_modality.ParsingModality"
    ]
    """<p>Specifies whether to enable parsing of multimodal data, including both text and/or images.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockFoundationModelConfiguration) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    if "parsing_prompt" in value:
        import capo_bedrock_agent.types.parsing_prompt

        out["parsingPrompt"] = capo_bedrock_agent.types.parsing_prompt.serialize_json(
            value["parsing_prompt"]
        )
    if "parsing_modality" in value:
        import capo_bedrock_agent.types.parsing_modality

        out["parsingModality"] = (
            capo_bedrock_agent.types.parsing_modality.serialize_json(
                value["parsing_modality"]
            )
        )
    return out


def deserialize_json(data: dict) -> BedrockFoundationModelConfiguration:
    out: BedrockFoundationModelConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        out["model_arn"] = ""
    if data.get("parsingPrompt") is not None:
        import capo_bedrock_agent.types.parsing_prompt

        out["parsing_prompt"] = (
            capo_bedrock_agent.types.parsing_prompt.deserialize_json(
                data["parsingPrompt"]
            )
        )
    if data.get("parsingModality") is not None:
        import capo_bedrock_agent.types.parsing_modality

        out["parsing_modality"] = (
            capo_bedrock_agent.types.parsing_modality.deserialize_json(
                data["parsingModality"]
            )
        )
    return out
