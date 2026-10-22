"""Generated from Smithy shape ``com.amazonaws.quicksight#ServiceAccountCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.admin_account_email
    import capo_quicksight.types.client_email
    import capo_quicksight.types.private_key


class ServiceAccountCredentials(TypedDict, closed=True):
    admin_account_email: "capo_quicksight.types.admin_account_email.AdminAccountEmail"
    """<p>The email address of the Google Workspace administrator account that the service account impersonates through domain-wide delegation. This field is required.</p>"""
    service_account_private_key: "capo_quicksight.types.private_key.PrivateKey"
    """<p>The private key of the Google service account used for domain-wide delegation. This field is required.</p>"""
    client_email: "capo_quicksight.types.client_email.ClientEmail"
    """<p>The client email address of the Google service account used for domain-wide delegation. This field is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceAccountCredentials) -> dict:
    out: dict = {}
    out["AdminAccountEmail"] = value["admin_account_email"]
    out["ServiceAccountPrivateKey"] = value["service_account_private_key"]
    out["ClientEmail"] = value["client_email"]
    return out


def deserialize_json(data: dict) -> ServiceAccountCredentials:
    out: ServiceAccountCredentials = {}  # type: ignore[typeddict-item]
    if data.get("AdminAccountEmail") is not None:
        out["admin_account_email"] = data["AdminAccountEmail"]
    else:
        out["admin_account_email"] = ""
    if data.get("ServiceAccountPrivateKey") is not None:
        out["service_account_private_key"] = data["ServiceAccountPrivateKey"]
    else:
        out["service_account_private_key"] = ""
    if data.get("ClientEmail") is not None:
        out["client_email"] = data["ClientEmail"]
    else:
        out["client_email"] = ""
    return out


def redact_sensitive(value: ServiceAccountCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service_account_private_key" in value:
        out["service_account_private_key"] = "*** Sensitive Data Redacted ***"
    return out
