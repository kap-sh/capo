"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateAgentRecommendationStatusRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_wellarchitected.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_recommendation_arn
    import capo_wellarchitected.types.recommendation_status
    import capo_wellarchitected.types.sensitive_string


class UpdateAgentRecommendationStatusRequest(TypedDict, closed=True):
    recommendation_arn: (
        "capo_wellarchitected.types.agent_recommendation_arn.AgentRecommendationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the recommendation to update.</p>"""
    status: "capo_wellarchitected.types.recommendation_status.RecommendationStatus"
    """<p>The new status to assign to the recommendation.</p>"""
    update_reason: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>A free-text reason explaining this status update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentRecommendationStatusRequest) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.recommendation_status

    out["status"] = capo_wellarchitected.types.recommendation_status.serialize_json(
        value["status"]
    )
    if "update_reason" in value:
        out["updateReason"] = value["update_reason"]
    return out


def deserialize_json(data: dict) -> UpdateAgentRecommendationStatusRequest:
    out: UpdateAgentRecommendationStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_wellarchitected.types.recommendation_status

        out["status"] = (
            capo_wellarchitected.types.recommendation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAgentRecommendationStatusRequest.status required"
        )
    if data.get("updateReason") is not None:
        out["update_reason"] = data["updateReason"]
    return out


def redact_sensitive(value: UpdateAgentRecommendationStatusRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "update_reason" in value:
        out["update_reason"] = "*** Sensitive Data Redacted ***"
    return out
