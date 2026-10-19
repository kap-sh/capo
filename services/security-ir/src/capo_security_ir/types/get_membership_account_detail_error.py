"""Generated from Smithy shape ``com.amazonaws.securityir#GetMembershipAccountDetailError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.aws_account_id


class GetMembershipAccountDetailError(TypedDict, closed=True):
    account_id: "capo_security_ir.types.aws_account_id.AWSAccountId"
    """<p/>"""
    error: "str"
    """<p/>"""
    message: "str"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMembershipAccountDetailError) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["error"] = value["error"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> GetMembershipAccountDetailError:
    out: GetMembershipAccountDetailError = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("error") is not None:
        out["error"] = data["error"]
    else:
        out["error"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
