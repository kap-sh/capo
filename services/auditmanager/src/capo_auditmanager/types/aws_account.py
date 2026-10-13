"""Generated from Smithy shape ``com.amazonaws.auditmanager#AWSAccount``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.account_id
    import capo_auditmanager.types.account_name
    import capo_auditmanager.types.email_address


class AWSAccount(TypedDict, closed=True):
    id: NotRequired["capo_auditmanager.types.account_id.AccountId"]
    """<p> The identifier for the Amazon Web Services account. </p>"""
    email_address: NotRequired["capo_auditmanager.types.email_address.EmailAddress"]
    """<p> The email address that's associated with the Amazon Web Services account. </p>"""
    name: NotRequired["capo_auditmanager.types.account_name.AccountName"]
    """<p> The name of the Amazon Web Services account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AWSAccount) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "email_address" in value:
        out["emailAddress"] = value["email_address"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AWSAccount:
    out: AWSAccount = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("emailAddress") is not None:
        out["email_address"] = data["emailAddress"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out


def redact_sensitive(value: AWSAccount) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    return out
