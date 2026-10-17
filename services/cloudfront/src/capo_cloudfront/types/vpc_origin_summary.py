"""Generated from Smithy shape ``com.amazonaws.cloudfront#VpcOriginSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp
    import capo_cloudfront.types.vpc_ip_address_type


class VpcOriginSummary(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The VPC origin summary ID.</p>"""
    name: "capo_cloudfront.types.string.string"
    """<p>The VPC origin summary name.</p>"""
    status: "capo_cloudfront.types.string.string"
    """<p>The VPC origin summary status.</p>"""
    created_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The VPC origin summary created time.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The VPC origin summary last modified time.</p>"""
    arn: "capo_cloudfront.types.string.string"
    """<p>The VPC origin summary ARN.</p>"""
    account_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The account ID of the Amazon Web Services account that owns the VPC origin.</p>"""
    origin_endpoint_arn: "capo_cloudfront.types.string.string"
    """<p>The VPC origin summary origin endpoint ARN.</p>"""
    ip_address_type: NotRequired[
        "capo_cloudfront.types.vpc_ip_address_type.VpcIpAddressType"
    ]
    """<p>The IP address type of the CloudFront VPC origin. Valid values are <code>ipv4</code> and <code>dualstack</code>. IPv6-only is not supported for VPC origins.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: VpcOriginSummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "Status").text = str(value["status"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["created_time"], el, "CreatedTime"
    )
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    SubElement(el, "Arn").text = str(value["arn"])
    if "account_id" in value:
        SubElement(el, "AccountId").text = str(value["account_id"])
    SubElement(el, "OriginEndpointArn").text = str(value["origin_endpoint_arn"])
    if "ip_address_type" in value:
        import capo_cloudfront.types.vpc_ip_address_type

        capo_cloudfront.types.vpc_ip_address_type.serialize_xml(
            value["ip_address_type"], el, "IpAddressType"
        )


def deserialize_xml(el: Element) -> VpcOriginSummary:
    out: VpcOriginSummary = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("VpcOriginSummary.id required")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("VpcOriginSummary.name required")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    else:
        raise DeserializationError("VpcOriginSummary.status required")
    child_created_time = el.find("CreatedTime")
    if child_created_time is not None:
        import capo_cloudfront.types.timestamp

        out["created_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_created_time
        )
    else:
        raise DeserializationError("VpcOriginSummary.created_time required")
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        raise DeserializationError("VpcOriginSummary.last_modified_time required")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("VpcOriginSummary.arn required")
    child_account_id = el.find("AccountId")
    if child_account_id is not None:
        out["account_id"] = str(child_account_id.text or "")
    child_origin_endpoint_arn = el.find("OriginEndpointArn")
    if child_origin_endpoint_arn is not None:
        out["origin_endpoint_arn"] = str(child_origin_endpoint_arn.text or "")
    else:
        raise DeserializationError("VpcOriginSummary.origin_endpoint_arn required")
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import capo_cloudfront.types.vpc_ip_address_type

        out["ip_address_type"] = (
            capo_cloudfront.types.vpc_ip_address_type.deserialize_xml(
                child_ip_address_type
            )
        )
    return out
