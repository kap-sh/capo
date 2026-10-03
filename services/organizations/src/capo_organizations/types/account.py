"""Generated from Smithy shape ``com.amazonaws.organizations#Account``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.account_arn
    import capo_organizations.types.account_id
    import capo_organizations.types.account_joined_method
    import capo_organizations.types.account_name
    import capo_organizations.types.account_state
    import capo_organizations.types.account_status
    import capo_organizations.types.email
    import capo_organizations.types.paths
    import capo_organizations.types.timestamp


class Account(TypedDict, closed=True):
    id: NotRequired["capo_organizations.types.account_id.AccountId"]
    """<p>The unique identifier (ID) of the account.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for an account ID string requires exactly 12 digits.</p>"""
    arn: NotRequired["capo_organizations.types.account_arn.AccountArn"]
    """<p>The Amazon Resource Name (ARN) of the account.</p> <p>For more information about ARNs in Organizations, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies">ARN Formats Supported by Organizations</a> in the <i>Amazon Web Services Service Authorization Reference</i>.</p>"""
    email: NotRequired["capo_organizations.types.email.Email"]
    """<p>The email address associated with the Amazon Web Services account.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for this parameter is a string of characters that represents a standard internet email address.</p>"""
    name: NotRequired["capo_organizations.types.account_name.AccountName"]
    """<p>The friendly name of the account.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> that is used to validate this parameter is a string of any of the characters in the ASCII character range.</p>"""
    status: NotRequired["capo_organizations.types.account_status.AccountStatus"]
    """<p>The status of the account in the organization.</p> <important> <p>The <code>Status</code> parameter in the <code>Account</code> object will be retired on September 9, 2026. Although both the account <code>State</code> and account <code>Status</code> parameters are currently available in the Organizations APIs (<code>DescribeAccount</code>, <code>ListAccounts</code>, <code>ListAccountsForParent</code>), we recommend that you update your scripts or other code to use the <code>State</code> parameter instead of <code>Status</code> before September 9, 2026.</p> </important>"""
    state: NotRequired["capo_organizations.types.account_state.AccountState"]
    """<p>Each state represents a specific phase in the account lifecycle. Use this information to manage account access, automate workflows, or trigger actions based on account state changes.</p> <p>For more information about account states and their implications, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_account_state.html">Monitor the state of your Amazon Web Services accounts </a> in the <i>Organizations User Guide</i>.</p>"""
    paths: NotRequired["capo_organizations.types.paths.Paths"]
    """<p>The paths in the organization where the account exists.</p>"""
    joined_method: NotRequired[
        "capo_organizations.types.account_joined_method.AccountJoinedMethod"
    ]
    """<p>The method by which the account joined the organization.</p>"""
    joined_timestamp: NotRequired["capo_organizations.types.timestamp.Timestamp"]
    """<p>The date the account became a part of the organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Account) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "email" in value:
        out["Email"] = value["email"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_organizations.types.account_status

        out["Status"] = capo_organizations.types.account_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "state" in value:
        import capo_organizations.types.account_state

        out["State"] = capo_organizations.types.account_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "paths" in value:
        import capo_organizations.types.paths

        out["Paths"] = capo_organizations.types.paths.serialize_aws_json_1_1(
            value["paths"]
        )
    if "joined_method" in value:
        import capo_organizations.types.account_joined_method

        out["JoinedMethod"] = (
            capo_organizations.types.account_joined_method.serialize_aws_json_1_1(
                value["joined_method"]
            )
        )
    if "joined_timestamp" in value:
        import capo_organizations.types.timestamp

        out["JoinedTimestamp"] = (
            capo_organizations.types.timestamp.serialize_aws_json_1_1(
                value["joined_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Account:
    out: Account = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_organizations.types.account_status

        out["status"] = (
            capo_organizations.types.account_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("State") is not None:
        import capo_organizations.types.account_state

        out["state"] = capo_organizations.types.account_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("Paths") is not None:
        import capo_organizations.types.paths

        out["paths"] = capo_organizations.types.paths.deserialize_aws_json_1_1(
            data["Paths"]
        )
    if data.get("JoinedMethod") is not None:
        import capo_organizations.types.account_joined_method

        out["joined_method"] = (
            capo_organizations.types.account_joined_method.deserialize_aws_json_1_1(
                data["JoinedMethod"]
            )
        )
    if data.get("JoinedTimestamp") is not None:
        import capo_organizations.types.timestamp

        out["joined_timestamp"] = (
            capo_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["JoinedTimestamp"]
            )
        )
    return out
