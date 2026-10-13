"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LeadContact``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.lead_email
    import capo_partnercentral_selling.types.lead_job_title
    import capo_partnercentral_selling.types.lead_phone_number
    import capo_partnercentral_selling.types.name


class LeadContact(TypedDict, closed=True):
    business_title: "capo_partnercentral_selling.types.lead_job_title.LeadJobTitle"
    """<p>The lead contact's business title or job role associated with the engagement.</p>"""
    email: "capo_partnercentral_selling.types.lead_email.LeadEmail"
    """<p>The lead contact's email address associated with the engagement.</p>"""
    first_name: "capo_partnercentral_selling.types.name.Name"
    """<p>The lead contact's first name associated with the engagement.</p>"""
    last_name: "capo_partnercentral_selling.types.name.Name"
    """<p>The lead contact's last name associated with the engagement.</p>"""
    phone: NotRequired[
        "capo_partnercentral_selling.types.lead_phone_number.LeadPhoneNumber"
    ]
    """<p>The lead contact's phone number associated with the engagement.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LeadContact) -> dict:
    out: dict = {}
    out["BusinessTitle"] = value["business_title"]
    out["Email"] = value["email"]
    out["FirstName"] = value["first_name"]
    out["LastName"] = value["last_name"]
    if "phone" in value:
        out["Phone"] = value["phone"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LeadContact:
    out: LeadContact = {}  # type: ignore[typeddict-item]
    if data.get("BusinessTitle") is not None:
        out["business_title"] = data["BusinessTitle"]
    else:
        raise DeserializationError("LeadContact.business_title required")
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    else:
        raise DeserializationError("LeadContact.email required")
    if data.get("FirstName") is not None:
        out["first_name"] = data["FirstName"]
    else:
        raise DeserializationError("LeadContact.first_name required")
    if data.get("LastName") is not None:
        out["last_name"] = data["LastName"]
    else:
        raise DeserializationError("LeadContact.last_name required")
    if data.get("Phone") is not None:
        out["phone"] = data["Phone"]
    return out


def redact_sensitive(value: LeadContact) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "business_title" in value:
        out["business_title"] = "*** Sensitive Data Redacted ***"
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    if "phone" in value:
        out["phone"] = "*** Sensitive Data Redacted ***"
    return out
