"""Generated from Smithy shape ``com.amazonaws.cloudfront#TrustStoreConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.string


class TrustStoreConfig(TypedDict, closed=True):
    trust_store_id: "capo_cloudfront.types.string.string"
    """<p>The trust store ID.</p>"""
    advertise_trust_store_ca_names: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>The configuration to use to advertise trust store CA names.</p>"""
    ignore_certificate_expiry: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>The configuration to use to ignore certificate expiration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TrustStoreConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "TrustStoreId").text = str(value["trust_store_id"])
    if "advertise_trust_store_ca_names" in value:
        SubElement(el, "AdvertiseTrustStoreCaNames").text = (
            "true" if value["advertise_trust_store_ca_names"] else "false"
        )
    if "ignore_certificate_expiry" in value:
        SubElement(el, "IgnoreCertificateExpiry").text = (
            "true" if value["ignore_certificate_expiry"] else "false"
        )


def deserialize_xml(el: Element) -> TrustStoreConfig:
    out: TrustStoreConfig = {}  # type: ignore[typeddict-item]
    child_trust_store_id = el.find("TrustStoreId")
    if child_trust_store_id is not None:
        out["trust_store_id"] = str(child_trust_store_id.text or "")
    else:
        out["trust_store_id"] = ""
    child_advertise_trust_store_ca_names = el.find("AdvertiseTrustStoreCaNames")
    if child_advertise_trust_store_ca_names is not None:
        out["advertise_trust_store_ca_names"] = (
            child_advertise_trust_store_ca_names.text or ""
        ).lower() == "true"
    child_ignore_certificate_expiry = el.find("IgnoreCertificateExpiry")
    if child_ignore_certificate_expiry is not None:
        out["ignore_certificate_expiry"] = (
            child_ignore_certificate_expiry.text or ""
        ).lower() == "true"
    return out
