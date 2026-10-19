"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OpenResponsesEvaluatorModelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.model_id
    import capo_bedrock_agentcore_control.types.reasoning_configuration


class OpenResponsesEvaluatorModelConfig(TypedDict, closed=True):
    model_id: "capo_bedrock_agentcore_control.types.model_id.ModelId"
    """<p> The identifier of the model to use for evaluation. </p>"""
    max_output_tokens: NotRequired["int"]
    """<p> The maximum number of tokens to generate in the model response, including visible output and reasoning tokens. </p>"""
    temperature: NotRequired["float"]
    """<p> The temperature value that controls randomness in the model's responses. Lower values produce more deterministic outputs. </p>"""
    top_p: NotRequired["float"]
    """<p> The top-p sampling parameter that controls the diversity of the model's responses by limiting the cumulative probability of token choices. </p>"""
    reasoning: NotRequired[
        "capo_bedrock_agentcore_control.types.reasoning_configuration.ReasoningConfiguration"
    ]
    """<p> The reasoning configuration for reasoning models. Non-reasoning models ignore this configuration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenResponsesEvaluatorModelConfig) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    if "max_output_tokens" in value:
        out["maxOutputTokens"] = value["max_output_tokens"]
    if "temperature" in value:
        out["temperature"] = (
            "NaN"
            if value["temperature"] != value["temperature"]
            else "Infinity"
            if value["temperature"] == float("inf")
            else "-Infinity"
            if value["temperature"] == float("-inf")
            else value["temperature"]
        )
    if "top_p" in value:
        out["topP"] = (
            "NaN"
            if value["top_p"] != value["top_p"]
            else "Infinity"
            if value["top_p"] == float("inf")
            else "-Infinity"
            if value["top_p"] == float("-inf")
            else value["top_p"]
        )
    if "reasoning" in value:
        import capo_bedrock_agentcore_control.types.reasoning_configuration

        out["reasoning"] = (
            capo_bedrock_agentcore_control.types.reasoning_configuration.serialize_json(
                value["reasoning"]
            )
        )
    return out


def deserialize_json(data: dict) -> OpenResponsesEvaluatorModelConfig:
    out: OpenResponsesEvaluatorModelConfig = {}  # type: ignore[typeddict-item]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    if data.get("maxOutputTokens") is not None:
        out["max_output_tokens"] = data["maxOutputTokens"]
    if data.get("temperature") is not None:
        out["temperature"] = float(data["temperature"])
    if data.get("topP") is not None:
        out["top_p"] = float(data["topP"])
    if data.get("reasoning") is not None:
        import capo_bedrock_agentcore_control.types.reasoning_configuration

        out["reasoning"] = (
            capo_bedrock_agentcore_control.types.reasoning_configuration.deserialize_json(
                data["reasoning"]
            )
        )
    return out
