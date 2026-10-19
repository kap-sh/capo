"""Generated from Smithy shape ``com.amazonaws.cloudfront#DnsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.dns_configuration_status
    import capo_cloudfront.types.string


class DnsConfiguration(TypedDict, closed=True):
    domain: "capo_cloudfront.types.string.string"
    """<p>The domain name that you're verifying.</p>"""
    status: "capo_cloudfront.types.dns_configuration_status.DnsConfigurationStatus"
    """<p>The status of your domain name.</p> <ul> <li> <p> <code>valid-configuration</code>: The domain name is correctly configured and points to the correct routing endpoint of the connection group.</p> </li> <li> <p> <code>invalid-configuration</code>: There is either a missing DNS record or the DNS record exists but it's using an incorrect routing endpoint. Update the DNS record to point to the correct routing endpoint.</p> </li> <li> <p> <code>unknown-configuration</code>: CloudFront can't validate your DNS configuration. This status can appear if CloudFront can't verify the DNS record, or the DNS lookup request failed or timed out.</p> </li> </ul>"""
    reason: NotRequired["capo_cloudfront.types.string.string"]
    """<p>Explains the status of the DNS configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DnsConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Domain").text = str(value["domain"])
    import capo_cloudfront.types.dns_configuration_status

    capo_cloudfront.types.dns_configuration_status.serialize_xml(
        value["status"], el, "Status"
    )
    if "reason" in value:
        SubElement(el, "Reason").text = str(value["reason"])


def deserialize_xml(el: Element) -> DnsConfiguration:
    out: DnsConfiguration = {}  # type: ignore[typeddict-item]
    child_domain = el.find("Domain")
    if child_domain is not None:
        out["domain"] = str(child_domain.text or "")
    else:
        out["domain"] = ""
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudfront.types.dns_configuration_status

        out["status"] = capo_cloudfront.types.dns_configuration_status.deserialize_xml(
            child_status
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cloudfront.types.dns_configuration_status.DnsConfigurationStatus", ""
        )
    child_reason = el.find("Reason")
    if child_reason is not None:
        out["reason"] = str(child_reason.text or "")
    return out
