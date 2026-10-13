"""Generated from Smithy shape ``com.amazonaws.detective#Account``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_detective.errors import DeserializationError

if TYPE_CHECKING:
    import capo_detective.types.account_id
    import capo_detective.types.email_address


class Account(TypedDict, closed=True):
    account_id: "capo_detective.types.account_id.AccountId"
    """<p>The account identifier of the Amazon Web Services account.</p>"""
    email_address: "capo_detective.types.email_address.EmailAddress"
    """<p>The Amazon Web Services account root user email address for the Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Account) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["EmailAddress"] = value["email_address"]
    return out


def deserialize_json(data: dict) -> Account:
    out: Account = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("Account.account_id required")
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    else:
        raise DeserializationError("Account.email_address required")
    return out


def redact_sensitive(value: Account) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    return out
