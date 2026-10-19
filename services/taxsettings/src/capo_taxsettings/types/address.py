"""Generated from Smithy shape ``com.amazonaws.taxsettings#Address``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.address_line1
    import capo_taxsettings.types.address_line2
    import capo_taxsettings.types.address_line3
    import capo_taxsettings.types.city
    import capo_taxsettings.types.country_code
    import capo_taxsettings.types.district
    import capo_taxsettings.types.postal_code
    import capo_taxsettings.types.state


class Address(TypedDict, closed=True):
    address_line1: "capo_taxsettings.types.address_line1.AddressLine1"
    """<p>The first line of the address. </p>"""
    address_line2: NotRequired["capo_taxsettings.types.address_line2.AddressLine2"]
    """<p>The second line of the address, if applicable. </p>"""
    address_line3: NotRequired["capo_taxsettings.types.address_line3.AddressLine3"]
    """<p> The third line of the address, if applicable. Currently, the Tax Settings API accepts the <code>addressLine3</code> parameter only for Saudi Arabia. When you specify a TRN in Saudi Arabia, you must enter the <code>addressLine3</code> and specify the building number for the address. For example, you might enter <code>1234</code>.</p>"""
    district_or_county: NotRequired["capo_taxsettings.types.district.District"]
    """<p>The district or county the address is located. </p> <note> <p>For addresses in Brazil, this parameter uses the name of the neighborhood. When you set a TRN in Brazil, use <code>districtOrCounty</code> for the neighborhood name.</p> </note>"""
    city: "capo_taxsettings.types.city.City"
    """<p>The city that the address is in. </p>"""
    state_or_region: NotRequired["capo_taxsettings.types.state.State"]
    """<p>The state, region, or province that the address is located. This field is only required for Canada, India, United Arab Emirates, Romania, and Brazil (CPF). It is optional for all other countries.</p> <p>If this is required for tax settings, use the same name as shown on the <b>Tax Settings</b> page.</p>"""
    postal_code: "capo_taxsettings.types.postal_code.PostalCode"
    """<p> The postal code associated with the address. </p>"""
    country_code: "capo_taxsettings.types.country_code.CountryCode"
    """<p>The country code for the country that the address is in. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Address) -> dict:
    out: dict = {}
    out["addressLine1"] = value.get("address_line1", "Unknown")
    if "address_line2" in value:
        out["addressLine2"] = value["address_line2"]
    if "address_line3" in value:
        out["addressLine3"] = value["address_line3"]
    if "district_or_county" in value:
        out["districtOrCounty"] = value["district_or_county"]
    out["city"] = value.get("city", "Unknown")
    if "state_or_region" in value:
        out["stateOrRegion"] = value["state_or_region"]
    out["postalCode"] = value["postal_code"]
    out["countryCode"] = value["country_code"]
    return out


def deserialize_json(data: dict) -> Address:
    out: Address = {}  # type: ignore[typeddict-item]
    if data.get("addressLine1") is not None:
        out["address_line1"] = data["addressLine1"]
    else:
        out["address_line1"] = "Unknown"
    if data.get("addressLine2") is not None:
        out["address_line2"] = data["addressLine2"]
    if data.get("addressLine3") is not None:
        out["address_line3"] = data["addressLine3"]
    if data.get("districtOrCounty") is not None:
        out["district_or_county"] = data["districtOrCounty"]
    if data.get("city") is not None:
        out["city"] = data["city"]
    else:
        out["city"] = "Unknown"
    if data.get("stateOrRegion") is not None:
        out["state_or_region"] = data["stateOrRegion"]
    if data.get("postalCode") is not None:
        out["postal_code"] = data["postalCode"]
    else:
        out["postal_code"] = ""
    if data.get("countryCode") is not None:
        out["country_code"] = data["countryCode"]
    else:
        out["country_code"] = ""
    return out
