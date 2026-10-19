"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetRecommendationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.kms_key_arn
    import capo_bedrock_agentcore.types.recommendation_arn
    import capo_bedrock_agentcore.types.recommendation_config
    import capo_bedrock_agentcore.types.recommendation_description
    import capo_bedrock_agentcore.types.recommendation_id
    import capo_bedrock_agentcore.types.recommendation_name
    import capo_bedrock_agentcore.types.recommendation_result
    import capo_bedrock_agentcore.types.recommendation_status
    import capo_bedrock_agentcore.types.recommendation_type


class GetRecommendationResponse(TypedDict, closed=True):
    recommendation_id: "capo_bedrock_agentcore.types.recommendation_id.RecommendationId"
    """<p>The unique identifier of the recommendation.</p>"""
    recommendation_arn: (
        "capo_bedrock_agentcore.types.recommendation_arn.RecommendationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the recommendation.</p>"""
    name: "capo_bedrock_agentcore.types.recommendation_name.RecommendationName"
    """<p>The name of the recommendation.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore.types.recommendation_description.RecommendationDescription"
    ]
    """<p>The description of the recommendation.</p>"""
    type: "capo_bedrock_agentcore.types.recommendation_type.RecommendationType"
    """<p>The type of recommendation.</p>"""
    recommendation_config: (
        "capo_bedrock_agentcore.types.recommendation_config.RecommendationConfig"
    )
    """<p>The configuration for the recommendation.</p>"""
    status: "capo_bedrock_agentcore.types.recommendation_status.RecommendationStatus"
    """<p>The current status of the recommendation.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the recommendation was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the recommendation was last updated.</p>"""
    recommendation_result: NotRequired[
        "capo_bedrock_agentcore.types.recommendation_result.RecommendationResult"
    ]
    """<p>The result of the recommendation, containing the optimized system prompt or tool descriptions. Only present when the recommendation status is <code>COMPLETED</code>.</p>"""
    kms_key_arn: NotRequired["capo_bedrock_agentcore.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key used to encrypt recommendation data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationResponse) -> dict:
    out: dict = {}
    out["recommendationId"] = value["recommendation_id"]
    out["recommendationArn"] = value["recommendation_arn"]
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
    import capo_bedrock_agentcore.types.recommendation_status

    out["status"] = capo_bedrock_agentcore.types.recommendation_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agentcore._protocol.serialize

    out["createdAt"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_bedrock_agentcore._protocol.serialize

    out["updatedAt"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    if "recommendation_result" in value:
        import capo_bedrock_agentcore.types.recommendation_result

        out["recommendationResult"] = (
            capo_bedrock_agentcore.types.recommendation_result.serialize_json(
                value["recommendation_result"]
            )
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> GetRecommendationResponse:
    out: GetRecommendationResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendationId") is not None:
        out["recommendation_id"] = data["recommendationId"]
    else:
        out["recommendation_id"] = ""
    if data.get("recommendationArn") is not None:
        out["recommendation_arn"] = data["recommendationArn"]
    else:
        out["recommendation_arn"] = ""
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
        import capo_bedrock_agentcore.types._unknown

        out["recommendation_config"] = (
            capo_bedrock_agentcore.types._unknown.UnknownUnionMember("")
        )
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.recommendation_status

        out["status"] = (
            capo_bedrock_agentcore.types.recommendation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore.types.recommendation_status.RecommendationStatus",
            "",
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("recommendationResult") is not None:
        import capo_bedrock_agentcore.types.recommendation_result

        out["recommendation_result"] = (
            capo_bedrock_agentcore.types.recommendation_result.deserialize_json(
                data["recommendationResult"]
            )
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out


def redact_sensitive(value: GetRecommendationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recommendation_config" in value:
        import capo_bedrock_agentcore.types.recommendation_config

        out["recommendation_config"] = (
            capo_bedrock_agentcore.types.recommendation_config.redact_sensitive(
                value["recommendation_config"]
            )
        )
    if "recommendation_result" in value:
        import capo_bedrock_agentcore.types.recommendation_result

        out["recommendation_result"] = (
            capo_bedrock_agentcore.types.recommendation_result.redact_sensitive(
                value["recommendation_result"]
            )
        )
    return out
