"""Generated from Smithy shape ``com.amazonaws.cloudfront#GeoRestriction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.geo_restriction_type
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.location_list


class GeoRestriction(TypedDict, closed=True):
    restriction_type: "capo_cloudfront.types.geo_restriction_type.GeoRestrictionType"
    """<p>The method that you want to use to restrict distribution of your content by country:</p> <ul> <li> <p> <code>none</code>: No geo restriction is enabled, meaning access to content is not restricted by client geo location.</p> </li> <li> <p> <code>blacklist</code>: The <code>Location</code> elements specify the countries in which you don't want CloudFront to distribute your content.</p> </li> <li> <p> <code>whitelist</code>: The <code>Location</code> elements specify the countries in which you want CloudFront to distribute your content.</p> </li> </ul>"""
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>When geo restriction is <code>enabled</code>, this is the number of countries in your <code>whitelist</code> or <code>blacklist</code>. Otherwise, when it is not enabled, <code>Quantity</code> is <code>0</code>, and you can omit <code>Items</code>.</p>"""
    items: NotRequired["capo_cloudfront.types.location_list.LocationList"]
    """<p>A complex type that contains a <code>Location</code> element for each country in which you want CloudFront either to distribute your content (<code>whitelist</code>) or not distribute your content (<code>blacklist</code>).</p> <p>The <code>Location</code> element is a two-letter, uppercase country code for a country that you want to include in your <code>blacklist</code> or <code>whitelist</code>. Include one <code>Location</code> element for each country.</p> <p>CloudFront and <code>MaxMind</code> both use <code>ISO 3166</code> country codes. For the current list of countries and the corresponding codes, see <code>ISO 3166-1-alpha-2</code> code on the <i>International Organization for Standardization</i> website. You can also refer to the country list on the CloudFront console, which includes both country names and codes.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GeoRestriction, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.geo_restriction_type

    capo_cloudfront.types.geo_restriction_type.serialize_xml(
        value["restriction_type"], el, "RestrictionType"
    )
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.location_list

        capo_cloudfront.types.location_list.serialize_xml(value["items"], el, "Items")


def deserialize_xml(el: Element) -> GeoRestriction:
    out: GeoRestriction = {}  # type: ignore[typeddict-item]
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
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.location_list

        out["items"] = capo_cloudfront.types.location_list.deserialize_xml(child_items)
    return out
