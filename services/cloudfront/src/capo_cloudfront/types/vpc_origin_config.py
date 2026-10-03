"""Generated from Smithy shape ``com.amazonaws.cloudfront#VpcOriginConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.string


class VpcOriginConfig(TypedDict, closed=True):
    vpc_origin_id: "capo_cloudfront.types.string.string"
    """<p>The VPC origin ID.</p>"""
    owner_account_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The account ID of the Amazon Web Services account that owns the VPC origin.</p>"""
    origin_read_timeout: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>Specifies how long, in seconds, CloudFront waits for a response from the origin. This is also known as the <i>origin response timeout</i>. The minimum timeout is 1 second, the maximum is 120 seconds, and the default (if you don't specify otherwise) is 30 seconds.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginResponseTimeout">Response timeout</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    origin_keepalive_timeout: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>Specifies how long, in seconds, CloudFront persists its connection to the origin. The minimum timeout is 1 second, the maximum is 120 seconds, and the default (if you don't specify otherwise) is 5 seconds.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginKeepaliveTimeout">Keep-alive timeout (custom origins only)</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: VpcOriginConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "VpcOriginId").text = str(value["vpc_origin_id"])
    if "owner_account_id" in value:
        SubElement(el, "OwnerAccountId").text = str(value["owner_account_id"])
    if "origin_read_timeout" in value:
        SubElement(el, "OriginReadTimeout").text = str(value["origin_read_timeout"])
    if "origin_keepalive_timeout" in value:
        SubElement(el, "OriginKeepaliveTimeout").text = str(
            value["origin_keepalive_timeout"]
        )


def deserialize_xml(el: Element) -> VpcOriginConfig:
    out: VpcOriginConfig = {}  # type: ignore[typeddict-item]
    child_vpc_origin_id = el.find("VpcOriginId")
    if child_vpc_origin_id is not None:
        out["vpc_origin_id"] = str(child_vpc_origin_id.text or "")
    else:
        raise DeserializationError("VpcOriginConfig.vpc_origin_id required")
    child_owner_account_id = el.find("OwnerAccountId")
    if child_owner_account_id is not None:
        out["owner_account_id"] = str(child_owner_account_id.text or "")
    child_origin_read_timeout = el.find("OriginReadTimeout")
    if child_origin_read_timeout is not None:
        out["origin_read_timeout"] = int(child_origin_read_timeout.text or "")
    child_origin_keepalive_timeout = el.find("OriginKeepaliveTimeout")
    if child_origin_keepalive_timeout is not None:
        out["origin_keepalive_timeout"] = int(child_origin_keepalive_timeout.text or "")
    return out
