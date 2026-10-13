"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#Contact``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.contact_email
    import capo_partnercentral_benefits.types.contact_first_name
    import capo_partnercentral_benefits.types.contact_last_name
    import capo_partnercentral_benefits.types.contact_phone


class Contact(TypedDict, closed=True):
    email: NotRequired["capo_partnercentral_benefits.types.contact_email.ContactEmail"]
    """<p>The email address of the contact person.</p>"""
    first_name: NotRequired[
        "capo_partnercentral_benefits.types.contact_first_name.ContactFirstName"
    ]
    """<p>The first name of the contact person.</p>"""
    last_name: NotRequired[
        "capo_partnercentral_benefits.types.contact_last_name.ContactLastName"
    ]
    """<p>The last name of the contact person.</p>"""
    business_title: NotRequired["str"]
    """<p>The business title or role of the contact person within the organization.</p>"""
    phone: NotRequired["capo_partnercentral_benefits.types.contact_phone.ContactPhone"]
    """<p>The phone number of the contact person.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Contact) -> dict:
    out: dict = {}
    if "email" in value:
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


def deserialize_aws_json_1_0(data: dict) -> Contact:
    out: Contact = {}  # type: ignore[typeddict-item]
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    if data.get("FirstName") is not None:
        out["first_name"] = data["FirstName"]
    if data.get("LastName") is not None:
        out["last_name"] = data["LastName"]
    if data.get("BusinessTitle") is not None:
        out["business_title"] = data["BusinessTitle"]
    if data.get("Phone") is not None:
        out["phone"] = data["Phone"]
    return out


def redact_sensitive(value: Contact) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    if "phone" in value:
        out["phone"] = "*** Sensitive Data Redacted ***"
    return out
