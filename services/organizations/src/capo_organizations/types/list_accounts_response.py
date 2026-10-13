"""Generated from Smithy shape ``com.amazonaws.organizations#ListAccountsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.accounts
    import capo_organizations.types.next_token


class ListAccountsResponse(TypedDict, closed=True):
    accounts: NotRequired["capo_organizations.types.accounts.Accounts"]
    """<p>A list of objects in the organization.</p> <important> <p>The <code>Status</code> parameter in the API response will be retired on September 9, 2026. Although both the account <code>State</code> and account <code>Status</code> parameters are currently available in the Organizations APIs (<code>DescribeAccount</code>, <code>ListAccounts</code>, <code>ListAccountsForParent</code>), we recommend that you update your scripts or other code to use the <code>State</code> parameter instead of <code>Status</code> before September 9, 2026.</p> </important>"""
    next_token: NotRequired["capo_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccountsResponse) -> dict:
    out: dict = {}
    if "accounts" in value:
        import capo_organizations.types.accounts

        out["Accounts"] = capo_organizations.types.accounts.serialize_aws_json_1_1(
            value["accounts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccountsResponse:
    out: ListAccountsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Accounts") is not None:
        import capo_organizations.types.accounts

        out["accounts"] = capo_organizations.types.accounts.deserialize_aws_json_1_1(
            data["Accounts"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListAccountsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "accounts" in value:
        import capo_organizations.types.accounts

        out["accounts"] = capo_organizations.types.accounts.redact_sensitive(
            value["accounts"]
        )
    return out
