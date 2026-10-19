"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#UpdateOrganizationRecommendationLifecycleRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.organization_recommendation_identifier
    import capo_trustedadvisor.types.recommendation_update_reason
    import capo_trustedadvisor.types.update_recommendation_lifecycle_stage
    import capo_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code


class UpdateOrganizationRecommendationLifecycleRequest(TypedDict, closed=True):
    lifecycle_stage: "capo_trustedadvisor.types.update_recommendation_lifecycle_stage.UpdateRecommendationLifecycleStage"
    """<p>The new lifecycle stage</p>"""
    update_reason: NotRequired[
        "capo_trustedadvisor.types.recommendation_update_reason.RecommendationUpdateReason"
    ]
    """<p>Reason for the lifecycle stage change</p>"""
    update_reason_code: NotRequired[
        "capo_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code.UpdateRecommendationLifecycleStageReasonCode"
    ]
    """<p>Reason code for the lifecycle state change</p>"""
    organization_recommendation_identifier: "capo_trustedadvisor.types.organization_recommendation_identifier.OrganizationRecommendationIdentifier"
    """<p>The Recommendation identifier for AWS Trusted Advisor Priority recommendations</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOrganizationRecommendationLifecycleRequest) -> dict:
    out: dict = {}
    import capo_trustedadvisor.types.update_recommendation_lifecycle_stage

    out["lifecycleStage"] = (
        capo_trustedadvisor.types.update_recommendation_lifecycle_stage.serialize_json(
            value["lifecycle_stage"]
        )
    )
    if "update_reason" in value:
        out["updateReason"] = value["update_reason"]
    if "update_reason_code" in value:
        import capo_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code

        out["updateReasonCode"] = (
            capo_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code.serialize_json(
                value["update_reason_code"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateOrganizationRecommendationLifecycleRequest:
    out: UpdateOrganizationRecommendationLifecycleRequest = {}  # type: ignore[typeddict-item]
    if data.get("lifecycleStage") is not None:
        import capo_trustedadvisor.types.update_recommendation_lifecycle_stage

        out["lifecycle_stage"] = (
            capo_trustedadvisor.types.update_recommendation_lifecycle_stage.deserialize_json(
                data["lifecycleStage"]
            )
        )
    else:
        import typing

        out["lifecycle_stage"] = typing.cast(
            "capo_trustedadvisor.types.update_recommendation_lifecycle_stage.UpdateRecommendationLifecycleStage",
            "",
        )
    if data.get("updateReason") is not None:
        out["update_reason"] = data["updateReason"]
    if data.get("updateReasonCode") is not None:
        import capo_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code

        out["update_reason_code"] = (
            capo_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code.deserialize_json(
                data["updateReasonCode"]
            )
        )
    return out


def redact_sensitive(
    value: UpdateOrganizationRecommendationLifecycleRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "update_reason" in value:
        out["update_reason"] = "*** Sensitive Data Redacted ***"
    return out
