"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StartRecommendationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.kms_key_arn
    import capo_bedrock_agentcore.types.recommendation_config
    import capo_bedrock_agentcore.types.recommendation_description
    import capo_bedrock_agentcore.types.recommendation_name
    import capo_bedrock_agentcore.types.recommendation_type
    import capo_bedrock_agentcore.types.tags_map


class StartRecommendationRequest(TypedDict, closed=True):
    name: "capo_bedrock_agentcore.types.recommendation_name.RecommendationName"
    """<p>The name of the recommendation. Must be unique within your account.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore.types.recommendation_description.RecommendationDescription"
    ]
    """<p>The description of the recommendation.</p>"""
    type: "capo_bedrock_agentcore.types.recommendation_type.RecommendationType"
    """<p>The type of recommendation to generate. Valid values are <code>SYSTEM_PROMPT_RECOMMENDATION</code> for system prompt optimization or <code>TOOL_DESCRIPTION_RECOMMENDATION</code> for tool description optimization.</p>"""
    recommendation_config: (
        "capo_bedrock_agentcore.types.recommendation_config.RecommendationConfig"
    )
    """<p>The configuration for the recommendation, including the input to optimize, agent traces to analyze, and evaluation settings.</p>"""
    kms_key_arn: NotRequired["capo_bedrock_agentcore.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key used to encrypt recommendation data. If provided, customer data is encrypted at rest with the specified key.</p>"""
    client_token: NotRequired["capo_bedrock_agentcore.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""
    tags: NotRequired["capo_bedrock_agentcore.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to associate with the recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRecommendationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore.types.recommendation_type

    out["type"] = capo_bedrock_agentcore.types.recommendation_type.serialize_json(
        value["type"]
    )
    import capo_bedrock_agentcore.types.recommendation_config

    out["recommendationConfig"] = (
        capo_bedrock_agentcore.types.recommendation_config.serialize_json(
            value["recommendation_config"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_bedrock_agentcore.types.tags_map

        out["tags"] = capo_bedrock_agentcore.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> StartRecommendationRequest:
    out: StartRecommendationRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        import capo_bedrock_agentcore.types.recommendation_type

        out["type"] = capo_bedrock_agentcore.types.recommendation_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agentcore.types.recommendation_type.RecommendationType", ""
        )
    if data.get("recommendationConfig") is not None:
        import capo_bedrock_agentcore.types.recommendation_config

        out["recommendation_config"] = (
            capo_bedrock_agentcore.types.recommendation_config.deserialize_json(
                data["recommendationConfig"]
            )
        )
    else:
        out["recommendation_config"] = {"$unknown": {"name": ""}}
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_bedrock_agentcore.types.tags_map

        out["tags"] = capo_bedrock_agentcore.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out


def redact_sensitive(value: StartRecommendationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recommendation_config" in value:
        import capo_bedrock_agentcore.types.recommendation_config

        out["recommendation_config"] = (
            capo_bedrock_agentcore.types.recommendation_config.redact_sensitive(
                value["recommendation_config"]
            )
        )
    return out
