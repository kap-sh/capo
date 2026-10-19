"""Generated from Smithy shape ``com.amazonaws.connect#EmailAddressInfo``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.email_address
    import capo_connect.types.email_address_display_name


class EmailAddressInfo(TypedDict, closed=True):
    email_address: "capo_connect.types.email_address.EmailAddress"
    """<p>The email address, including the domain.</p>"""
    display_name: NotRequired[
        "capo_connect.types.email_address_display_name.EmailAddressDisplayName"
    ]
    """<p>The display name of email address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressInfo) -> dict:
    out: dict = {}
    out["EmailAddress"] = value["email_address"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> EmailAddressInfo:
    out: EmailAddressInfo = {}  # type: ignore[typeddict-item]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    else:
        out["email_address"] = ""
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    return out


def redact_sensitive(value: EmailAddressInfo) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    return out
