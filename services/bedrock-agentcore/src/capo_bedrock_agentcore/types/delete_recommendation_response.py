"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeleteRecommendationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.recommendation_id
    import capo_bedrock_agentcore.types.recommendation_status


class DeleteRecommendationResponse(TypedDict, closed=True):
    recommendation_id: "capo_bedrock_agentcore.types.recommendation_id.RecommendationId"
    """<p>The unique identifier of the deleted recommendation.</p>"""
    status: "capo_bedrock_agentcore.types.recommendation_status.RecommendationStatus"
    """<p>The status of the recommendation deletion operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecommendationResponse) -> dict:
    out: dict = {}
    out["recommendationId"] = value["recommendation_id"]
    import capo_bedrock_agentcore.types.recommendation_status

    out["status"] = capo_bedrock_agentcore.types.recommendation_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteRecommendationResponse:
    out: DeleteRecommendationResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendationId") is not None:
        out["recommendation_id"] = data["recommendationId"]
    else:
        out["recommendation_id"] = ""
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
    return out
