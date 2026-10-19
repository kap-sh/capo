"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#StopEngagementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.ssm_contacts_arn
    import capo_ssm_contacts.types.stop_reason


class StopEngagementRequest(TypedDict, closed=True):
    engagement_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the engagement.</p>"""
    reason: NotRequired["capo_ssm_contacts.types.stop_reason.StopReason"]
    """<p>The reason that you're stopping the engagement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopEngagementRequest) -> dict:
    out: dict = {}
    out["EngagementId"] = value["engagement_id"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopEngagementRequest:
    out: StopEngagementRequest = {}  # type: ignore[typeddict-item]
    if data.get("EngagementId") is not None:
        out["engagement_id"] = data["EngagementId"]
    else:
        out["engagement_id"] = ""
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    return out
