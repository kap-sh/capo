"""Generated from Smithy shape ``com.amazonaws.cloudfront#VerifyDnsConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class VerifyDnsConfigurationRequest(TypedDict, closed=True):
    domain: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The domain name that you're verifying.</p>"""
    identifier: "capo_cloudfront.types.string.string"
    """<p>The identifier of the distribution tenant. You can specify the ARN, ID, or name of the distribution tenant.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: VerifyDnsConfigurationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "domain" in value:
        SubElement(el, "Domain").text = str(value["domain"])
    SubElement(el, "Identifier").text = str(value["identifier"])


def deserialize_xml(el: Element) -> VerifyDnsConfigurationRequest:
    out: VerifyDnsConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    child_identifier = el.find("Identifier")
    if child_identifier is not None:
        out["identifier"] = str(child_identifier.text or "")
    else:
        out["identifier"] = ""
    return out
