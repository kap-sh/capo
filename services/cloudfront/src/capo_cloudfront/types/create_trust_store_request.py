"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateTrustStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.ca_certificates_bundle_source
    import capo_cloudfront.types.string
    import capo_cloudfront.types.tags


class CreateTrustStoreRequest(TypedDict, closed=True):
    name: "capo_cloudfront.types.string.string"
    """<p>A name for the trust store.</p>"""
    ca_certificates_bundle_source: (
        "capo_cloudfront.types.ca_certificates_bundle_source.CaCertificatesBundleSource"
    )
    """<p>The CA certificates bundle source for the trust store.</p>"""
    use_client_certificate_ocsp_endpoint: NotRequired[
        "capo_cloudfront.types.boolean.boolean"
    ]
    """<p>A Boolean that determines whether to use the CA certificate's OCSP endpoint to check certificate revocation status.</p>"""
    tags: NotRequired["capo_cloudfront.types.tags.Tags"]


# --- restXml ser/de ---
def serialize_xml(value: CreateTrustStoreRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    import capo_cloudfront.types.ca_certificates_bundle_source

    capo_cloudfront.types.ca_certificates_bundle_source.serialize_xml(
        value["ca_certificates_bundle_source"], el, "CaCertificatesBundleSource"
    )
    if "use_client_certificate_ocsp_endpoint" in value:
        SubElement(el, "UseClientCertificateOCSPEndpoint").text = (
            "true" if value["use_client_certificate_ocsp_endpoint"] else "false"
        )
    if "tags" in value:
        import capo_cloudfront.types.tags

        capo_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> CreateTrustStoreRequest:
    out: CreateTrustStoreRequest = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_ca_certificates_bundle_source = el.find("CaCertificatesBundleSource")
    if child_ca_certificates_bundle_source is not None:
        import capo_cloudfront.types.ca_certificates_bundle_source

        out["ca_certificates_bundle_source"] = (
            capo_cloudfront.types.ca_certificates_bundle_source.deserialize_xml(
                child_ca_certificates_bundle_source
            )
        )
    else:
        import capo_cloudfront.types._unknown

        out["ca_certificates_bundle_source"] = (
            capo_cloudfront.types._unknown.UnknownUnionMember("")
        )
    child_use_client_certificate_ocsp_endpoint = el.find(
        "UseClientCertificateOCSPEndpoint"
    )
    if child_use_client_certificate_ocsp_endpoint is not None:
        out["use_client_certificate_ocsp_endpoint"] = (
            child_use_client_certificate_ocsp_endpoint.text or ""
        ).lower() == "true"
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudfront.types.tags

        out["tags"] = capo_cloudfront.types.tags.deserialize_xml(child_tags)
    return out
