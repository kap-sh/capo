"""Generated from Smithy shape ``com.amazonaws.cloudfront#GeoRestrictionCustomization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.geo_restriction_type
    import capo_cloudfront.types.location_list


class GeoRestrictionCustomization(TypedDict, closed=True):
    restriction_type: "capo_cloudfront.types.geo_restriction_type.GeoRestrictionType"
    """<p>The method that you want to use to restrict distribution of your content by country:</p> <ul> <li> <p> <code>none</code>: No geographic restriction is enabled, meaning access to content is not restricted by client geo location.</p> </li> <li> <p> <code>blacklist</code>: The <code>Location</code> elements specify the countries in which you don't want CloudFront to distribute your content.</p> </li> <li> <p> <code>whitelist</code>: The <code>Location</code> elements specify the countries in which you want CloudFront to distribute your content.</p> </li> </ul>"""
    locations: NotRequired["capo_cloudfront.types.location_list.LocationList"]
    """<p>The locations for geographic restrictions.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GeoRestrictionCustomization, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.geo_restriction_type

    capo_cloudfront.types.geo_restriction_type.serialize_xml(
        value["restriction_type"], el, "RestrictionType"
    )
    if "locations" in value:
        import capo_cloudfront.types.location_list

        capo_cloudfront.types.location_list.serialize_xml(
            value["locations"], el, "Locations"
        )


def deserialize_xml(el: Element) -> GeoRestrictionCustomization:
    out: GeoRestrictionCustomization = {}  # type: ignore[typeddict-item]
    child_restriction_type = el.find("RestrictionType")
    if child_restriction_type is not None:
        import capo_cloudfront.types.geo_restriction_type

        out["restriction_type"] = (
            capo_cloudfront.types.geo_restriction_type.deserialize_xml(
                child_restriction_type
            )
        )
    else:
        import typing

        out["restriction_type"] = typing.cast(
            "capo_cloudfront.types.geo_restriction_type.GeoRestrictionType", ""
        )
    child_locations = el.find("Locations")
    if child_locations is not None:
        import capo_cloudfront.types.location_list

        out["locations"] = capo_cloudfront.types.location_list.deserialize_xml(
            child_locations
        )
    return out
