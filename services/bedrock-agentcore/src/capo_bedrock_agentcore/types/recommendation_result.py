"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecommendationResult``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.system_prompt_recommendation_result
    import capo_bedrock_agentcore.types.tool_description_recommendation_result


class RecommendationResultSystemPromptRecommendationResultMember(
    TypedDict, closed=True
):
    systemPromptRecommendationResult: "capo_bedrock_agentcore.types.system_prompt_recommendation_result.SystemPromptRecommendationResult"


class RecommendationResultToolDescriptionRecommendationResultMember(
    TypedDict, closed=True
):
    toolDescriptionRecommendationResult: "capo_bedrock_agentcore.types.tool_description_recommendation_result.ToolDescriptionRecommendationResult"


RecommendationResult: TypeAlias = (
    RecommendationResultSystemPromptRecommendationResultMember
    | RecommendationResultToolDescriptionRecommendationResultMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationResult) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RecommendationResult: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "systemPromptRecommendationResult" in value:
        import capo_bedrock_agentcore.types.system_prompt_recommendation_result

        return {
            "systemPromptRecommendationResult": capo_bedrock_agentcore.types.system_prompt_recommendation_result.serialize_json(
                value["systemPromptRecommendationResult"]
            )
        }
    elif "toolDescriptionRecommendationResult" in value:
        import capo_bedrock_agentcore.types.tool_description_recommendation_result

        return {
            "toolDescriptionRecommendationResult": capo_bedrock_agentcore.types.tool_description_recommendation_result.serialize_json(
                value["toolDescriptionRecommendationResult"]
            )
        }
    else:
        raise SerializationError("RecommendationResult: no variant present")


def deserialize_json(data: dict) -> RecommendationResult:
    if data.get("systemPromptRecommendationResult") is not None:
        import capo_bedrock_agentcore.types.system_prompt_recommendation_result

        return {
            "systemPromptRecommendationResult": capo_bedrock_agentcore.types.system_prompt_recommendation_result.deserialize_json(
                data["systemPromptRecommendationResult"]
            )
        }
    elif data.get("toolDescriptionRecommendationResult") is not None:
        import capo_bedrock_agentcore.types.tool_description_recommendation_result

        return {
            "toolDescriptionRecommendationResult": capo_bedrock_agentcore.types.tool_description_recommendation_result.deserialize_json(
                data["toolDescriptionRecommendationResult"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RecommendationResult: no recognized variant key")


def redact_sensitive(value: RecommendationResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "systemPromptRecommendationResult" in value:
        import capo_bedrock_agentcore.types.system_prompt_recommendation_result

        out["systemPromptRecommendationResult"] = (
            capo_bedrock_agentcore.types.system_prompt_recommendation_result.redact_sensitive(
                value["systemPromptRecommendationResult"]
            )
        )
    if "toolDescriptionRecommendationResult" in value:
        import capo_bedrock_agentcore.types.tool_description_recommendation_result

        out["toolDescriptionRecommendationResult"] = (
            capo_bedrock_agentcore.types.tool_description_recommendation_result.redact_sensitive(
                value["toolDescriptionRecommendationResult"]
            )
        )
    return out
