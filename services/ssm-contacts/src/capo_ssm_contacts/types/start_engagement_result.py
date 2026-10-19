"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#StartEngagementResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.ssm_contacts_arn


class StartEngagementResult(TypedDict, closed=True):
    engagement_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the engagement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartEngagementResult) -> dict:
    out: dict = {}
    out["EngagementArn"] = value["engagement_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartEngagementResult:
    out: StartEngagementResult = {}  # type: ignore[typeddict-item]
    if data.get("EngagementArn") is not None:
        out["engagement_arn"] = data["EngagementArn"]
    else:
        out["engagement_arn"] = ""
    return out
