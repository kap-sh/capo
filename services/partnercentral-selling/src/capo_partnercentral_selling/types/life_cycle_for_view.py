"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LifeCycleForView``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.date
    import capo_partnercentral_selling.types.pii_string
    import capo_partnercentral_selling.types.review_status
    import capo_partnercentral_selling.types.stage


class LifeCycleForView(TypedDict, closed=True):
    target_close_date: NotRequired["capo_partnercentral_selling.types.date.Date"]
    """<p> The projected launch date of the opportunity shared through a snapshot. </p>"""
    review_status: NotRequired[
        "capo_partnercentral_selling.types.review_status.ReviewStatus"
    ]
    """<p> Defines the approval status of the opportunity shared through a snapshot. </p>"""
    stage: NotRequired["capo_partnercentral_selling.types.stage.Stage"]
    """<p> Defines the current stage of the opportunity shared through a snapshot. </p>"""
    next_steps: NotRequired["capo_partnercentral_selling.types.pii_string.PiiString"]
    """<p> Describes the next steps for the opportunity shared through a snapshot. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LifeCycleForView) -> dict:
    out: dict = {}
    if "target_close_date" in value:
        out["TargetCloseDate"] = value["target_close_date"]
    if "review_status" in value:
        import capo_partnercentral_selling.types.review_status

        out["ReviewStatus"] = (
            capo_partnercentral_selling.types.review_status.serialize_aws_json_1_0(
                value["review_status"]
            )
        )
    if "stage" in value:
        import capo_partnercentral_selling.types.stage

        out["Stage"] = capo_partnercentral_selling.types.stage.serialize_aws_json_1_0(
            value["stage"]
        )
    if "next_steps" in value:
        out["NextSteps"] = value["next_steps"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LifeCycleForView:
    out: LifeCycleForView = {}  # type: ignore[typeddict-item]
    if data.get("TargetCloseDate") is not None:
        out["target_close_date"] = data["TargetCloseDate"]
    if data.get("ReviewStatus") is not None:
        import capo_partnercentral_selling.types.review_status

        out["review_status"] = (
            capo_partnercentral_selling.types.review_status.deserialize_aws_json_1_0(
                data["ReviewStatus"]
            )
        )
    if data.get("Stage") is not None:
        import capo_partnercentral_selling.types.stage

        out["stage"] = capo_partnercentral_selling.types.stage.deserialize_aws_json_1_0(
            data["Stage"]
        )
    if data.get("NextSteps") is not None:
        out["next_steps"] = data["NextSteps"]
    return out


def redact_sensitive(value: LifeCycleForView) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_steps" in value:
        out["next_steps"] = "*** Sensitive Data Redacted ***"
    return out
