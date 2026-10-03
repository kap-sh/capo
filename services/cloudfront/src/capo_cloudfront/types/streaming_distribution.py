"""Generated from Smithy shape ``com.amazonaws.cloudfront#StreamingDistribution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.active_trusted_signers
    import capo_cloudfront.types.streaming_distribution_config
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class StreamingDistribution(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The identifier for the RTMP distribution. For example: <code>EGTXBD79EXAMPLE</code>.</p>"""
    arn: "capo_cloudfront.types.string.string"
    """<p>The ARN (Amazon Resource Name) for the distribution. For example: <code>arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5</code>, where <code>123456789012</code> is your Amazon Web Services account ID.</p>"""
    status: "capo_cloudfront.types.string.string"
    """<p>The current status of the RTMP distribution. When the status is <code>Deployed</code>, the distribution's information is propagated to all CloudFront edge locations.</p>"""
    last_modified_time: NotRequired["capo_cloudfront.types.timestamp.timestamp"]
    """<p>The date and time that the distribution was last modified.</p>"""
    domain_name: "capo_cloudfront.types.string.string"
    """<p>The domain name that corresponds to the streaming distribution, for example, <code>s5c39gqb8ow64r.cloudfront.net</code>.</p>"""
    active_trusted_signers: (
        "capo_cloudfront.types.active_trusted_signers.ActiveTrustedSigners"
    )
    """<p>A complex type that lists the Amazon Web Services accounts, if any, that you included in the <code>TrustedSigners</code> complex type for this distribution. These are the accounts that you want to allow to create signed URLs for private content.</p> <p>The <code>Signer</code> complex type lists the Amazon Web Services account number of the trusted signer or <code>self</code> if the signer is the Amazon Web Services account that created the distribution. The <code>Signer</code> element also includes the IDs of any active CloudFront key pairs that are associated with the trusted signer's Amazon Web Services account. If no <code>KeyPairId</code> element appears for a <code>Signer</code>, that signer can't create signed URLs.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">Serving Private Content through CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    streaming_distribution_config: "capo_cloudfront.types.streaming_distribution_config.StreamingDistributionConfig"
    """<p>The current configuration information for the RTMP distribution.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: StreamingDistribution, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "ARN").text = str(value["arn"])
    SubElement(el, "Status").text = str(value["status"])
    if "last_modified_time" in value:
        import capo_cloudfront.types.timestamp

        capo_cloudfront.types.timestamp.serialize_xml(
            value["last_modified_time"], el, "LastModifiedTime"
        )
    SubElement(el, "DomainName").text = str(value["domain_name"])
    import capo_cloudfront.types.active_trusted_signers

    capo_cloudfront.types.active_trusted_signers.serialize_xml(
        value["active_trusted_signers"], el, "ActiveTrustedSigners"
    )
    import capo_cloudfront.types.streaming_distribution_config

    capo_cloudfront.types.streaming_distribution_config.serialize_xml(
        value["streaming_distribution_config"], el, "StreamingDistributionConfig"
    )


def deserialize_xml(el: Element) -> StreamingDistribution:
    out: StreamingDistribution = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("StreamingDistribution.id required")
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("StreamingDistribution.arn required")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    else:
        raise DeserializationError("StreamingDistribution.status required")
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError("StreamingDistribution.domain_name required")
    child_active_trusted_signers = el.find("ActiveTrustedSigners")
    if child_active_trusted_signers is not None:
        import capo_cloudfront.types.active_trusted_signers

        out["active_trusted_signers"] = (
            capo_cloudfront.types.active_trusted_signers.deserialize_xml(
                child_active_trusted_signers
            )
        )
    else:
        raise DeserializationError(
            "StreamingDistribution.active_trusted_signers required"
        )
    child_streaming_distribution_config = el.find("StreamingDistributionConfig")
    if child_streaming_distribution_config is not None:
        import capo_cloudfront.types.streaming_distribution_config

        out["streaming_distribution_config"] = (
            capo_cloudfront.types.streaming_distribution_config.deserialize_xml(
                child_streaming_distribution_config
            )
        )
    else:
        raise DeserializationError(
            "StreamingDistribution.streaming_distribution_config required"
        )
    return out
