"""Generated from Smithy shape ``com.amazonaws.cloudfront#VpcOriginEndpointConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.origin_protocol_policy
    import capo_cloudfront.types.origin_ssl_protocols
    import capo_cloudfront.types.string


class VpcOriginEndpointConfig(TypedDict, closed=True):
    name: "capo_cloudfront.types.string.string"
    """<p>The name of the CloudFront VPC origin endpoint configuration.</p>"""
    arn: "capo_cloudfront.types.string.string"
    """<p>The ARN of the CloudFront VPC origin endpoint configuration.</p>"""
    http_port: "capo_cloudfront.types.integer.integer"
    """<p>The HTTP port for the CloudFront VPC origin endpoint configuration. The default value is <code>80</code>.</p>"""
    https_port: "capo_cloudfront.types.integer.integer"
    """<p>The HTTPS port of the CloudFront VPC origin endpoint configuration. The default value is <code>443</code>.</p>"""
    origin_protocol_policy: (
        "capo_cloudfront.types.origin_protocol_policy.OriginProtocolPolicy"
    )
    """<p>The origin protocol policy for the CloudFront VPC origin endpoint configuration.</p>"""
    origin_ssl_protocols: NotRequired[
        "capo_cloudfront.types.origin_ssl_protocols.OriginSslProtocols"
    ]


# --- restXml ser/de ---
def serialize_xml(value: VpcOriginEndpointConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "Arn").text = str(value["arn"])
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


def deserialize_xml(el: Element) -> VpcOriginEndpointConfig:
    out: VpcOriginEndpointConfig = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("VpcOriginEndpointConfig.name required")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("VpcOriginEndpointConfig.arn required")
    child_http_port = el.find("HTTPPort")
    if child_http_port is not None:
        out["http_port"] = int(child_http_port.text or "")
    else:
        raise DeserializationError("VpcOriginEndpointConfig.http_port required")
    child_https_port = el.find("HTTPSPort")
    if child_https_port is not None:
        out["https_port"] = int(child_https_port.text or "")
    else:
        raise DeserializationError("VpcOriginEndpointConfig.https_port required")
    child_origin_protocol_policy = el.find("OriginProtocolPolicy")
    if child_origin_protocol_policy is not None:
        import capo_cloudfront.types.origin_protocol_policy

        out["origin_protocol_policy"] = (
            capo_cloudfront.types.origin_protocol_policy.deserialize_xml(
                child_origin_protocol_policy
            )
        )
    else:
        raise DeserializationError(
            "VpcOriginEndpointConfig.origin_protocol_policy required"
        )
    child_origin_ssl_protocols = el.find("OriginSslProtocols")
    if child_origin_ssl_protocols is not None:
        import capo_cloudfront.types.origin_ssl_protocols

        out["origin_ssl_protocols"] = (
            capo_cloudfront.types.origin_ssl_protocols.deserialize_xml(
                child_origin_ssl_protocols
            )
        )
    return out
