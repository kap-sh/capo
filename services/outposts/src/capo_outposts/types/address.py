"""Generated from Smithy shape ``com.amazonaws.outposts#Address``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.address_line1
    import capo_outposts.types.address_line2
    import capo_outposts.types.address_line3
    import capo_outposts.types.city
    import capo_outposts.types.contact_name
    import capo_outposts.types.contact_phone_number
    import capo_outposts.types.country_code
    import capo_outposts.types.district_or_county
    import capo_outposts.types.municipality
    import capo_outposts.types.postal_code
    import capo_outposts.types.state_or_region


class Address(TypedDict, closed=True):
    contact_name: "capo_outposts.types.contact_name.ContactName"
    """<p>The name of the contact.</p>"""
    contact_phone_number: "capo_outposts.types.contact_phone_number.ContactPhoneNumber"
    """<p>The phone number of the contact, including the country code (for example, <code>+12065550100</code>).</p>"""
    address_line1: "capo_outposts.types.address_line1.AddressLine1"
    """<p>The first line of the address.</p>"""
    address_line2: NotRequired["capo_outposts.types.address_line2.AddressLine2"]
    """<p>The second line of the address.</p>"""
    address_line3: NotRequired["capo_outposts.types.address_line3.AddressLine3"]
    """<p>The third line of the address.</p>"""
    city: "capo_outposts.types.city.City"
    """<p>The city for the address.</p>"""
    state_or_region: "capo_outposts.types.state_or_region.StateOrRegion"
    """<p>The state for the address.</p>"""
    district_or_county: NotRequired[
        "capo_outposts.types.district_or_county.DistrictOrCounty"
    ]
    """<p>The district or county for the address.</p>"""
    postal_code: "capo_outposts.types.postal_code.PostalCode"
    """<p>The postal code for the address.</p>"""
    country_code: "capo_outposts.types.country_code.CountryCode"
    """<p>The ISO-3166 two-letter country code for the address.</p>"""
    municipality: NotRequired["capo_outposts.types.municipality.Municipality"]
    """<p>The municipality for the address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Address) -> dict:
    out: dict = {}
    out["ContactName"] = value["contact_name"]
    out["ContactPhoneNumber"] = value["contact_phone_number"]
    out["AddressLine1"] = value["address_line1"]
    if "address_line2" in value:
        out["AddressLine2"] = value["address_line2"]
    if "address_line3" in value:
        out["AddressLine3"] = value["address_line3"]
    out["City"] = value["city"]
    out["StateOrRegion"] = value["state_or_region"]
    if "district_or_county" in value:
        out["DistrictOrCounty"] = value["district_or_county"]
    out["PostalCode"] = value["postal_code"]
    out["CountryCode"] = value["country_code"]
    if "municipality" in value:
        out["Municipality"] = value["municipality"]
    return out


def deserialize_json(data: dict) -> Address:
    out: Address = {}  # type: ignore[typeddict-item]
    if data.get("ContactName") is not None:
        out["contact_name"] = data["ContactName"]
    else:
        out["contact_name"] = ""
    if data.get("ContactPhoneNumber") is not None:
        out["contact_phone_number"] = data["ContactPhoneNumber"]
    else:
        out["contact_phone_number"] = ""
    if data.get("AddressLine1") is not None:
        out["address_line1"] = data["AddressLine1"]
    else:
        out["address_line1"] = ""
    if data.get("AddressLine2") is not None:
        out["address_line2"] = data["AddressLine2"]
    if data.get("AddressLine3") is not None:
        out["address_line3"] = data["AddressLine3"]
    if data.get("City") is not None:
        out["city"] = data["City"]
    else:
        out["city"] = ""
    if data.get("StateOrRegion") is not None:
        out["state_or_region"] = data["StateOrRegion"]
    else:
        out["state_or_region"] = ""
    if data.get("DistrictOrCounty") is not None:
        out["district_or_county"] = data["DistrictOrCounty"]
    if data.get("PostalCode") is not None:
        out["postal_code"] = data["PostalCode"]
    else:
        out["postal_code"] = ""
    if data.get("CountryCode") is not None:
        out["country_code"] = data["CountryCode"]
    else:
        out["country_code"] = ""
    if data.get("Municipality") is not None:
        out["municipality"] = data["Municipality"]
    return out
