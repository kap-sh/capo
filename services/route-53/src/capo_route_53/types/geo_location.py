"""Generated from Smithy shape ``com.amazonaws.route53#GeoLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.geo_location_continent_code
    import capo_route_53.types.geo_location_country_code
    import capo_route_53.types.geo_location_subdivision_code


class GeoLocation(TypedDict, closed=True):
    continent_code: NotRequired[
        "capo_route_53.types.geo_location_continent_code.GeoLocationContinentCode"
    ]
    """<p>The two-letter code for the continent.</p> <p>Amazon Route 53 supports the following continent codes:</p> <ul> <li> <p> <b>AF</b>: Africa</p> </li> <li> <p> <b>AN</b>: Antarctica</p> </li> <li> <p> <b>AS</b>: Asia</p> </li> <li> <p> <b>EU</b>: Europe</p> </li> <li> <p> <b>OC</b>: Oceania</p> </li> <li> <p> <b>NA</b>: North America</p> </li> <li> <p> <b>SA</b>: South America</p> </li> </ul> <p>Constraint: Specifying <code>ContinentCode</code> with either <code>CountryCode</code> or <code>SubdivisionCode</code> returns an <code>InvalidInput</code> error.</p>"""
    country_code: NotRequired[
        "capo_route_53.types.geo_location_country_code.GeoLocationCountryCode"
    ]
    """<p>For geolocation resource record sets, the two-letter code for a country.</p> <p>Amazon Route 53 uses the two-letter country codes that are specified in <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO standard 3166-1 alpha-2</a>.</p> <p>Route 53 also supports the country code <b>UA</b> for Ukraine.</p>"""
    subdivision_code: NotRequired[
        "capo_route_53.types.geo_location_subdivision_code.GeoLocationSubdivisionCode"
    ]
    """<p>For geolocation resource record sets, the two-letter code for a state of the United States. Route 53 doesn't support any other values for <code>SubdivisionCode</code>. For a list of state abbreviations, see <a href="https://pe.usps.com/text/pub28/28apb.htm">Appendix B: Two–Letter State and Possession Abbreviations</a> on the United States Postal Service website. </p> <p>If you specify <code>subdivisioncode</code>, you must also specify <code>US</code> for <code>CountryCode</code>. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: GeoLocation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "continent_code" in value:
        SubElement(el, "ContinentCode").text = str(value["continent_code"])
    if "country_code" in value:
        SubElement(el, "CountryCode").text = str(value["country_code"])
    if "subdivision_code" in value:
        SubElement(el, "SubdivisionCode").text = str(value["subdivision_code"])


def deserialize_xml(el: Element) -> GeoLocation:
    out: GeoLocation = {}  # type: ignore[typeddict-item]
    child_continent_code = el.find("ContinentCode")
    if child_continent_code is not None:
        out["continent_code"] = str(child_continent_code.text or "")
    child_country_code = el.find("CountryCode")
    if child_country_code is not None:
        out["country_code"] = str(child_country_code.text or "")
    child_subdivision_code = el.find("SubdivisionCode")
    if child_subdivision_code is not None:
        out["subdivision_code"] = str(child_subdivision_code.text or "")
    return out
