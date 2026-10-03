"""Generated from Smithy shape ``com.amazonaws.cloudfront#S3Origin``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class S3Origin(TypedDict, closed=True):
    domain_name: "capo_cloudfront.types.string.string"
    """<p>The DNS name of the Amazon S3 origin.</p>"""
    origin_access_identity: "capo_cloudfront.types.string.string"
    """<p>The CloudFront origin access identity to associate with the distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.</p> <p>If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty <code>OriginAccessIdentity</code> element.</p> <p>To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty <code>OriginAccessIdentity</code> element.</p> <p>To replace the origin access identity, update the distribution configuration and specify the new origin access identity.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html">Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content</a> in the <i> Amazon CloudFront Developer Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3Origin, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "DomainName").text = str(value["domain_name"])
    SubElement(el, "OriginAccessIdentity").text = str(value["origin_access_identity"])


def deserialize_xml(el: Element) -> S3Origin:
    out: S3Origin = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError("S3Origin.domain_name required")
    child_origin_access_identity = el.find("OriginAccessIdentity")
    if child_origin_access_identity is not None:
        out["origin_access_identity"] = str(child_origin_access_identity.text or "")
    else:
        raise DeserializationError("S3Origin.origin_access_identity required")
    return out
