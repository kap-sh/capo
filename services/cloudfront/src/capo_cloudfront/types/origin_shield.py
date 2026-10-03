"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginShield``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.origin_shield_region


class OriginShield(TypedDict, closed=True):
    enabled: "capo_cloudfront.types.boolean.boolean"
    """<p>A flag that specifies whether Origin Shield is enabled.</p> <p>When it's enabled, CloudFront routes all requests through Origin Shield, which can help protect your origin. When it's disabled, CloudFront might send requests directly to your origin from multiple edge locations or regional edge caches.</p>"""
    origin_shield_region: NotRequired[
        "capo_cloudfront.types.origin_shield_region.OriginShieldRegion"
    ]
    """<p>The Amazon Web Services Region for Origin Shield.</p> <p>Specify the Amazon Web Services Region that has the lowest latency to your origin. To specify a region, use the region code, not the region name. For example, specify the US East (Ohio) region as <code>us-east-2</code>.</p> <p>When you enable CloudFront Origin Shield, you must specify the Amazon Web Services Region for Origin Shield. For the list of Amazon Web Services Regions that you can specify, and for help choosing the best Region for your origin, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html#choose-origin-shield-region">Choosing the Amazon Web Services Region for Origin Shield</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OriginShield, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"
    if "origin_shield_region" in value:
        SubElement(el, "OriginShieldRegion").text = str(value["origin_shield_region"])


def deserialize_xml(el: Element) -> OriginShield:
    out: OriginShield = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        raise DeserializationError("OriginShield.enabled required")
    child_origin_shield_region = el.find("OriginShieldRegion")
    if child_origin_shield_region is not None:
        out["origin_shield_region"] = str(child_origin_shield_region.text or "")
    return out
