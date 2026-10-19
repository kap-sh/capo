"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DescribePageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.ssm_contacts_arn


class DescribePageRequest(TypedDict, closed=True):
    page_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ID of the engagement to a contact channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePageRequest) -> dict:
    out: dict = {}
    out["PageId"] = value["page_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePageRequest:
    out: DescribePageRequest = {}  # type: ignore[typeddict-item]
    if data.get("PageId") is not None:
        out["page_id"] = data["PageId"]
    else:
        out["page_id"] = ""
    return out
