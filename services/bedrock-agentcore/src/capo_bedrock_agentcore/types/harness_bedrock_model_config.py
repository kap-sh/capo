"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessBedrockModelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_bedrock_api_format
    import capo_bedrock_agentcore.types.max_tokens
    import capo_bedrock_agentcore.types.model_id
    import capo_bedrock_agentcore.types.temperature
    import capo_bedrock_agentcore.types.top_p


class HarnessBedrockModelConfig(TypedDict, closed=True):
    model_id: "capo_bedrock_agentcore.types.model_id.ModelId"
    """<p>The Bedrock model ID.</p>"""
    max_tokens: NotRequired["capo_bedrock_agentcore.types.max_tokens.MaxTokens"]
    """<p>The maximum number of tokens to allow in the generated response per iteration.</p>"""
    temperature: NotRequired["capo_bedrock_agentcore.types.temperature.Temperature"]
    """<p>The temperature to set when calling the model.</p>"""
    top_p: NotRequired["capo_bedrock_agentcore.types.top_p.TopP"]
    """<p>The topP set when calling the model.</p>"""
    api_format: NotRequired[
        "capo_bedrock_agentcore.types.harness_bedrock_api_format.HarnessBedrockApiFormat"
    ]
    """<p>The API format to use when calling the Bedrock provider.</p>"""
    additional_params: NotRequired["object"]
    """<p>Provider-specific parameters passed through to the model provider unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessBedrockModelConfig) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    if "max_tokens" in value:
        out["maxTokens"] = value["max_tokens"]
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
    if "api_format" in value:
        import capo_bedrock_agentcore.types.harness_bedrock_api_format

        out["apiFormat"] = (
            capo_bedrock_agentcore.types.harness_bedrock_api_format.serialize_json(
                value["api_format"]
            )
        )
    if "additional_params" in value:
        out["additionalParams"] = value["additional_params"]
    return out


def deserialize_json(data: dict) -> HarnessBedrockModelConfig:
    out: HarnessBedrockModelConfig = {}  # type: ignore[typeddict-item]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    if data.get("maxTokens") is not None:
        out["max_tokens"] = data["maxTokens"]
    if data.get("temperature") is not None:
        out["temperature"] = float(data["temperature"])
    if data.get("topP") is not None:
        out["top_p"] = float(data["topP"])
    if data.get("apiFormat") is not None:
        import capo_bedrock_agentcore.types.harness_bedrock_api_format

        out["api_format"] = (
            capo_bedrock_agentcore.types.harness_bedrock_api_format.deserialize_json(
                data["apiFormat"]
            )
        )
    if data.get("additionalParams") is not None:
        out["additional_params"] = data["additionalParams"]
    return out
