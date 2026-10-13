"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AssigneeContact``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.email
    import capo_partnercentral_selling.types.job_title
    import capo_partnercentral_selling.types.name
    import capo_partnercentral_selling.types.phone_number


class AssigneeContact(TypedDict, closed=True):
    email: "capo_partnercentral_selling.types.email.Email"
    """<p>Provides the email address of the assignee. This email is used for communications and notifications related to the opportunity.</p>"""
    first_name: "capo_partnercentral_selling.types.name.Name"
    """<p>Specifies the first name of the assignee managing the opportunity. The system automatically retrieves this value from the user profile by referencing the associated email address.</p>"""
    last_name: "capo_partnercentral_selling.types.name.Name"
    """<p>Specifies the last name of the assignee managing the opportunity. The system automatically retrieves this value from the user profile by referencing the associated email address.</p>"""
    phone: NotRequired["capo_partnercentral_selling.types.phone_number.PhoneNumber"]
    """<p>Specifies the contact phone number of the assignee responsible for the opportunity or engagement. This field enables direct communication for time-sensitive matters and facilitates coordination between AWS and partner teams.</p>"""
    business_title: "capo_partnercentral_selling.types.job_title.JobTitle"
    """<p>Specifies the business title of the assignee managing the opportunity. This helps clarify the individual's role and responsibilities within the organization. Use the value <code>PartnerAccountManager</code> to update details of the opportunity owner.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssigneeContact) -> dict:
    out: dict = {}
    out["Email"] = value["email"]
    out["FirstName"] = value["first_name"]
    out["LastName"] = value["last_name"]
    if "phone" in value:
        out["Phone"] = value["phone"]
    out["BusinessTitle"] = value["business_title"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssigneeContact:
    out: AssigneeContact = {}  # type: ignore[typeddict-item]
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    else:
        raise DeserializationError("AssigneeContact.email required")
    if data.get("FirstName") is not None:
        out["first_name"] = data["FirstName"]
    else:
        raise DeserializationError("AssigneeContact.first_name required")
    if data.get("LastName") is not None:
        out["last_name"] = data["LastName"]
    else:
        raise DeserializationError("AssigneeContact.last_name required")
    if data.get("Phone") is not None:
        out["phone"] = data["Phone"]
    if data.get("BusinessTitle") is not None:
        out["business_title"] = data["BusinessTitle"]
    else:
        raise DeserializationError("AssigneeContact.business_title required")
    return out


def redact_sensitive(value: AssigneeContact) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    if "phone" in value:
        out["phone"] = "*** Sensitive Data Redacted ***"
    if "business_title" in value:
        out["business_title"] = "*** Sensitive Data Redacted ***"
    return out
