"""Generated from Smithy shape ``com.amazonaws.route53#GeoLocationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.geo_location_continent_code
    import capo_route_53.types.geo_location_continent_name
    import capo_route_53.types.geo_location_country_code
    import capo_route_53.types.geo_location_country_name
    import capo_route_53.types.geo_location_subdivision_code
    import capo_route_53.types.geo_location_subdivision_name


class GeoLocationDetails(TypedDict, closed=True):
    continent_code: NotRequired[
        "capo_route_53.types.geo_location_continent_code.GeoLocationContinentCode"
    ]
    """<p>The two-letter code for the continent.</p>"""
    continent_name: NotRequired[
        "capo_route_53.types.geo_location_continent_name.GeoLocationContinentName"
    ]
    """<p>The full name of the continent.</p>"""
    country_code: NotRequired[
        "capo_route_53.types.geo_location_country_code.GeoLocationCountryCode"
    ]
    """<p>The two-letter code for the country.</p>"""
    country_name: NotRequired[
        "capo_route_53.types.geo_location_country_name.GeoLocationCountryName"
    ]
    """<p>The name of the country.</p>"""
    subdivision_code: NotRequired[
        "capo_route_53.types.geo_location_subdivision_code.GeoLocationSubdivisionCode"
    ]
    """<p>The code for the subdivision, such as a particular state within the United States. For a list of US state abbreviations, see <a href="https://pe.usps.com/text/pub28/28apb.htm">Appendix B: Two–Letter State and Possession Abbreviations</a> on the United States Postal Service website. For a list of all supported subdivision codes, use the <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListGeoLocations.html">ListGeoLocations</a> API.</p>"""
    subdivision_name: NotRequired[
        "capo_route_53.types.geo_location_subdivision_name.GeoLocationSubdivisionName"
    ]
    """<p>The full name of the subdivision. Route 53 currently supports only states in the United States.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GeoLocationDetails, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "continent_code" in value:
        SubElement(el, "ContinentCode").text = str(value["continent_code"])
    if "continent_name" in value:
        SubElement(el, "ContinentName").text = str(value["continent_name"])
    if "country_code" in value:
        SubElement(el, "CountryCode").text = str(value["country_code"])
    if "country_name" in value:
        SubElement(el, "CountryName").text = str(value["country_name"])
    if "subdivision_code" in value:
        SubElement(el, "SubdivisionCode").text = str(value["subdivision_code"])
    if "subdivision_name" in value:
        SubElement(el, "SubdivisionName").text = str(value["subdivision_name"])


def deserialize_xml(el: Element) -> GeoLocationDetails:
    out: GeoLocationDetails = {}  # type: ignore[typeddict-item]
    child_continent_code = el.find("ContinentCode")
    if child_continent_code is not None:
        out["continent_code"] = str(child_continent_code.text or "")
    child_continent_name = el.find("ContinentName")
    if child_continent_name is not None:
        out["continent_name"] = str(child_continent_name.text or "")
    child_country_code = el.find("CountryCode")
    if child_country_code is not None:
        out["country_code"] = str(child_country_code.text or "")
    child_country_name = el.find("CountryName")
    if child_country_name is not None:
        out["country_name"] = str(child_country_name.text or "")
    child_subdivision_code = el.find("SubdivisionCode")
    if child_subdivision_code is not None:
        out["subdivision_code"] = str(child_subdivision_code.text or "")
    child_subdivision_name = el.find("SubdivisionName")
    if child_subdivision_name is not None:
        out["subdivision_name"] = str(child_subdivision_name.text or "")
    return out
