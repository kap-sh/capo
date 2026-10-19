"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessModelConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_bedrock_model_config
    import capo_bedrock_agentcore.types.harness_gemini_model_config
    import capo_bedrock_agentcore.types.harness_lite_llm_model_config
    import capo_bedrock_agentcore.types.harness_open_ai_model_config


class _HarnessModelConfiguration_bedrockModelConfig(TypedDict, closed=True):
    bedrockModelConfig: "capo_bedrock_agentcore.types.harness_bedrock_model_config.HarnessBedrockModelConfig"


class _HarnessModelConfiguration_openAiModelConfig(TypedDict, closed=True):
    openAiModelConfig: "capo_bedrock_agentcore.types.harness_open_ai_model_config.HarnessOpenAiModelConfig"


class _HarnessModelConfiguration_geminiModelConfig(TypedDict, closed=True):
    geminiModelConfig: "capo_bedrock_agentcore.types.harness_gemini_model_config.HarnessGeminiModelConfig"


class _HarnessModelConfiguration_liteLlmModelConfig(TypedDict, closed=True):
    liteLlmModelConfig: "capo_bedrock_agentcore.types.harness_lite_llm_model_config.HarnessLiteLlmModelConfig"


HarnessModelConfiguration: TypeAlias = (
    _HarnessModelConfiguration_bedrockModelConfig
    | _HarnessModelConfiguration_openAiModelConfig
    | _HarnessModelConfiguration_geminiModelConfig
    | _HarnessModelConfiguration_liteLlmModelConfig
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessModelConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"HarnessModelConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "bedrockModelConfig" in value:
        import capo_bedrock_agentcore.types.harness_bedrock_model_config

        return {
            "bedrockModelConfig": capo_bedrock_agentcore.types.harness_bedrock_model_config.serialize_json(
                value["bedrockModelConfig"]
            )
        }
    elif "openAiModelConfig" in value:
        import capo_bedrock_agentcore.types.harness_open_ai_model_config

        return {
            "openAiModelConfig": capo_bedrock_agentcore.types.harness_open_ai_model_config.serialize_json(
                value["openAiModelConfig"]
            )
        }
    elif "geminiModelConfig" in value:
        import capo_bedrock_agentcore.types.harness_gemini_model_config

        return {
            "geminiModelConfig": capo_bedrock_agentcore.types.harness_gemini_model_config.serialize_json(
                value["geminiModelConfig"]
            )
        }
    elif "liteLlmModelConfig" in value:
        import capo_bedrock_agentcore.types.harness_lite_llm_model_config

        return {
            "liteLlmModelConfig": capo_bedrock_agentcore.types.harness_lite_llm_model_config.serialize_json(
                value["liteLlmModelConfig"]
            )
        }
    else:
        raise SerializationError("HarnessModelConfiguration: no variant present")


def deserialize_json(data: dict) -> HarnessModelConfiguration:
    if data.get("bedrockModelConfig") is not None:
        import capo_bedrock_agentcore.types.harness_bedrock_model_config

        return {
            "bedrockModelConfig": capo_bedrock_agentcore.types.harness_bedrock_model_config.deserialize_json(
                data["bedrockModelConfig"]
            )
        }
    elif data.get("openAiModelConfig") is not None:
        import capo_bedrock_agentcore.types.harness_open_ai_model_config

        return {
            "openAiModelConfig": capo_bedrock_agentcore.types.harness_open_ai_model_config.deserialize_json(
                data["openAiModelConfig"]
            )
        }
    elif data.get("geminiModelConfig") is not None:
        import capo_bedrock_agentcore.types.harness_gemini_model_config

        return {
            "geminiModelConfig": capo_bedrock_agentcore.types.harness_gemini_model_config.deserialize_json(
                data["geminiModelConfig"]
            )
        }
    elif data.get("liteLlmModelConfig") is not None:
        import capo_bedrock_agentcore.types.harness_lite_llm_model_config

        return {
            "liteLlmModelConfig": capo_bedrock_agentcore.types.harness_lite_llm_model_config.deserialize_json(
                data["liteLlmModelConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "HarnessModelConfiguration: no recognized variant key"
        )


def redact_sensitive(
    value: HarnessModelConfiguration,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "openAiModelConfig" in value:
        import capo_bedrock_agentcore.types.harness_open_ai_model_config

        out["openAiModelConfig"] = (
            capo_bedrock_agentcore.types.harness_open_ai_model_config.redact_sensitive(
                value["openAiModelConfig"]
            )
        )
    if "liteLlmModelConfig" in value:
        import capo_bedrock_agentcore.types.harness_lite_llm_model_config

        out["liteLlmModelConfig"] = (
            capo_bedrock_agentcore.types.harness_lite_llm_model_config.redact_sensitive(
                value["liteLlmModelConfig"]
            )
        )
    return out
