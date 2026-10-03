"""Generated from Smithy shape ``com.amazonaws.organizations#CreateGovCloudAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.create_account_name
    import capo_organizations.types.email
    import capo_organizations.types.iam_user_access_to_billing
    import capo_organizations.types.role_name
    import capo_organizations.types.tags


class CreateGovCloudAccountRequest(TypedDict, closed=True):
    email: "capo_organizations.types.email.Email"
    r"""<p>Specifies the email address of the owner to assign to the new member account in the commercial Region. This email address must not already be associated with another Amazon Web Services account. You must use a valid email address to complete account creation.</p> <p>The rules for a valid email address:</p> <ul> <li> <p>The address must be a minimum of 6 and a maximum of 64 characters long.</p> </li> <li> <p>All characters must be 7-bit ASCII characters.</p> </li> <li> <p>There must be one and only one @ symbol, which separates the local name from the domain name.</p> </li> <li> <p>The local name can't contain any of the following characters:</p> <p>whitespace, " ' ( ) < > [ ] : ; , \ | % &</p> </li> <li> <p>The local name can't begin with a dot (.)</p> </li> <li> <p>The domain name can consist of only the characters [a-z],[A-Z],[0-9], hyphen (-), or dot (.)</p> </li> <li> <p>The domain name can't begin or end with a hyphen (-) or dot (.)</p> </li> <li> <p>The domain name must contain at least one dot</p> </li> </ul> <p>You can't access the root user of the account or remove an account that was created with an invalid email address. Like all request parameters for <code>CreateGovCloudAccount</code>, the request for the email address for the Amazon Web Services GovCloud (US) account originates from the commercial Region, not from the Amazon Web Services GovCloud (US) Region.</p>"""
    account_name: "capo_organizations.types.create_account_name.CreateAccountName"
    """<p>The friendly name of the member account. </p> <p>The account name can consist of only the characters [a-z],[A-Z],[0-9], hyphen (-), or dot (.) You can't separate characters with a dash (–).</p>"""
    role_name: NotRequired["capo_organizations.types.role_name.RoleName"]
    """<p>(Optional)</p> <p>The name of an IAM role that Organizations automatically preconfigures in the new member accounts in both the Amazon Web Services GovCloud (US) Region and in the commercial Region. This role trusts the management account, allowing users in the management account to assume the role, as permitted by the management account administrator. The role has administrator permissions in the new member account.</p> <p>If you don't specify this parameter, the role name defaults to <code>OrganizationAccountAccessRole</code>.</p> <p>For more information about how to use this role to access the member account, see the following links:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access.html#orgs_manage_accounts_create-cross-account-role">Creating the OrganizationAccountAccessRole in an invited member account</a> in the <i>Organizations User Guide</i> </p> </li> <li> <p>Steps 2 and 3 in <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html">IAM Tutorial: Delegate access across Amazon Web Services accounts using IAM roles</a> in the <i>IAM User Guide</i> </p> </li> </ul> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> that is used to validate this parameter. The pattern can include uppercase letters, lowercase letters, digits with no spaces, and any of the following characters: =,.@-</p>"""
    iam_user_access_to_billing: NotRequired[
        "capo_organizations.types.iam_user_access_to_billing.IAMUserAccessToBilling"
    ]
    """<p>If set to <code>ALLOW</code>, the new linked account in the commercial Region enables IAM users to access account billing information <i>if</i> they have the required permissions. If set to <code>DENY</code>, only the root user of the new account can access account billing information. For more information, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/grantaccess.html#ControllingAccessWebsite-Activate">About IAM access to the Billing and Cost Management console</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>.</p> <p>If you don't specify this parameter, the value defaults to <code>ALLOW</code>, and IAM users and roles with the required permissions can access billing information for the new account.</p>"""
    tags: NotRequired["capo_organizations.types.tags.Tags"]
    """<p>A list of tags that you want to attach to the newly created account. These tags are attached to the commercial account associated with the GovCloud account, and not to the GovCloud account itself. To add tags to the actual GovCloud account, call the <a>TagResource</a> operation in the GovCloud region after the new GovCloud account exists.</p> <p>For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to <code>null</code>. For more information about tagging, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html">Tagging Organizations resources</a> in the Organizations User Guide.</p> <note> <p>If any one of the tags is not valid or if you exceed the maximum allowed number of tags for an account, then the entire request fails and the account is not created.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGovCloudAccountRequest) -> dict:
    out: dict = {}
    out["Email"] = value["email"]
    out["AccountName"] = value["account_name"]
    if "role_name" in value:
        out["RoleName"] = value["role_name"]
    if "iam_user_access_to_billing" in value:
        import capo_organizations.types.iam_user_access_to_billing

        out["IamUserAccessToBilling"] = (
            capo_organizations.types.iam_user_access_to_billing.serialize_aws_json_1_1(
                value["iam_user_access_to_billing"]
            )
        )
    if "tags" in value:
        import capo_organizations.types.tags

        out["Tags"] = capo_organizations.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGovCloudAccountRequest:
    out: CreateGovCloudAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    else:
        raise DeserializationError("CreateGovCloudAccountRequest.email required")
    if data.get("AccountName") is not None:
        out["account_name"] = data["AccountName"]
    else:
        raise DeserializationError("CreateGovCloudAccountRequest.account_name required")
    if data.get("RoleName") is not None:
        out["role_name"] = data["RoleName"]
    if data.get("IamUserAccessToBilling") is not None:
        import capo_organizations.types.iam_user_access_to_billing

        out["iam_user_access_to_billing"] = (
            capo_organizations.types.iam_user_access_to_billing.deserialize_aws_json_1_1(
                data["IamUserAccessToBilling"]
            )
        )
    if data.get("Tags") is not None:
        import capo_organizations.types.tags

        out["tags"] = capo_organizations.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
