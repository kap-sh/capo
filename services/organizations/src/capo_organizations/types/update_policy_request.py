"""Generated from Smithy shape ``com.amazonaws.organizations#UpdatePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.policy_content
    import capo_organizations.types.policy_description
    import capo_organizations.types.policy_id
    import capo_organizations.types.policy_name


class UpdatePolicyRequest(TypedDict, closed=True):
    policy_id: "capo_organizations.types.policy_id.PolicyId"
    """<p>ID for the policy that you want to update.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for a policy ID string requires "p-" followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).</p>"""
    name: NotRequired["capo_organizations.types.policy_name.PolicyName"]
    """<p>If provided, the new name for the policy.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> that is used to validate this parameter is a string of any of the characters in the ASCII character range.</p>"""
    description: NotRequired[
        "capo_organizations.types.policy_description.PolicyDescription"
    ]
    """<p>If provided, the new description for the policy.</p>"""
    content: NotRequired["capo_organizations.types.policy_content.PolicyContent"]
    """<p>If provided, the new content for the policy. The text must be correctly formatted JSON that complies with the syntax for the policy's type. For more information, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html">SCP syntax</a> in the <i>Organizations User Guide</i>.</p> <p>The maximum size of a policy document depends on the policy's type. For more information, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html#min-max-values">Maximum and minimum values</a> in the <i>Organizations User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePolicyRequest) -> dict:
    out: dict = {}
    out["PolicyId"] = value["policy_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "content" in value:
        out["Content"] = value["content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePolicyRequest:
    out: UpdatePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    else:
        raise DeserializationError("UpdatePolicyRequest.policy_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    return out
