"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#AllianceLeadContact``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.email
    import capo_partnercentral_account.types.sensitive_unicode_string


class AllianceLeadContact(TypedDict, closed=True):
    first_name: "capo_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString"
    """<p>The first name of the alliance lead contact person.</p>"""
    last_name: "capo_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString"
    """<p>The last name of the alliance lead contact person.</p>"""
    email: "capo_partnercentral_account.types.email.Email"
    """<p>The email address of the alliance lead contact person.</p>"""
    business_title: "capo_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString"
    """<p>The business title or role of the alliance lead contact person.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AllianceLeadContact) -> dict:
    out: dict = {}
    out["FirstName"] = value["first_name"]
    out["LastName"] = value["last_name"]
    out["Email"] = value["email"]
    out["BusinessTitle"] = value["business_title"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AllianceLeadContact:
    out: AllianceLeadContact = {}  # type: ignore[typeddict-item]
    if data.get("FirstName") is not None:
        out["first_name"] = data["FirstName"]
    else:
        raise DeserializationError("AllianceLeadContact.first_name required")
    if data.get("LastName") is not None:
        out["last_name"] = data["LastName"]
    else:
        raise DeserializationError("AllianceLeadContact.last_name required")
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    else:
        raise DeserializationError("AllianceLeadContact.email required")
    if data.get("BusinessTitle") is not None:
        out["business_title"] = data["BusinessTitle"]
    else:
        raise DeserializationError("AllianceLeadContact.business_title required")
    return out


def redact_sensitive(value: AllianceLeadContact) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    if "business_title" in value:
        out["business_title"] = "*** Sensitive Data Redacted ***"
    return out
