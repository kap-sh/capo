"""Generated from Smithy shape ``com.amazonaws.organizations#PolicyTargetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.generic_arn
    import capo_organizations.types.policy_target_id
    import capo_organizations.types.target_name
    import capo_organizations.types.target_type


class PolicyTargetSummary(TypedDict, closed=True):
    target_id: NotRequired["capo_organizations.types.policy_target_id.PolicyTargetId"]
    """<p>The unique identifier (ID) of the policy target.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for a target ID string requires one of the following:</p> <ul> <li> <p> <b>Root</b> - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits.</p> </li> <li> <p> <b>Account</b> - A string that consists of exactly 12 digits.</p> </li> <li> <p> <b>Organizational unit (OU)</b> - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.</p> </li> </ul>"""
    arn: NotRequired["capo_organizations.types.generic_arn.GenericArn"]
    """<p>The Amazon Resource Name (ARN) of the policy target.</p> <p>For more information about ARNs in Organizations, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies">ARN Formats Supported by Organizations</a> in the <i>Amazon Web Services Service Authorization Reference</i>.</p>"""
    name: NotRequired["capo_organizations.types.target_name.TargetName"]
    """<p>The friendly name of the policy target.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> that is used to validate this parameter is a string of any of the characters in the ASCII character range.</p>"""
    type: NotRequired["capo_organizations.types.target_type.TargetType"]
    """<p>The type of the policy target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyTargetSummary) -> dict:
    out: dict = {}
    if "target_id" in value:
        out["TargetId"] = value["target_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_organizations.types.target_type

        out["Type"] = capo_organizations.types.target_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicyTargetSummary:
    out: PolicyTargetSummary = {}  # type: ignore[typeddict-item]
    if data.get("TargetId") is not None:
        out["target_id"] = data["TargetId"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        import capo_organizations.types.target_type

        out["type"] = capo_organizations.types.target_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out
