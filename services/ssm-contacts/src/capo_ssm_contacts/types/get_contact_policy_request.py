"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#GetContactPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.ssm_contacts_arn


class GetContactPolicyRequest(TypedDict, closed=True):
    contact_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact or escalation plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContactPolicyRequest) -> dict:
    out: dict = {}
    out["ContactArn"] = value["contact_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContactPolicyRequest:
    out: GetContactPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContactArn") is not None:
        out["contact_arn"] = data["ContactArn"]
    else:
        out["contact_arn"] = ""
    return out
