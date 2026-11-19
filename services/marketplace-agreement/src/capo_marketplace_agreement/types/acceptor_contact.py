"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AcceptorContact``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.contact_company_name
    import capo_marketplace_agreement.types.country_code
    import capo_marketplace_agreement.types.email_address
    import capo_marketplace_agreement.types.person_name


class AcceptorContact(TypedDict, closed=True):
    first_name: "capo_marketplace_agreement.types.person_name.PersonName"
    """<p>The first name of the acceptor contact.</p>"""
    last_name: "capo_marketplace_agreement.types.person_name.PersonName"
    """<p>The last name of the acceptor contact.</p>"""
    email_address: "capo_marketplace_agreement.types.email_address.EmailAddress"
    """<p>The email address of the acceptor contact.</p>"""
    company_name: (
        "capo_marketplace_agreement.types.contact_company_name.ContactCompanyName"
    )
    """<p>The name of the company that the acceptor contact represents.</p>"""
    country_code: "capo_marketplace_agreement.types.country_code.CountryCode"
    """<p>The ISO-3166 two-letter country code for the acceptor contact.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptorContact) -> dict:
    out: dict = {}
    out["firstName"] = value["first_name"]
    out["lastName"] = value["last_name"]
    out["emailAddress"] = value["email_address"]
    out["companyName"] = value["company_name"]
    out["countryCode"] = value["country_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptorContact:
    out: AcceptorContact = {}  # type: ignore[typeddict-item]
    if data.get("firstName") is not None:
        out["first_name"] = data["firstName"]
    else:
        out["first_name"] = ""
    if data.get("lastName") is not None:
        out["last_name"] = data["lastName"]
    else:
        out["last_name"] = ""
    if data.get("emailAddress") is not None:
        out["email_address"] = data["emailAddress"]
    else:
        out["email_address"] = ""
    if data.get("companyName") is not None:
        out["company_name"] = data["companyName"]
    else:
        out["company_name"] = ""
    if data.get("countryCode") is not None:
        out["country_code"] = data["countryCode"]
    else:
        out["country_code"] = ""
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AcceptorContact) -> dict:
    out: dict = {}
    out["firstName"] = value["first_name"]
    out["lastName"] = value["last_name"]
    out["emailAddress"] = value["email_address"]
    out["companyName"] = value["company_name"]
    out["countryCode"] = value["country_code"]
    return out


def deserialize_cbor(data: dict) -> AcceptorContact:
    out: AcceptorContact = {}  # type: ignore[typeddict-item]
    if data.get("firstName") is not None:
        out["first_name"] = data["firstName"]
    else:
        out["first_name"] = ""
    if data.get("lastName") is not None:
        out["last_name"] = data["lastName"]
    else:
        out["last_name"] = ""
    if data.get("emailAddress") is not None:
        out["email_address"] = data["emailAddress"]
    else:
        out["email_address"] = ""
    if data.get("companyName") is not None:
        out["company_name"] = data["companyName"]
    else:
        out["company_name"] = ""
    if data.get("countryCode") is not None:
        out["country_code"] = data["countryCode"]
    else:
        out["country_code"] = ""
    return out
