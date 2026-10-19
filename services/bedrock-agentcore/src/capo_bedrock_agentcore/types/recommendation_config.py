"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecommendationConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.system_prompt_recommendation_config
    import capo_bedrock_agentcore.types.tool_description_recommendation_config


class _RecommendationConfig_systemPromptRecommendationConfig(TypedDict, closed=True):
    systemPromptRecommendationConfig: "capo_bedrock_agentcore.types.system_prompt_recommendation_config.SystemPromptRecommendationConfig"


class _RecommendationConfig_toolDescriptionRecommendationConfig(TypedDict, closed=True):
    toolDescriptionRecommendationConfig: "capo_bedrock_agentcore.types.tool_description_recommendation_config.ToolDescriptionRecommendationConfig"


RecommendationConfig: TypeAlias = (
    _RecommendationConfig_systemPromptRecommendationConfig
    | _RecommendationConfig_toolDescriptionRecommendationConfig
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"RecommendationConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "systemPromptRecommendationConfig" in value:
        import capo_bedrock_agentcore.types.system_prompt_recommendation_config

        return {
            "systemPromptRecommendationConfig": capo_bedrock_agentcore.types.system_prompt_recommendation_config.serialize_json(
                value["systemPromptRecommendationConfig"]
            )
        }
    elif "toolDescriptionRecommendationConfig" in value:
        import capo_bedrock_agentcore.types.tool_description_recommendation_config

        return {
            "toolDescriptionRecommendationConfig": capo_bedrock_agentcore.types.tool_description_recommendation_config.serialize_json(
                value["toolDescriptionRecommendationConfig"]
            )
        }
    else:
        raise SerializationError("RecommendationConfig: no variant present")


def deserialize_json(data: dict) -> RecommendationConfig:
    if data.get("systemPromptRecommendationConfig") is not None:
        import capo_bedrock_agentcore.types.system_prompt_recommendation_config

        return {
            "systemPromptRecommendationConfig": capo_bedrock_agentcore.types.system_prompt_recommendation_config.deserialize_json(
                data["systemPromptRecommendationConfig"]
            )
        }
    elif data.get("toolDescriptionRecommendationConfig") is not None:
        import capo_bedrock_agentcore.types.tool_description_recommendation_config

        return {
            "toolDescriptionRecommendationConfig": capo_bedrock_agentcore.types.tool_description_recommendation_config.deserialize_json(
                data["toolDescriptionRecommendationConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("RecommendationConfig: no recognized variant key")


def redact_sensitive(
    value: RecommendationConfig,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "systemPromptRecommendationConfig" in value:
        import capo_bedrock_agentcore.types.system_prompt_recommendation_config

        out["systemPromptRecommendationConfig"] = (
            capo_bedrock_agentcore.types.system_prompt_recommendation_config.redact_sensitive(
                value["systemPromptRecommendationConfig"]
            )
        )
    if "toolDescriptionRecommendationConfig" in value:
        import capo_bedrock_agentcore.types.tool_description_recommendation_config

        out["toolDescriptionRecommendationConfig"] = (
            capo_bedrock_agentcore.types.tool_description_recommendation_config.redact_sensitive(
                value["toolDescriptionRecommendationConfig"]
            )
        )
    return out
