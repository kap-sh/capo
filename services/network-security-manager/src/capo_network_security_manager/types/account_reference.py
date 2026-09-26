"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AccountReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.account_id
    import capo_network_security_manager.types.sensitive_account_email
    import capo_network_security_manager.types.sensitive_account_name


class AccountReference(TypedDict, closed=True):
    account_id: "capo_network_security_manager.types.account_id.AccountId"
    """<p>The AWS account ID.</p>"""
    name: NotRequired[
        "capo_network_security_manager.types.sensitive_account_name.SensitiveAccountName"
    ]
    """<p>The display name of the account.</p>"""
    email: NotRequired[
        "capo_network_security_manager.types.sensitive_account_email.SensitiveAccountEmail"
    ]
    """<p>The email address associated with the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountReference) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "email" in value:
        out["email"] = value["email"]
    return out


def deserialize_json(data: dict) -> AccountReference:
    out: AccountReference = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("AccountReference.account_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("email") is not None:
        out["email"] = data["email"]
    return out
