"""Generated from Smithy shape ``com.amazonaws.cloudfront#StreamingDistributionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.aliases
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.price_class
    import capo_cloudfront.types.s3_origin
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp
    import capo_cloudfront.types.trusted_signers


class StreamingDistributionSummary(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The identifier for the distribution, for example, <code>EDFDVBD632BHDS5</code>.</p>"""
    arn: "capo_cloudfront.types.string.string"
    """<p>The ARN (Amazon Resource Name) for the streaming distribution. For example: <code>arn:aws:cloudfront::123456789012:streaming-distribution/EDFDVBD632BHDS5</code>, where <code>123456789012</code> is your Amazon Web Services account ID.</p>"""
    status: "capo_cloudfront.types.string.string"
    """<p>Indicates the current status of the distribution. When the status is <code>Deployed</code>, the distribution's information is fully propagated throughout the Amazon CloudFront system.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The date and time the distribution was last modified.</p>"""
    domain_name: "capo_cloudfront.types.string.string"
    """<p>The domain name corresponding to the distribution, for example, <code>d111111abcdef8.cloudfront.net</code>.</p>"""
    s3_origin: "capo_cloudfront.types.s3_origin.S3Origin"
    """<p>A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.</p>"""
    aliases: "capo_cloudfront.types.aliases.Aliases"
    """<p>A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.</p>"""
    trusted_signers: "capo_cloudfront.types.trusted_signers.TrustedSigners"
    """<p>A complex type that specifies the Amazon Web Services accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the <code>PathPattern</code> for this cache behavior, specify <code>true</code> for <code>Enabled</code>, and specify the applicable values for <code>Quantity</code> and <code>Items</code>.If you don't want to require signed URLs in requests for objects that match <code>PathPattern</code>, specify <code>false</code> for <code>Enabled</code> and <code>0</code> for <code>Quantity</code>. Omit <code>Items</code>. To add, change, or remove one or more trusted signers, change <code>Enabled</code> to <code>true</code> (if it's currently <code>false</code>), change <code>Quantity</code> as applicable, and specify all of the trusted signers that you want to include in the updated distribution.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">Serving Private Content through CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    comment: "capo_cloudfront.types.string.string"
    """<p>The comment originally specified when this distribution was created.</p>"""
    price_class: "capo_cloudfront.types.price_class.PriceClass"
    """<p>A complex type that contains information about price class for this streaming distribution.</p>"""
    enabled: "capo_cloudfront.types.boolean.boolean"
    """<p>Whether the distribution is enabled to accept end user requests for content.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: StreamingDistributionSummary, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "ARN").text = str(value["arn"])
    SubElement(el, "Status").text = str(value["status"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    SubElement(el, "DomainName").text = str(value["domain_name"])
    import capo_cloudfront.types.s3_origin

    capo_cloudfront.types.s3_origin.serialize_xml(value["s3_origin"], el, "S3Origin")
    import capo_cloudfront.types.aliases

    capo_cloudfront.types.aliases.serialize_xml(value["aliases"], el, "Aliases")
    import capo_cloudfront.types.trusted_signers

    capo_cloudfront.types.trusted_signers.serialize_xml(
        value["trusted_signers"], el, "TrustedSigners"
    )
    SubElement(el, "Comment").text = str(value["comment"])
    import capo_cloudfront.types.price_class

    capo_cloudfront.types.price_class.serialize_xml(
        value["price_class"], el, "PriceClass"
    )
    SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"


def deserialize_xml(el: Element) -> StreamingDistributionSummary:
    out: StreamingDistributionSummary = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("StreamingDistributionSummary.id required")
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("StreamingDistributionSummary.arn required")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    else:
        raise DeserializationError("StreamingDistributionSummary.status required")
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        raise DeserializationError(
            "StreamingDistributionSummary.last_modified_time required"
        )
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError("StreamingDistributionSummary.domain_name required")
    child_s3_origin = el.find("S3Origin")
    if child_s3_origin is not None:
        import capo_cloudfront.types.s3_origin

        out["s3_origin"] = capo_cloudfront.types.s3_origin.deserialize_xml(
            child_s3_origin
        )
    else:
        raise DeserializationError("StreamingDistributionSummary.s3_origin required")
    child_aliases = el.find("Aliases")
    if child_aliases is not None:
        import capo_cloudfront.types.aliases

        out["aliases"] = capo_cloudfront.types.aliases.deserialize_xml(child_aliases)
    else:
        raise DeserializationError("StreamingDistributionSummary.aliases required")
    child_trusted_signers = el.find("TrustedSigners")
    if child_trusted_signers is not None:
        import capo_cloudfront.types.trusted_signers

        out["trusted_signers"] = capo_cloudfront.types.trusted_signers.deserialize_xml(
            child_trusted_signers
        )
    else:
        raise DeserializationError(
            "StreamingDistributionSummary.trusted_signers required"
        )
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    else:
        raise DeserializationError("StreamingDistributionSummary.comment required")
    child_price_class = el.find("PriceClass")
    if child_price_class is not None:
        import capo_cloudfront.types.price_class

        out["price_class"] = capo_cloudfront.types.price_class.deserialize_xml(
            child_price_class
        )
    else:
        raise DeserializationError("StreamingDistributionSummary.price_class required")
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        raise DeserializationError("StreamingDistributionSummary.enabled required")
    return out
