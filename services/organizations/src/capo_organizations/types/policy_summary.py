"""Generated from Smithy shape ``com.amazonaws.organizations#PolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.aws_managed_policy
    import capo_organizations.types.policy_arn
    import capo_organizations.types.policy_description
    import capo_organizations.types.policy_id
    import capo_organizations.types.policy_name
    import capo_organizations.types.policy_type


class PolicySummary(TypedDict, closed=True):
    id: NotRequired["capo_organizations.types.policy_id.PolicyId"]
    """<p>The unique identifier (ID) of the policy.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for a policy ID string requires "p-" followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).</p>"""
    arn: NotRequired["capo_organizations.types.policy_arn.PolicyArn"]
    """<p>The Amazon Resource Name (ARN) of the policy.</p> <p>For more information about ARNs in Organizations, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies">ARN Formats Supported by Organizations</a> in the <i>Amazon Web Services Service Authorization Reference</i>.</p>"""
    name: NotRequired["capo_organizations.types.policy_name.PolicyName"]
    """<p>The friendly name of the policy.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> that is used to validate this parameter is a string of any of the characters in the ASCII character range.</p>"""
    description: NotRequired[
        "capo_organizations.types.policy_description.PolicyDescription"
    ]
    """<p>The description of the policy.</p>"""
    type: NotRequired["capo_organizations.types.policy_type.PolicyType"]
    """<p>The type of policy.</p>"""
    aws_managed: "capo_organizations.types.aws_managed_policy.AwsManagedPolicy"
    """<p>A boolean value that indicates whether the specified policy is an Amazon Web Services managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicySummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import capo_organizations.types.policy_type

        out["Type"] = capo_organizations.types.policy_type.serialize_aws_json_1_1(
            value["type"]
        )
    out["AwsManaged"] = value.get("aws_managed", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicySummary:
    out: PolicySummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Type") is not None:
        import capo_organizations.types.policy_type

        out["type"] = capo_organizations.types.policy_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("AwsManaged") is not None:
        out["aws_managed"] = data["AwsManaged"]
    else:
        out["aws_managed"] = False
    return out
