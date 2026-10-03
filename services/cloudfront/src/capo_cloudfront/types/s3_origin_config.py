"""Generated from Smithy shape ``com.amazonaws.cloudfront#S3OriginConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.string


class S3OriginConfig(TypedDict, closed=True):
    origin_access_identity: "capo_cloudfront.types.string.string"
    """<note> <p>If you're using origin access control (OAC) instead of origin access identity, specify an empty <code>OriginAccessIdentity</code> element. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-origin.html">Restricting access to an Amazon Web Services</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note> <p>The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can <i>only</i> access objects in an Amazon S3 bucket through CloudFront. The format of the value is:</p> <p> <code>origin-access-identity/cloudfront/ID-of-origin-access-identity</code> </p> <p>The <code> <i>ID-of-origin-access-identity</i> </code> is the value that CloudFront returned in the <code>ID</code> element when you created the origin access identity.</p> <p>If you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty <code>OriginAccessIdentity</code> element.</p> <p>To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty <code>OriginAccessIdentity</code> element.</p> <p>To replace the origin access identity, update the distribution configuration and specify the new origin access identity.</p> <p>For more information about the origin access identity, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">Serving Private Content through CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    origin_read_timeout: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>Specifies how long, in seconds, CloudFront waits for a response from the origin. This is also known as the <i>origin response timeout</i>. The minimum timeout is 1 second, the maximum is 120 seconds, and the default (if you don't specify otherwise) is 30 seconds.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginResponseTimeout">Response timeout</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3OriginConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "OriginAccessIdentity").text = str(
        value.get("origin_access_identity", "")
    )
    if "origin_read_timeout" in value:
        SubElement(el, "OriginReadTimeout").text = str(value["origin_read_timeout"])


def deserialize_xml(el: Element) -> S3OriginConfig:
    out: S3OriginConfig = {}  # type: ignore[typeddict-item]
    child_origin_access_identity = el.find("OriginAccessIdentity")
    if child_origin_access_identity is not None:
        out["origin_access_identity"] = str(child_origin_access_identity.text or "")
    else:
        out["origin_access_identity"] = ""
    child_origin_read_timeout = el.find("OriginReadTimeout")
    if child_origin_read_timeout is not None:
        out["origin_read_timeout"] = int(child_origin_read_timeout.text or "")
    return out
