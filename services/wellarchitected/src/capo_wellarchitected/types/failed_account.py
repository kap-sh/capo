"""Generated from Smithy shape ``com.amazonaws.wellarchitected#FailedAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.account_id


class FailedAccount(TypedDict, closed=True):
    account_id: "capo_wellarchitected.types.account_id.AccountId"
    """<p>The AWS account ID that failed.</p>"""
    reason: "str"
    """<p>A human-readable explanation of why the account could not be processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedAccount) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> FailedAccount:
    out: FailedAccount = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    else:
        out["reason"] = ""
    return out
