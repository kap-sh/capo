"""Generated from Smithy shape ``com.amazonaws.guardduty#AccountDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_id
    import capo_guardduty.types.email


class AccountDetail(TypedDict, closed=True):
    account_id: NotRequired["capo_guardduty.types.account_id.AccountId"]
    """<p>The member account ID.</p>"""
    email: NotRequired["capo_guardduty.types.email.Email"]
    r"""<p>The email address of the member account. The following list includes the rules for a valid email address:</p> <ul> <li> <p>The email address must be a minimum of 6 and a maximum of 64 characters long.</p> </li> <li> <p>All characters must be 7-bit ASCII characters.</p> </li> <li> <p>There must be one and only one @ symbol, which separates the local name from the domain name.</p> </li> <li> <p>The local name can't contain any of the following characters:</p> <p>whitespace, " ' ( ) &lt; &gt; [ ] : ' , \ | % &amp;</p> </li> <li> <p>The local name can't begin with a dot (.).</p> </li> <li> <p>The domain name can consist of only the characters [a-z], [A-Z], [0-9], hyphen (-), or dot (.).</p> </li> <li> <p>The domain name can't begin or end with a dot (.) or hyphen (-).</p> </li> <li> <p>The domain name must contain at least one dot. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountDetail) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "email" in value:
        out["email"] = value["email"]
    return out


def deserialize_json(data: dict) -> AccountDetail:
    out: AccountDetail = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("email") is not None:
        out["email"] = data["email"]
    return out
