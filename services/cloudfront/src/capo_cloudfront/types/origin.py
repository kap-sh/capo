"""Generated from Smithy shape ``com.amazonaws.cloudfront#Origin``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.custom_headers
    import capo_cloudfront.types.custom_origin_config
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.origin_shield
    import capo_cloudfront.types.s3_origin_config
    import capo_cloudfront.types.string
    import capo_cloudfront.types.vpc_origin_config


class Origin(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>A unique identifier for the origin. This value must be unique within the distribution.</p> <p>Use this value to specify the <code>TargetOriginId</code> in a <code>CacheBehavior</code> or <code>DefaultCacheBehavior</code>.</p>"""
    domain_name: "capo_cloudfront.types.string.string"
    """<p>The domain name for the origin.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesDomainName">Origin Domain Name</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    origin_path: NotRequired["capo_cloudfront.types.string.string"]
    """<p>An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesOriginPath">Origin Path</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    custom_headers: NotRequired["capo_cloudfront.types.custom_headers.CustomHeaders"]
    """<p>A list of HTTP header names and values that CloudFront adds to the requests that it sends to the origin.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/add-origin-custom-headers.html">Adding Custom Headers to Origin Requests</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    s3_origin_config: NotRequired[
        "capo_cloudfront.types.s3_origin_config.S3OriginConfig"
    ]
    """<p>Use this type to specify an origin that is an Amazon S3 bucket that is not configured with static website hosting. To specify any other type of origin, including an Amazon S3 bucket that is configured with static website hosting, use the <code>CustomOriginConfig</code> type instead.</p>"""
    custom_origin_config: NotRequired[
        "capo_cloudfront.types.custom_origin_config.CustomOriginConfig"
    ]
    """<p>Use this type to specify an origin that is not an Amazon S3 bucket, with one exception. If the Amazon S3 bucket is configured with static website hosting, use this type. If the Amazon S3 bucket is not configured with static website hosting, use the <code>S3OriginConfig</code> type instead.</p>"""
    vpc_origin_config: NotRequired[
        "capo_cloudfront.types.vpc_origin_config.VpcOriginConfig"
    ]
    """<p>The VPC origin configuration.</p>"""
    connection_attempts: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>The number of times that CloudFront attempts to connect to the origin. The minimum number is 1, the maximum is 3, and the default (if you don't specify otherwise) is 3.</p> <p>For a custom origin (including an Amazon S3 bucket that's configured with static website hosting), this value also specifies the number of times that CloudFront attempts to get a response from the origin, in the case of an <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesOriginResponseTimeout">Origin Response Timeout</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#origin-connection-attempts">Origin Connection Attempts</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    connection_timeout: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>The number of seconds that CloudFront waits when trying to establish a connection to the origin. The minimum timeout is 1 second, the maximum is 10 seconds, and the default (if you don't specify otherwise) is 10 seconds.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#origin-connection-timeout">Origin Connection Timeout</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    response_completion_timeout: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>The time (in seconds) that a request from CloudFront to the origin can stay open and wait for a response. If the complete response isn't received from the origin by this time, CloudFront ends the connection.</p> <p>The value for <code>ResponseCompletionTimeout</code> must be equal to or greater than the value for <code>OriginReadTimeout</code>. If you don't set a value for <code>ResponseCompletionTimeout</code>, CloudFront doesn't enforce a maximum value.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#response-completion-timeout">Response completion timeout</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    origin_shield: NotRequired["capo_cloudfront.types.origin_shield.OriginShield"]
    """<p>CloudFront Origin Shield. Using Origin Shield can help reduce the load on your origin.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html">Using Origin Shield</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    origin_access_control_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The unique identifier of an origin access control for this origin.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html">Restricting access to an Amazon S3 origin</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Origin, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "DomainName").text = str(value["domain_name"])
    if "origin_path" in value:
        SubElement(el, "OriginPath").text = str(value["origin_path"])
    if "custom_headers" in value:
        import capo_cloudfront.types.custom_headers

        capo_cloudfront.types.custom_headers.serialize_xml(
            value["custom_headers"], el, "CustomHeaders"
        )
    if "s3_origin_config" in value:
        import capo_cloudfront.types.s3_origin_config

        capo_cloudfront.types.s3_origin_config.serialize_xml(
            value["s3_origin_config"], el, "S3OriginConfig"
        )
    if "custom_origin_config" in value:
        import capo_cloudfront.types.custom_origin_config

        capo_cloudfront.types.custom_origin_config.serialize_xml(
            value["custom_origin_config"], el, "CustomOriginConfig"
        )
    if "vpc_origin_config" in value:
        import capo_cloudfront.types.vpc_origin_config

        capo_cloudfront.types.vpc_origin_config.serialize_xml(
            value["vpc_origin_config"], el, "VpcOriginConfig"
        )
    if "connection_attempts" in value:
        SubElement(el, "ConnectionAttempts").text = str(value["connection_attempts"])
    if "connection_timeout" in value:
        SubElement(el, "ConnectionTimeout").text = str(value["connection_timeout"])
    if "response_completion_timeout" in value:
        SubElement(el, "ResponseCompletionTimeout").text = str(
            value["response_completion_timeout"]
        )
    if "origin_shield" in value:
        import capo_cloudfront.types.origin_shield

        capo_cloudfront.types.origin_shield.serialize_xml(
            value["origin_shield"], el, "OriginShield"
        )
    if "origin_access_control_id" in value:
        SubElement(el, "OriginAccessControlId").text = str(
            value["origin_access_control_id"]
        )


