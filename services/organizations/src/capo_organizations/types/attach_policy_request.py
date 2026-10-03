"""Generated from Smithy shape ``com.amazonaws.organizations#AttachPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.policy_id
    import capo_organizations.types.policy_target_id


class AttachPolicyRequest(TypedDict, closed=True):
    policy_id: "capo_organizations.types.policy_id.PolicyId"
    """<p>ID for the policy that you want to attach to the target. You can get the ID for the policy by calling the <a>ListPolicies</a> operation.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for a policy ID string requires "p-" followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).</p>"""
    target_id: "capo_organizations.types.policy_target_id.PolicyTargetId"
    """<p>ID for the root, OU, or account that you want to attach the policy to. You can get the ID by calling the <a>ListRoots</a>, <a>ListOrganizationalUnitsForParent</a>, or <a>ListAccounts</a> operations.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for a target ID string requires one of the following:</p> <ul> <li> <p> <b>Root</b> - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits.</p> </li> <li> <p> <b>Account</b> - A string that consists of exactly 12 digits.</p> </li> <li> <p> <b>Organizational unit (OU)</b> - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachPolicyRequest) -> dict:
    out: dict = {}
    out["PolicyId"] = value["policy_id"]
    out["TargetId"] = value["target_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachPolicyRequest:
    out: AttachPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    else:
        raise DeserializationError("AttachPolicyRequest.policy_id required")
    if data.get("TargetId") is not None:
        out["target_id"] = data["TargetId"]
    else:
        raise DeserializationError("AttachPolicyRequest.target_id required")
    return out
