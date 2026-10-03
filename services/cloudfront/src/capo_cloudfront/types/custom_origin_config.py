"""Generated from Smithy shape ``com.amazonaws.cloudfront#CustomOriginConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.ip_address_type
    import capo_cloudfront.types.origin_mtls_config
    import capo_cloudfront.types.origin_protocol_policy
    import capo_cloudfront.types.origin_ssl_protocols


class CustomOriginConfig(TypedDict, closed=True):
    http_port: "capo_cloudfront.types.integer.integer"
    """<p>The HTTP port that CloudFront uses to connect to the origin. Specify the HTTP port that the origin listens on.</p>"""
    https_port: "capo_cloudfront.types.integer.integer"
    """<p>The HTTPS port that CloudFront uses to connect to the origin. Specify the HTTPS port that the origin listens on.</p>"""
    origin_protocol_policy: (
        "capo_cloudfront.types.origin_protocol_policy.OriginProtocolPolicy"
    )
    """<p>Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Valid values are:</p> <ul> <li> <p> <code>http-only</code> – CloudFront always uses HTTP to connect to the origin.</p> </li> <li> <p> <code>match-viewer</code> – CloudFront connects to the origin using the same protocol that the viewer used to connect to CloudFront.</p> </li> <li> <p> <code>https-only</code> – CloudFront always uses HTTPS to connect to the origin.</p> </li> </ul>"""
    origin_ssl_protocols: NotRequired[
        "capo_cloudfront.types.origin_ssl_protocols.OriginSslProtocols"
    ]
    """<p>Specifies the minimum SSL/TLS protocol that CloudFront uses when connecting to your origin over HTTPS. Valid values include <code>SSLv3</code>, <code>TLSv1</code>, <code>TLSv1.1</code>, and <code>TLSv1.2</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginSSLProtocols">Minimum Origin SSL Protocol</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    origin_read_timeout: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>Specifies how long, in seconds, CloudFront waits for a response from the origin. This is also known as the <i>origin response timeout</i>. The minimum timeout is 1 second, the maximum is 120 seconds, and the default (if you don't specify otherwise) is 30 seconds.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginResponseTimeout">Response timeout</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    origin_keepalive_timeout: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>Specifies how long, in seconds, CloudFront persists its connection to the origin. The minimum timeout is 1 second, the maximum is 120 seconds, and the default (if you don't specify otherwise) is 5 seconds.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginKeepaliveTimeout">Keep-alive timeout (custom origins only)</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    ip_address_type: NotRequired["capo_cloudfront.types.ip_address_type.IpAddressType"]
    """<p>Specifies which IP protocol CloudFront uses when connecting to your origin. If your origin uses both IPv4 and IPv6 protocols, you can choose <code>dualstack</code> to help optimize reliability.</p>"""
    origin_mtls_config: NotRequired[
        "capo_cloudfront.types.origin_mtls_config.OriginMtlsConfig"
    ]
    """<p>Configures mutual TLS authentication between CloudFront and your origin server.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CustomOriginConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "HTTPPort").text = str(value["http_port"])
    SubElement(el, "HTTPSPort").text = str(value["https_port"])
    import capo_cloudfront.types.origin_protocol_policy

    capo_cloudfront.types.origin_protocol_policy.serialize_xml(
        value["origin_protocol_policy"], el, "OriginProtocolPolicy"
    )
    if "origin_ssl_protocols" in value:
        import capo_cloudfront.types.origin_ssl_protocols

        capo_cloudfront.types.origin_ssl_protocols.serialize_xml(
            value["origin_ssl_protocols"], el, "OriginSslProtocols"
        )
    if "origin_read_timeout" in value:
        SubElement(el, "OriginReadTimeout").text = str(value["origin_read_timeout"])
    if "origin_keepalive_timeout" in value:
        SubElement(el, "OriginKeepaliveTimeout").text = str(
            value["origin_keepalive_timeout"]
        )
    if "ip_address_type" in value:
        import capo_cloudfront.types.ip_address_type

        capo_cloudfront.types.ip_address_type.serialize_xml(
            value["ip_address_type"], el, "IpAddressType"
        )
    if "origin_mtls_config" in value:
        import capo_cloudfront.types.origin_mtls_config

        capo_cloudfront.types.origin_mtls_config.serialize_xml(
            value["origin_mtls_config"], el, "OriginMtlsConfig"
        )


def deserialize_xml(el: Element) -> CustomOriginConfig:
    out: CustomOriginConfig = {}  # type: ignore[typeddict-item]
    child_http_port = el.find("HTTPPort")
    if child_http_port is not None:
        out["http_port"] = int(child_http_port.text or "")
    else:
        raise DeserializationError("CustomOriginConfig.http_port required")
    child_https_port = el.find("HTTPSPort")
    if child_https_port is not None:
        out["https_port"] = int(child_https_port.text or "")
    else:
        raise DeserializationError("CustomOriginConfig.https_port required")
    child_origin_protocol_policy = el.find("OriginProtocolPolicy")
    if child_origin_protocol_policy is not None:
        import capo_cloudfront.types.origin_protocol_policy

        out["origin_protocol_policy"] = (
            capo_cloudfront.types.origin_protocol_policy.deserialize_xml(
                child_origin_protocol_policy
            )
        )
    else:
        raise DeserializationError("CustomOriginConfig.origin_protocol_policy required")
    child_origin_ssl_protocols = el.find("OriginSslProtocols")
    if child_origin_ssl_protocols is not None:
        import capo_cloudfront.types.origin_ssl_protocols

        out["origin_ssl_protocols"] = (
            capo_cloudfront.types.origin_ssl_protocols.deserialize_xml(
                child_origin_ssl_protocols
            )
        )
    child_origin_read_timeout = el.find("OriginReadTimeout")
    if child_origin_read_timeout is not None:
        out["origin_read_timeout"] = int(child_origin_read_timeout.text or "")
    child_origin_keepalive_timeout = el.find("OriginKeepaliveTimeout")
    if child_origin_keepalive_timeout is not None:
        out["origin_keepalive_timeout"] = int(child_origin_keepalive_timeout.text or "")
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import capo_cloudfront.types.ip_address_type

        out["ip_address_type"] = capo_cloudfront.types.ip_address_type.deserialize_xml(
            child_ip_address_type
        )
    child_origin_mtls_config = el.find("OriginMtlsConfig")
    if child_origin_mtls_config is not None:
        import capo_cloudfront.types.origin_mtls_config

        out["origin_mtls_config"] = (
            capo_cloudfront.types.origin_mtls_config.deserialize_xml(
                child_origin_mtls_config
            )
        )
    return out
