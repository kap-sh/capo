"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SenderContact``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.job_title
    import capo_partnercentral_selling.types.name
    import capo_partnercentral_selling.types.phone_number
    import capo_partnercentral_selling.types.sender_contact_email


class SenderContact(TypedDict, closed=True):
    email: "capo_partnercentral_selling.types.sender_contact_email.SenderContactEmail"
    """<p>The sender-provided contact's email address associated with the <code>EngagementInvitation</code>.</p>"""
    first_name: NotRequired["capo_partnercentral_selling.types.name.Name"]
    """<p>The sender-provided contact's last name associated with the <code>EngagementInvitation</code>.</p>"""
    last_name: NotRequired["capo_partnercentral_selling.types.name.Name"]
    """<p>The sender-provided contact's first name associated with the <code>EngagementInvitation</code>.</p>"""
    business_title: NotRequired["capo_partnercentral_selling.types.job_title.JobTitle"]
    """<p>The sender-provided contact's title (job title or role) associated with the <code>EngagementInvitation</code>.</p>"""
    phone: NotRequired["capo_partnercentral_selling.types.phone_number.PhoneNumber"]
    """<p>The sender-provided contact's phone number associated with the <code>EngagementInvitation</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SenderContact) -> dict:
    out: dict = {}
    out["Email"] = value["email"]
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    if "business_title" in value:
        out["BusinessTitle"] = value["business_title"]
    if "phone" in value:
        out["Phone"] = value["phone"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SenderContact:
    out: SenderContact = {}  # type: ignore[typeddict-item]
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    else:
        raise DeserializationError("SenderContact.email required")
    if data.get("FirstName") is not None:
        out["first_name"] = data["FirstName"]
    if data.get("LastName") is not None:
        out["last_name"] = data["LastName"]
    if data.get("BusinessTitle") is not None:
        out["business_title"] = data["BusinessTitle"]
    if data.get("Phone") is not None:
        out["phone"] = data["Phone"]
    return out


def redact_sensitive(value: SenderContact) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    if "business_title" in value:
        out["business_title"] = "*** Sensitive Data Redacted ***"
    if "phone" in value:
        out["phone"] = "*** Sensitive Data Redacted ***"
    return out
