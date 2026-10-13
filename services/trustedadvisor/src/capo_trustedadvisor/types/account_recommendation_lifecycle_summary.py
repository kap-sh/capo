"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#AccountRecommendationLifecycleSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_trustedadvisor.types.account_id
    import capo_trustedadvisor.types.account_recommendation_arn
    import capo_trustedadvisor.types.recommendation_lifecycle_stage
    import capo_trustedadvisor.types.recommendation_update_reason
    import capo_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code


class AccountRecommendationLifecycleSummary(TypedDict, closed=True):
    account_id: NotRequired["capo_trustedadvisor.types.account_id.AccountId"]
    """<p>The AWS account ID</p>"""
    account_recommendation_arn: NotRequired[
        "capo_trustedadvisor.types.account_recommendation_arn.AccountRecommendationArn"
    ]
    """<p>The Recommendation ARN</p>"""
    lifecycle_stage: NotRequired[
        "capo_trustedadvisor.types.recommendation_lifecycle_stage.RecommendationLifecycleStage"
    ]
    """<p>The lifecycle stage from AWS Trusted Advisor Priority</p>"""
    updated_on_behalf_of: NotRequired["str"]
    """<p>The person on whose behalf a Technical Account Manager (TAM) updated the recommendation. This information is only available when a Technical Account Manager takes an action on a recommendation managed by AWS Trusted Advisor Priority </p>"""
    updated_on_behalf_of_job_title: NotRequired["str"]
    """<p>The job title of the person on whose behalf a Technical Account Manager (TAM) updated the recommendation. This information is only available when a Technical Account Manager takes an action on a recommendation managed by AWS Trusted Advisor Priority </p>"""
    update_reason: NotRequired[
        "capo_trustedadvisor.types.recommendation_update_reason.RecommendationUpdateReason"
    ]
    """<p>Reason for the lifecycle stage change</p>"""
    update_reason_code: NotRequired[
        "capo_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code.UpdateRecommendationLifecycleStageReasonCode"
    ]
    """<p>Reason code for the lifecycle state change</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>When the Recommendation was last updated</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountRecommendationLifecycleSummary) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "account_recommendation_arn" in value:
        out["accountRecommendationArn"] = value["account_recommendation_arn"]
    if "lifecycle_stage" in value:
        import capo_trustedadvisor.types.recommendation_lifecycle_stage

        out["lifecycleStage"] = (
            capo_trustedadvisor.types.recommendation_lifecycle_stage.serialize_json(
                value["lifecycle_stage"]
            )
        )
    if "updated_on_behalf_of" in value:
        out["updatedOnBehalfOf"] = value["updated_on_behalf_of"]
    if "updated_on_behalf_of_job_title" in value:
        out["updatedOnBehalfOfJobTitle"] = value["updated_on_behalf_of_job_title"]
    if "update_reason" in value:
        out["updateReason"] = value["update_reason"]
    if "update_reason_code" in value:
        import capo_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code

        out["updateReasonCode"] = (
            capo_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code.serialize_json(
                value["update_reason_code"]
            )
        )
    if "last_updated_at" in value:
        import capo_trustedadvisor._protocol.serialize

        out["lastUpdatedAt"] = capo_trustedadvisor._protocol.serialize.fmt_date_time(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> AccountRecommendationLifecycleSummary:
    out: AccountRecommendationLifecycleSummary = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("accountRecommendationArn") is not None:
        out["account_recommendation_arn"] = data["accountRecommendationArn"]
    if data.get("lifecycleStage") is not None:
        import capo_trustedadvisor.types.recommendation_lifecycle_stage

        out["lifecycle_stage"] = (
            capo_trustedadvisor.types.recommendation_lifecycle_stage.deserialize_json(
                data["lifecycleStage"]
            )
        )
    if data.get("updatedOnBehalfOf") is not None:
        out["updated_on_behalf_of"] = data["updatedOnBehalfOf"]
    if data.get("updatedOnBehalfOfJobTitle") is not None:
        out["updated_on_behalf_of_job_title"] = data["updatedOnBehalfOfJobTitle"]
    if data.get("updateReason") is not None:
        out["update_reason"] = data["updateReason"]
    if data.get("updateReasonCode") is not None:
        import capo_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code

        out["update_reason_code"] = (
            capo_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code.deserialize_json(
                data["updateReasonCode"]
            )
        )
    if data.get("lastUpdatedAt") is not None:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromisoformat(
            data["lastUpdatedAt"].replace("Z", "+00:00")
        )
    return out


def redact_sensitive(value: AccountRecommendationLifecycleSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "update_reason" in value:
        out["update_reason"] = "*** Sensitive Data Redacted ***"
    return out
