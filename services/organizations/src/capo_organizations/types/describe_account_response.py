"""Generated from Smithy shape ``com.amazonaws.organizations#DescribeAccountResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.account


class DescribeAccountResponse(TypedDict, closed=True):
    account: NotRequired["capo_organizations.types.account.Account"]
    """<p>A structure that contains information about the requested account.</p> <important> <p>The <code>Status</code> parameter in the API response will be retired on September 9, 2026. Although both the account <code>State</code> and account <code>Status</code> parameters are currently available in the Organizations APIs (<code>DescribeAccount</code>, <code>ListAccounts</code>, <code>ListAccountsForParent</code>), we recommend that you update your scripts or other code to use the <code>State</code> parameter instead of <code>Status</code> before September 9, 2026.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccountResponse) -> dict:
    out: dict = {}
    if "account" in value:
        import capo_organizations.types.account

        out["Account"] = capo_organizations.types.account.serialize_aws_json_1_1(
            value["account"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccountResponse:
    out: DescribeAccountResponse = {}  # type: ignore[typeddict-item]
    if data.get("Account") is not None:
        import capo_organizations.types.account

        out["account"] = capo_organizations.types.account.deserialize_aws_json_1_1(
            data["Account"]
        )
    return out


def redact_sensitive(value: DescribeAccountResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "account" in value:
        import capo_organizations.types.account

        out["account"] = capo_organizations.types.account.redact_sensitive(
            value["account"]
        )
    return out
