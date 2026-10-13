"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolDescriptionRecommendationResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.recommendation_error_code
    import capo_bedrock_agentcore.types.recommendation_error_message
    import capo_bedrock_agentcore.types.recommendation_result_configuration_bundle
    import capo_bedrock_agentcore.types.tool_description_result_list


class ToolDescriptionRecommendationResult(TypedDict, closed=True):
    tools: NotRequired[
        "capo_bedrock_agentcore.types.tool_description_result_list.ToolDescriptionResultList"
    ]
    """<p>The list of tools with their recommended descriptions.</p>"""
    configuration_bundle: NotRequired[
        "capo_bedrock_agentcore.types.recommendation_result_configuration_bundle.RecommendationResultConfigurationBundle"
    ]
    """<p>The configuration bundle containing the recommended tool descriptions, if the input was sourced from a configuration bundle.</p>"""
    error_code: NotRequired[
        "capo_bedrock_agentcore.types.recommendation_error_code.RecommendationErrorCode"
    ]
    """<p>The error code if the recommendation failed.</p>"""
    error_message: NotRequired[
        "capo_bedrock_agentcore.types.recommendation_error_message.RecommendationErrorMessage"
    ]
    """<p>The error message if the recommendation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolDescriptionRecommendationResult) -> dict:
    out: dict = {}
    if "tools" in value:
        import capo_bedrock_agentcore.types.tool_description_result_list

        out["tools"] = (
            capo_bedrock_agentcore.types.tool_description_result_list.serialize_json(
                value["tools"]
            )
        )
    if "configuration_bundle" in value:
        import capo_bedrock_agentcore.types.recommendation_result_configuration_bundle

        out["configurationBundle"] = (
            capo_bedrock_agentcore.types.recommendation_result_configuration_bundle.serialize_json(
                value["configuration_bundle"]
            )
        )
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ToolDescriptionRecommendationResult:
    out: ToolDescriptionRecommendationResult = {}  # type: ignore[typeddict-item]
    if data.get("tools") is not None:
        import capo_bedrock_agentcore.types.tool_description_result_list

        out["tools"] = (
            capo_bedrock_agentcore.types.tool_description_result_list.deserialize_json(
                data["tools"]
            )
        )
    if data.get("configurationBundle") is not None:
        import capo_bedrock_agentcore.types.recommendation_result_configuration_bundle

        out["configuration_bundle"] = (
            capo_bedrock_agentcore.types.recommendation_result_configuration_bundle.deserialize_json(
                data["configurationBundle"]
            )
        )
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out


def redact_sensitive(value: ToolDescriptionRecommendationResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tools" in value:
        import capo_bedrock_agentcore.types.tool_description_result_list

        out["tools"] = (
            capo_bedrock_agentcore.types.tool_description_result_list.redact_sensitive(
                value["tools"]
            )
        )
    return out
