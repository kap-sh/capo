"""Generated from Smithy shape ``com.amazonaws.cloudfront#ManagedCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.certificate_transparency_logging_preference
    import capo_cloudfront.types.string
    import capo_cloudfront.types.validation_token_host


class ManagedCertificateRequest(TypedDict, closed=True):
    validation_token_host: (
        "capo_cloudfront.types.validation_token_host.ValidationTokenHost"
    )
    """<p>Specify how the HTTP validation token will be served when requesting the CloudFront managed ACM certificate.</p> <ul> <li> <p>For <code>cloudfront</code>, CloudFront will automatically serve the validation token. Choose this mode if you can point the domain's DNS to CloudFront immediately.</p> </li> <li> <p>For <code>self-hosted</code>, you serve the validation token from your existing infrastructure. Choose this mode when you need to maintain current traffic flow while your certificate is being issued. You can place the validation token at the well-known path on your existing web server, wait for ACM to validate and issue the certificate, and then update your DNS to point to CloudFront.</p> </li> </ul>"""
    primary_domain_name: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The primary domain name associated with the CloudFront managed ACM certificate.</p>"""
    certificate_transparency_logging_preference: NotRequired[
        "capo_cloudfront.types.certificate_transparency_logging_preference.CertificateTransparencyLoggingPreference"
    ]
    """<p>You can opt out of certificate transparency logging by specifying the <code>disabled</code> option. Opt in by specifying <code>enabled</code>. For more information, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency">Certificate Transparency Logging </a> in the <i>Certificate Manager User Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ManagedCertificateRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.validation_token_host

    capo_cloudfront.types.validation_token_host.serialize_xml(
        value["validation_token_host"], el, "ValidationTokenHost"
    )
    if "primary_domain_name" in value:
        SubElement(el, "PrimaryDomainName").text = str(value["primary_domain_name"])
    if "certificate_transparency_logging_preference" in value:
        import capo_cloudfront.types.certificate_transparency_logging_preference

        capo_cloudfront.types.certificate_transparency_logging_preference.serialize_xml(
            value["certificate_transparency_logging_preference"],
            el,
            "CertificateTransparencyLoggingPreference",
        )


def deserialize_xml(el: Element) -> ManagedCertificateRequest:
    out: ManagedCertificateRequest = {}  # type: ignore[typeddict-item]
    child_validation_token_host = el.find("ValidationTokenHost")
    if child_validation_token_host is not None:
        import capo_cloudfront.types.validation_token_host

        out["validation_token_host"] = (
            capo_cloudfront.types.validation_token_host.deserialize_xml(
                child_validation_token_host
            )
        )
    else:
        raise DeserializationError(
            "ManagedCertificateRequest.validation_token_host required"
        )
    child_primary_domain_name = el.find("PrimaryDomainName")
    if child_primary_domain_name is not None:
        out["primary_domain_name"] = str(child_primary_domain_name.text or "")
    child_certificate_transparency_logging_preference = el.find(
        "CertificateTransparencyLoggingPreference"
    )
    if child_certificate_transparency_logging_preference is not None:
        import capo_cloudfront.types.certificate_transparency_logging_preference

        out["certificate_transparency_logging_preference"] = (
            capo_cloudfront.types.certificate_transparency_logging_preference.deserialize_xml(
                child_certificate_transparency_logging_preference
            )
        )
    return out
