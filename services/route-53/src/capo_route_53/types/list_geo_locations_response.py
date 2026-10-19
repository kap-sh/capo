"""Generated from Smithy shape ``com.amazonaws.route53#ListGeoLocationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.geo_location_continent_code
    import capo_route_53.types.geo_location_country_code
    import capo_route_53.types.geo_location_details_list
    import capo_route_53.types.geo_location_subdivision_code
    import capo_route_53.types.page_truncated


class ListGeoLocationsResponse(TypedDict, closed=True):
    geo_location_details_list: (
        "capo_route_53.types.geo_location_details_list.GeoLocationDetailsList"
    )
    """<p>A complex type that contains one <code>GeoLocationDetails</code> element for each location that Amazon Route 53 supports for geolocation.</p>"""
    is_truncated: "capo_route_53.types.page_truncated.PageTruncated"
    """<p>A value that indicates whether more locations remain to be listed after the last location in this response. If so, the value of <code>IsTruncated</code> is <code>true</code>. To get more values, submit another request and include the values of <code>NextContinentCode</code>, <code>NextCountryCode</code>, and <code>NextSubdivisionCode</code> in the <code>startcontinentcode</code>, <code>startcountrycode</code>, and <code>startsubdivisioncode</code>, as applicable.</p>"""
    next_continent_code: NotRequired[
        "capo_route_53.types.geo_location_continent_code.GeoLocationContinentCode"
    ]
    """<p>If <code>IsTruncated</code> is <code>true</code>, you can make a follow-up request to display more locations. Enter the value of <code>NextContinentCode</code> in the <code>startcontinentcode</code> parameter in another <code>ListGeoLocations</code> request.</p>"""
    next_country_code: NotRequired[
        "capo_route_53.types.geo_location_country_code.GeoLocationCountryCode"
    ]
    """<p>If <code>IsTruncated</code> is <code>true</code>, you can make a follow-up request to display more locations. Enter the value of <code>NextCountryCode</code> in the <code>startcountrycode</code> parameter in another <code>ListGeoLocations</code> request.</p>"""
    next_subdivision_code: NotRequired[
        "capo_route_53.types.geo_location_subdivision_code.GeoLocationSubdivisionCode"
    ]
    """<p>If <code>IsTruncated</code> is <code>true</code>, you can make a follow-up request to display more locations. Enter the value of <code>NextSubdivisionCode</code> in the <code>startsubdivisioncode</code> parameter in another <code>ListGeoLocations</code> request.</p>"""
    max_items: "int"
    """<p>The value that you specified for <code>MaxItems</code> in the request.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListGeoLocationsResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.geo_location_details_list

    capo_route_53.types.geo_location_details_list.serialize_xml(
        value["geo_location_details_list"], el, "GeoLocationDetailsList"
    )
    SubElement(el, "IsTruncated").text = (
        "true" if value.get("is_truncated", False) else "false"
    )
    if "next_continent_code" in value:
        SubElement(el, "NextContinentCode").text = str(value["next_continent_code"])
    if "next_country_code" in value:
        SubElement(el, "NextCountryCode").text = str(value["next_country_code"])
    if "next_subdivision_code" in value:
        SubElement(el, "NextSubdivisionCode").text = str(value["next_subdivision_code"])
    SubElement(el, "MaxItems").text = str(value["max_items"])


def deserialize_xml(el: Element) -> ListGeoLocationsResponse:
    out: ListGeoLocationsResponse = {}  # type: ignore[typeddict-item]
    child_geo_location_details_list = el.find("GeoLocationDetailsList")
    if child_geo_location_details_list is not None:
        import capo_route_53.types.geo_location_details_list

        out["geo_location_details_list"] = (
            capo_route_53.types.geo_location_details_list.deserialize_xml(
                child_geo_location_details_list
            )
        )
    else:
        out["geo_location_details_list"] = []
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_next_continent_code = el.find("NextContinentCode")
    if child_next_continent_code is not None:
        out["next_continent_code"] = str(child_next_continent_code.text or "")
    child_next_country_code = el.find("NextCountryCode")
    if child_next_country_code is not None:
        out["next_country_code"] = str(child_next_country_code.text or "")
    child_next_subdivision_code = el.find("NextSubdivisionCode")
    if child_next_subdivision_code is not None:
        out["next_subdivision_code"] = str(child_next_subdivision_code.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    else:
        out["max_items"] = 0
    return out
