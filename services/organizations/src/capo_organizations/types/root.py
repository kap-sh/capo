"""Generated from Smithy shape ``com.amazonaws.organizations#Root``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.policy_types
    import capo_organizations.types.root_arn
    import capo_organizations.types.root_id
    import capo_organizations.types.root_name


class Root(TypedDict, closed=True):
    id: NotRequired["capo_organizations.types.root_id.RootId"]
    """<p>The unique identifier (ID) for the root. The ID is unique to the organization only.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for a root ID string requires "r-" followed by from 4 to 32 lowercase letters or digits.</p>"""
    arn: NotRequired["capo_organizations.types.root_arn.RootArn"]
    """<p>The Amazon Resource Name (ARN) of the root.</p> <p>For more information about ARNs in Organizations, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies">ARN Formats Supported by Organizations</a> in the <i>Amazon Web Services Service Authorization Reference</i>.</p>"""
    name: NotRequired["capo_organizations.types.root_name.RootName"]
    """<p>The friendly name of the root.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> that is used to validate this parameter is a string of any of the characters in the ASCII character range.</p>"""
    policy_types: NotRequired["capo_organizations.types.policy_types.PolicyTypes"]
    """<p>The types of policies that are currently enabled for the root and therefore can be attached to the root or to its OUs or accounts.</p> <note> <p>Even if a policy type is shown as available in the organization, you can separately enable and disable them at the root level by using <a>EnablePolicyType</a> and <a>DisablePolicyType</a>. Use <a>DescribeOrganization</a> to see the availability of the policy types in that organization.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Root) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "policy_types" in value:
        import capo_organizations.types.policy_types

        out["PolicyTypes"] = (
            capo_organizations.types.policy_types.serialize_aws_json_1_1(
                value["policy_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Root:
    out: Root = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("PolicyTypes") is not None:
        import capo_organizations.types.policy_types

        out["policy_types"] = (
            capo_organizations.types.policy_types.deserialize_aws_json_1_1(
                data["PolicyTypes"]
            )
        )
    return out
