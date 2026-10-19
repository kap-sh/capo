"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessOpenAiModelConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.api_key_arn
    import capo_bedrock_agentcore.types.harness_open_ai_api_base
    import capo_bedrock_agentcore.types.harness_open_ai_api_format
    import capo_bedrock_agentcore.types.max_tokens
    import capo_bedrock_agentcore.types.model_id
    import capo_bedrock_agentcore.types.temperature
    import capo_bedrock_agentcore.types.top_p


class HarnessOpenAiModelConfig(TypedDict, closed=True):
    model_id: "capo_bedrock_agentcore.types.model_id.ModelId"
    """<p>The OpenAI model ID.</p>"""
    api_key_arn: "capo_bedrock_agentcore.types.api_key_arn.ApiKeyArn"
    """<p>The ARN of your OpenAI API key on AgentCore Identity.</p>"""
    api_base: NotRequired[
        "capo_bedrock_agentcore.types.harness_open_ai_api_base.HarnessOpenAiApiBase"
    ]
    """<p>Optional custom endpoint URL for an OpenAI-compatible endpoint.</p>"""
    max_tokens: NotRequired["capo_bedrock_agentcore.types.max_tokens.MaxTokens"]
    """<p>The maximum number of tokens to allow in the generated response per iteration.</p>"""
    temperature: NotRequired["capo_bedrock_agentcore.types.temperature.Temperature"]
    """<p>The temperature to set when calling the model.</p>"""
    top_p: NotRequired["capo_bedrock_agentcore.types.top_p.TopP"]
    """<p>The topP set when calling the model.</p>"""
    api_format: NotRequired[
        "capo_bedrock_agentcore.types.harness_open_ai_api_format.HarnessOpenAiApiFormat"
    ]
    """<p>The API format to use when calling the OpenAI provider.</p>"""
    additional_params: NotRequired["object"]
    """<p>Provider-specific parameters passed through to the model provider unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessOpenAiModelConfig) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
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
    if "api_format" in value:
        import capo_bedrock_agentcore.types.harness_open_ai_api_format

        out["apiFormat"] = (
            capo_bedrock_agentcore.types.harness_open_ai_api_format.serialize_json(
                value["api_format"]
            )
        )
    if "additional_params" in value:
        out["additionalParams"] = value["additional_params"]
    return out


def deserialize_json(data: dict) -> HarnessOpenAiModelConfig:
    out: HarnessOpenAiModelConfig = {}  # type: ignore[typeddict-item]
    if data.get("modelId") is not None:
        out["model_id"] = data["modelId"]
    else:
        out["model_id"] = ""
    if data.get("apiKeyArn") is not None:
        out["api_key_arn"] = data["apiKeyArn"]
    else:
        out["api_key_arn"] = ""
    if data.get("apiBase") is not None:
        out["api_base"] = data["apiBase"]
    if data.get("maxTokens") is not None:
        out["max_tokens"] = data["maxTokens"]
    if data.get("temperature") is not None:
        out["temperature"] = float(data["temperature"])
    if data.get("topP") is not None:
        out["top_p"] = float(data["topP"])
    if data.get("apiFormat") is not None:
        import capo_bedrock_agentcore.types.harness_open_ai_api_format

        out["api_format"] = (
            capo_bedrock_agentcore.types.harness_open_ai_api_format.deserialize_json(
                data["apiFormat"]
            )
        )
    if data.get("additionalParams") is not None:
        out["additional_params"] = data["additionalParams"]
    return out


def redact_sensitive(value: HarnessOpenAiModelConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "api_base" in value:
        out["api_base"] = "*** Sensitive Data Redacted ***"
    return out
