"""Generated from Smithy shape ``com.amazonaws.route53#GetGeoLocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.geo_location_continent_code
    import capo_route_53.types.geo_location_country_code
    import capo_route_53.types.geo_location_subdivision_code


class GetGeoLocationRequest(TypedDict, closed=True):
    continent_code: NotRequired[
        "capo_route_53.types.geo_location_continent_code.GeoLocationContinentCode"
    ]
    """<p>For geolocation resource record sets, a two-letter abbreviation that identifies a continent. Amazon Route 53 supports the following continent codes:</p> <ul> <li> <p> <b>AF</b>: Africa</p> </li> <li> <p> <b>AN</b>: Antarctica</p> </li> <li> <p> <b>AS</b>: Asia</p> </li> <li> <p> <b>EU</b>: Europe</p> </li> <li> <p> <b>OC</b>: Oceania</p> </li> <li> <p> <b>NA</b>: North America</p> </li> <li> <p> <b>SA</b>: South America</p> </li> </ul>"""
    country_code: NotRequired[
        "capo_route_53.types.geo_location_country_code.GeoLocationCountryCode"
    ]
    """<p>Amazon Route 53 uses the two-letter country codes that are specified in <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO standard 3166-1 alpha-2</a>.</p> <p>Route 53 also supports the country code <b>UA</b> for Ukraine.</p>"""
    subdivision_code: NotRequired[
        "capo_route_53.types.geo_location_subdivision_code.GeoLocationSubdivisionCode"
    ]
    """<p>The code for the subdivision, such as a particular state within the United States. For a list of US state abbreviations, see <a href="https://pe.usps.com/text/pub28/28apb.htm">Appendix B: Two–Letter State and Possession Abbreviations</a> on the United States Postal Service website. For a list of all supported subdivision codes, use the <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListGeoLocations.html">ListGeoLocations</a> API.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetGeoLocationRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetGeoLocationRequest:
    out: GetGeoLocationRequest = {}  # type: ignore[typeddict-item]
    return out
