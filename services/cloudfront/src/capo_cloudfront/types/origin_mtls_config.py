"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginMtlsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class OriginMtlsConfig(TypedDict, closed=True):
    client_certificate_arn: "capo_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the client certificate stored in Amazon Web Services Certificate Manager (ACM) that CloudFront uses to authenticate with your origin using Mutual TLS.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OriginMtlsConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "ClientCertificateArn").text = str(value["client_certificate_arn"])


def deserialize_xml(el: Element) -> OriginMtlsConfig:
    out: OriginMtlsConfig = {}  # type: ignore[typeddict-item]
    child_client_certificate_arn = el.find("ClientCertificateArn")
    if child_client_certificate_arn is not None:
        out["client_certificate_arn"] = str(child_client_certificate_arn.text or "")
    else:
        out["client_certificate_arn"] = ""
    return out