def deserialize_xml(el: Element) -> Origin:
    out: Origin = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("Origin.id required")
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError("Origin.domain_name required")
    child_origin_path = el.find("OriginPath")
    if child_origin_path is not None:
        out["origin_path"] = str(child_origin_path.text or "")
    child_custom_headers = el.find("CustomHeaders")
    if child_custom_headers is not None:
        import capo_cloudfront.types.custom_headers

        out["custom_headers"] = capo_cloudfront.types.custom_headers.deserialize_xml(
            child_custom_headers
        )
    child_s3_origin_config = el.find("S3OriginConfig")
    if child_s3_origin_config is not None:
        import capo_cloudfront.types.s3_origin_config

        out["s3_origin_config"] = (
            capo_cloudfront.types.s3_origin_config.deserialize_xml(
                child_s3_origin_config
            )
        )
    child_custom_origin_config = el.find("CustomOriginConfig")
    if child_custom_origin_config is not None:
        import capo_cloudfront.types.custom_origin_config

        out["custom_origin_config"] = (
            capo_cloudfront.types.custom_origin_config.deserialize_xml(
                child_custom_origin_config
            )
        )
    child_vpc_origin_config = el.find("VpcOriginConfig")
    if child_vpc_origin_config is not None:
        import capo_cloudfront.types.vpc_origin_config

        out["vpc_origin_config"] = (
            capo_cloudfront.types.vpc_origin_config.deserialize_xml(
                child_vpc_origin_config
            )
        )
    child_connection_attempts = el.find("ConnectionAttempts")
    if child_connection_attempts is not None:
        out["connection_attempts"] = int(child_connection_attempts.text or "")
    child_connection_timeout = el.find("ConnectionTimeout")
    if child_connection_timeout is not None:
        out["connection_timeout"] = int(child_connection_timeout.text or "")
    child_response_completion_timeout = el.find("ResponseCompletionTimeout")
    if child_response_completion_timeout is not None:
        out["response_completion_timeout"] = int(
            child_response_completion_timeout.text or ""
        )
    child_origin_shield = el.find("OriginShield")
    if child_origin_shield is not None:
        import capo_cloudfront.types.origin_shield

        out["origin_shield"] = capo_cloudfront.types.origin_shield.deserialize_xml(
            child_origin_shield
        )
    child_origin_access_control_id = el.find("OriginAccessControlId")
    if child_origin_access_control_id is not None:
        out["origin_access_control_id"] = str(child_origin_access_control_id.text or "")
    return out
