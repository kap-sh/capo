"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsOpportunityLifeCycle``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_closed_lost_reason
    import capo_partnercentral_selling.types.aws_opportunity_stage
    import capo_partnercentral_selling.types.date
    import capo_partnercentral_selling.types.pii_string
    import capo_partnercentral_selling.types.profile_next_steps_histories


class AwsOpportunityLifeCycle(TypedDict, closed=True):
    target_close_date: NotRequired["capo_partnercentral_selling.types.date.Date"]
    """<p>Indicates the expected date by which the opportunity is projected to close. This field helps in planning resources and timelines for both the partner and AWS.</p>"""
    closed_lost_reason: NotRequired[
        "capo_partnercentral_selling.types.aws_closed_lost_reason.AwsClosedLostReason"
    ]
    """<p>Indicates the reason why an opportunity was marked as <code>Closed Lost</code>. This helps in understanding the context behind the lost opportunity and aids in refining future strategies.</p>"""
    stage: NotRequired[
        "capo_partnercentral_selling.types.aws_opportunity_stage.AwsOpportunityStage"
    ]
    """<p>Represents the current stage of the opportunity in its lifecycle, such as <code>Qualification</code>, <code>Validation</code>, or <code>Closed Won</code>. This helps in understanding the opportunity's progress.</p>"""
    next_steps: NotRequired["capo_partnercentral_selling.types.pii_string.PiiString"]
    """<p>Specifies the immediate next steps required to progress the opportunity. These steps are based on AWS guidance and the current stage of the opportunity.</p>"""
    next_steps_history: NotRequired[
        "capo_partnercentral_selling.types.profile_next_steps_histories.ProfileNextStepsHistories"
    ]
    """<p>Provides a historical log of previous next steps that were taken to move the opportunity forward. This helps in tracking the decision-making process and identifying any delays or obstacles encountered.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsOpportunityLifeCycle) -> dict:
    out: dict = {}
    if "target_close_date" in value:
        out["TargetCloseDate"] = value["target_close_date"]
    if "closed_lost_reason" in value:
        import capo_partnercentral_selling.types.aws_closed_lost_reason

        out["ClosedLostReason"] = (
            capo_partnercentral_selling.types.aws_closed_lost_reason.serialize_aws_json_1_0(
                value["closed_lost_reason"]
            )
        )
    if "stage" in value:
        import capo_partnercentral_selling.types.aws_opportunity_stage

        out["Stage"] = (
            capo_partnercentral_selling.types.aws_opportunity_stage.serialize_aws_json_1_0(
                value["stage"]
            )
        )
    if "next_steps" in value:
        out["NextSteps"] = value["next_steps"]
    if "next_steps_history" in value:
        import capo_partnercentral_selling.types.profile_next_steps_histories

        out["NextStepsHistory"] = (
            capo_partnercentral_selling.types.profile_next_steps_histories.serialize_aws_json_1_0(
                value["next_steps_history"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsOpportunityLifeCycle:
    out: AwsOpportunityLifeCycle = {}  # type: ignore[typeddict-item]
    if data.get("TargetCloseDate") is not None:
        out["target_close_date"] = data["TargetCloseDate"]
    if data.get("ClosedLostReason") is not None:
        import capo_partnercentral_selling.types.aws_closed_lost_reason

        out["closed_lost_reason"] = (
            capo_partnercentral_selling.types.aws_closed_lost_reason.deserialize_aws_json_1_0(
                data["ClosedLostReason"]
            )
        )
    if data.get("Stage") is not None:
        import capo_partnercentral_selling.types.aws_opportunity_stage

        out["stage"] = (
            capo_partnercentral_selling.types.aws_opportunity_stage.deserialize_aws_json_1_0(
                data["Stage"]
            )
        )
    if data.get("NextSteps") is not None:
        out["next_steps"] = data["NextSteps"]
    if data.get("NextStepsHistory") is not None:
        import capo_partnercentral_selling.types.profile_next_steps_histories

        out["next_steps_history"] = (
            capo_partnercentral_selling.types.profile_next_steps_histories.deserialize_aws_json_1_0(
                data["NextStepsHistory"]
            )
        )
    return out


def redact_sensitive(value: AwsOpportunityLifeCycle) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_steps" in value:
        out["next_steps"] = "*** Sensitive Data Redacted ***"
    return out
