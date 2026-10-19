"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#PutContactPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.policy
    import capo_ssm_contacts.types.ssm_contacts_arn


class PutContactPolicyRequest(TypedDict, closed=True):
    contact_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact or escalation plan.</p>"""
    policy: "capo_ssm_contacts.types.policy.Policy"
    """<p>Details of the resource policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutContactPolicyRequest) -> dict:
    out: dict = {}
    out["ContactArn"] = value["contact_arn"]
    out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutContactPolicyRequest:
    out: PutContactPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContactArn") is not None:
        out["contact_arn"] = data["ContactArn"]
    else:
        out["contact_arn"] = ""
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        out["policy"] = ""
    return out
