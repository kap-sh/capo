"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessLiteLlmModelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.api_key_arn
    import capo_bedrock_agentcore_control.types.harness_lite_llm_api_base
    import capo_bedrock_agentcore_control.types.max_tokens
    import capo_bedrock_agentcore_control.types.model_id
    import capo_bedrock_agentcore_control.types.temperature
    import capo_bedrock_agentcore_control.types.top_p


class HarnessLiteLlmModelConfig(TypedDict, closed=True):
    model_id: "capo_bedrock_agentcore_control.types.model_id.ModelId"
    """<p>The LiteLLM model identifier (e.g., "anthropic/claude-3-sonnet").</p>"""
    api_key_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.api_key_arn.ApiKeyArn"
    ]
    """<p>The ARN of the API key in AgentCore Identity for authenticating with the model provider.</p>"""
    api_base: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_lite_llm_api_base.HarnessLiteLlmApiBase"
    ]
    """<p>The base URL for the model provider's API endpoint.</p>"""
    max_tokens: NotRequired["capo_bedrock_agentcore_control.types.max_tokens.MaxTokens"]
    """<p>The maximum number of tokens to allow in the generated response per iteration.</p>"""
    temperature: NotRequired[
        "capo_bedrock_agentcore_control.types.temperature.Temperature"
    ]
    """<p>The temperature to set when calling the model.</p>"""
    top_p: NotRequired["capo_bedrock_agentcore_control.types.top_p.TopP"]
    """<p>The topP set when calling the model.</p>"""
    additional_params: NotRequired["object"]
    """<p>Provider-specific parameters passed through to the model provider unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessLiteLlmModelConfig) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    if "api_key_arn" in value:
        out["apiKeyArn"] = value["api_key_arn"]
    if "api_base" in value:
        out["apiBase"] = value["api_base"]
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
    if "additional_params" in value:
        out["additionalParams"] = value["additional_params"]
    return out


def deserialize_json(data: dict) -> HarnessLiteLlmModelConfig:
    out: HarnessLiteLlmModelConfig = {}  # type: ignore[typeddict-item]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("HarnessLiteLlmModelConfig.model_id required")
    if data.get("apiKeyArn") is not None:
        out["api_key_arn"] = data["apiKeyArn"]
    if data.get("apiBase") is not None:
        out["api_base"] = data["apiBase"]
    if data.get("maxTokens") is not None:
        out["max_tokens"] = data["maxTokens"]
    if data.get("temperature") is not None:
        out["temperature"] = float(data["temperature"])
    if data.get("topP") is not None:
        out["top_p"] = float(data["topP"])
    if data.get("additionalParams") is not None:
        out["additional_params"] = data["additionalParams"]
    return out
