"""Generated from Smithy shape ``com.amazonaws.accountaccessruntime#AccessDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account_access_runtime.types.account


class AccessDetails(TypedDict, closed=True):
    account_id: "capo_account_access_runtime.types.account.Account"
    """<p>The 12-digit identifier of the Amazon Web Services account that contains the role.</p>"""
    account_name: NotRequired["str"]
    """<p>The display name of the Amazon Web Services account, if available. This value can be absent when the account name can't be resolved.</p>"""
    role_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the role that you can access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDetails) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    if "account_name" in value:
        out["accountName"] = value["account_name"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> AccessDetails:
    out: AccessDetails = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("accountName") is not None:
        out["account_name"] = data["accountName"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
