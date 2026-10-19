"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessGeminiModelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.api_key_arn
    import capo_bedrock_agentcore_control.types.max_tokens
    import capo_bedrock_agentcore_control.types.model_id
    import capo_bedrock_agentcore_control.types.temperature
    import capo_bedrock_agentcore_control.types.top_k
    import capo_bedrock_agentcore_control.types.top_p


class HarnessGeminiModelConfig(TypedDict, closed=True):
    model_id: "capo_bedrock_agentcore_control.types.model_id.ModelId"
    """<p>The Gemini model ID.</p>"""
    api_key_arn: "capo_bedrock_agentcore_control.types.api_key_arn.ApiKeyArn"
    """<p>The ARN of your Gemini API key on AgentCore Identity.</p>"""
    max_tokens: NotRequired["capo_bedrock_agentcore_control.types.max_tokens.MaxTokens"]
    """<p>The maximum number of tokens to allow in the generated response per model call.</p>"""
    temperature: NotRequired[
        "capo_bedrock_agentcore_control.types.temperature.Temperature"
    ]
    """<p>The temperature to set when calling the model.</p>"""
    top_p: NotRequired["capo_bedrock_agentcore_control.types.top_p.TopP"]
    """<p>The topP set when calling the model.</p>"""
    top_k: NotRequired["capo_bedrock_agentcore_control.types.top_k.TopK"]
    """<p>The topK set when calling the model.</p>"""
    additional_params: NotRequired["object"]
    """<p>Provider-specific parameters passed through to the Gemini model provider unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessGeminiModelConfig) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    out["apiKeyArn"] = value["api_key_arn"]
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
    if "top_k" in value:
        out["topK"] = value["top_k"]
    if "additional_params" in value:
        out["additionalParams"] = value["additional_params"]
    return out


def deserialize_json(data: dict) -> HarnessGeminiModelConfig:
    out: HarnessGeminiModelConfig = {}  # type: ignore[typeddict-item]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    if data.get("apiKeyArn") is not None:
        out["api_key_arn"] = data["apiKeyArn"]
    else:
        out["api_key_arn"] = ""
    if data.get("maxTokens") is not None:
        out["max_tokens"] = data["maxTokens"]
    if data.get("temperature") is not None:
        out["temperature"] = float(data["temperature"])
    if data.get("topP") is not None:
        out["top_p"] = float(data["topP"])
    if data.get("topK") is not None:
        out["top_k"] = data["topK"]
    if data.get("additionalParams") is not None:
        out["additional_params"] = data["additionalParams"]
    return out
