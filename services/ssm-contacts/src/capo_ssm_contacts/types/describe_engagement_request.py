"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DescribeEngagementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.ssm_contacts_arn


class DescribeEngagementRequest(TypedDict, closed=True):
    engagement_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the engagement you want the details of.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEngagementRequest) -> dict:
    out: dict = {}
    out["EngagementId"] = value["engagement_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEngagementRequest:
    out: DescribeEngagementRequest = {}  # type: ignore[typeddict-item]
    if data.get("EngagementId") is not None:
        out["engagement_id"] = data["EngagementId"]
    else:
        out["engagement_id"] = ""
    return out
