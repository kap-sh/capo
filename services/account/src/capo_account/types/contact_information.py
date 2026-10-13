"""Generated from Smithy shape ``com.amazonaws.account#ContactInformation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account.types.address_line
    import capo_account.types.city
    import capo_account.types.company_name
    import capo_account.types.contact_information_phone_number
    import capo_account.types.country_code
    import capo_account.types.district_or_county
    import capo_account.types.full_name
    import capo_account.types.postal_code
    import capo_account.types.state_or_region
    import capo_account.types.website_url


class ContactInformation(TypedDict, closed=True):
    full_name: "capo_account.types.full_name.FullName"
    """<p>The full name of the primary contact address.</p>"""
    address_line1: "capo_account.types.address_line.AddressLine"
    """<p>The first line of the primary contact address.</p>"""
    address_line2: NotRequired["capo_account.types.address_line.AddressLine"]
    """<p>The second line of the primary contact address, if any.</p>"""
    address_line3: NotRequired["capo_account.types.address_line.AddressLine"]
    """<p>The third line of the primary contact address, if any.</p>"""
    city: "capo_account.types.city.City"
    """<p>The city of the primary contact address.</p>"""
    state_or_region: NotRequired["capo_account.types.state_or_region.StateOrRegion"]
    """<p>The state or region of the primary contact address. If the mailing address is within the United States (US), the value in this field can be either a two character state code (for example, <code>NJ</code>) or the full state name (for example, <code>New Jersey</code>). This field is required in the following countries: <code>US</code>, <code>CA</code>, <code>GB</code>, <code>DE</code>, <code>JP</code>, <code>IN</code>, and <code>BR</code>.</p>"""
    district_or_county: NotRequired[
        "capo_account.types.district_or_county.DistrictOrCounty"
    ]
    """<p>The district or county of the primary contact address, if any.</p>"""
    postal_code: "capo_account.types.postal_code.PostalCode"
    """<p>The postal code of the primary contact address.</p>"""
    country_code: "capo_account.types.country_code.CountryCode"
    """<p>The ISO-3166 two-letter country code for the primary contact address.</p>"""
    phone_number: "capo_account.types.contact_information_phone_number.ContactInformationPhoneNumber"
    """<p>The phone number of the primary contact information. The number will be validated and, in some countries, checked for activation.</p>"""
    company_name: NotRequired["capo_account.types.company_name.CompanyName"]
    """<p>The name of the company associated with the primary contact information, if any.</p>"""
    website_url: NotRequired["capo_account.types.website_url.WebsiteUrl"]
    """<p>The URL of the website associated with the primary contact information, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactInformation) -> dict:
    out: dict = {}
    out["FullName"] = value["full_name"]
    out["AddressLine1"] = value["address_line1"]
    if "address_line2" in value:
        out["AddressLine2"] = value["address_line2"]
    if "address_line3" in value:
        out["AddressLine3"] = value["address_line3"]
    out["City"] = value["city"]
    if "state_or_region" in value:
        out["StateOrRegion"] = value["state_or_region"]
    if "district_or_county" in value:
        out["DistrictOrCounty"] = value["district_or_county"]
    out["PostalCode"] = value["postal_code"]
    out["CountryCode"] = value["country_code"]
    out["PhoneNumber"] = value["phone_number"]
    if "company_name" in value:
        out["CompanyName"] = value["company_name"]
    if "website_url" in value:
        out["WebsiteUrl"] = value["website_url"]
    return out


def deserialize_json(data: dict) -> ContactInformation:
    out: ContactInformation = {}  # type: ignore[typeddict-item]
    if data.get("FullName") is not None:
        out["full_name"] = data["FullName"]
    else:
        raise DeserializationError("ContactInformation.full_name required")
    if data.get("AddressLine1") is not None:
        out["address_line1"] = data["AddressLine1"]
    else:
        raise DeserializationError("ContactInformation.address_line1 required")
    if data.get("AddressLine2") is not None:
        out["address_line2"] = data["AddressLine2"]
    if data.get("AddressLine3") is not None:
        out["address_line3"] = data["AddressLine3"]
    if data.get("City") is not None:
        out["city"] = data["City"]
    else:
        raise DeserializationError("ContactInformation.city required")
    if data.get("StateOrRegion") is not None:
        out["state_or_region"] = data["StateOrRegion"]
    if data.get("DistrictOrCounty") is not None:
        out["district_or_county"] = data["DistrictOrCounty"]
    if data.get("PostalCode") is not None:
        out["postal_code"] = data["PostalCode"]
    else:
        raise DeserializationError("ContactInformation.postal_code required")
    if data.get("CountryCode") is not None:
        out["country_code"] = data["CountryCode"]
    else:
        raise DeserializationError("ContactInformation.country_code required")
    if data.get("PhoneNumber") is not None:
        out["phone_number"] = data["PhoneNumber"]
    else:
        raise DeserializationError("ContactInformation.phone_number required")
    if data.get("CompanyName") is not None:
        out["company_name"] = data["CompanyName"]
    if data.get("WebsiteUrl") is not None:
        out["website_url"] = data["WebsiteUrl"]
    return out


def redact_sensitive(value: ContactInformation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "full_name" in value:
        out["full_name"] = "*** Sensitive Data Redacted ***"
    if "address_line1" in value:
        out["address_line1"] = "*** Sensitive Data Redacted ***"
    if "address_line2" in value:
        out["address_line2"] = "*** Sensitive Data Redacted ***"
    if "address_line3" in value:
        out["address_line3"] = "*** Sensitive Data Redacted ***"
    if "city" in value:
        out["city"] = "*** Sensitive Data Redacted ***"
    if "state_or_region" in value:
        out["state_or_region"] = "*** Sensitive Data Redacted ***"
    if "district_or_county" in value:
        out["district_or_county"] = "*** Sensitive Data Redacted ***"
    if "postal_code" in value:
        out["postal_code"] = "*** Sensitive Data Redacted ***"
    if "country_code" in value:
        out["country_code"] = "*** Sensitive Data Redacted ***"
    if "phone_number" in value:
        out["phone_number"] = "*** Sensitive Data Redacted ***"
    if "company_name" in value:
        out["company_name"] = "*** Sensitive Data Redacted ***"
    if "website_url" in value:
        out["website_url"] = "*** Sensitive Data Redacted ***"
    return out
