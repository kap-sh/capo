"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyStrictTransportSecurity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.integer


class ResponseHeadersPolicyStrictTransportSecurity(TypedDict, closed=True):
    override: "capo_cloudfront.types.boolean.boolean"
    """<p>A Boolean that determines whether CloudFront overrides the <code>Strict-Transport-Security</code> HTTP response header received from the origin with the one specified in this response headers policy.</p>"""
    include_subdomains: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>A Boolean that determines whether CloudFront includes the <code>includeSubDomains</code> directive in the <code>Strict-Transport-Security</code> HTTP response header.</p>"""
    preload: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>A Boolean that determines whether CloudFront includes the <code>preload</code> directive in the <code>Strict-Transport-Security</code> HTTP response header.</p>"""
    access_control_max_age_sec: "capo_cloudfront.types.integer.integer"
    """<p>A number that CloudFront uses as the value for the <code>max-age</code> directive in the <code>Strict-Transport-Security</code> HTTP response header.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyStrictTransportSecurity, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Override").text = "true" if value["override"] else "false"
    if "include_subdomains" in value:
        SubElement(el, "IncludeSubdomains").text = (
            "true" if value["include_subdomains"] else "false"
        )
    if "preload" in value:
        SubElement(el, "Preload").text = "true" if value["preload"] else "false"
    SubElement(el, "AccessControlMaxAgeSec").text = str(
        value["access_control_max_age_sec"]
    )


def deserialize_xml(el: Element) -> ResponseHeadersPolicyStrictTransportSecurity:
    out: ResponseHeadersPolicyStrictTransportSecurity = {}  # type: ignore[typeddict-item]
    child_override = el.find("Override")
    if child_override is not None:
        out["override"] = (child_override.text or "").lower() == "true"
    else:
        out["override"] = False
    child_include_subdomains = el.find("IncludeSubdomains")
    if child_include_subdomains is not None:
        out["include_subdomains"] = (
            child_include_subdomains.text or ""
        ).lower() == "true"
    child_preload = el.find("Preload")
    if child_preload is not None:
        out["preload"] = (child_preload.text or "").lower() == "true"
    child_access_control_max_age_sec = el.find("AccessControlMaxAgeSec")
    if child_access_control_max_age_sec is not None:
        out["access_control_max_age_sec"] = int(
            child_access_control_max_age_sec.text or ""
        )
    else:
        out["access_control_max_age_sec"] = 0
    return out
