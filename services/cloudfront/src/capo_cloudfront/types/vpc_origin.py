"""Generated from Smithy shape ``com.amazonaws.cloudfront#VpcOrigin``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp
    import capo_cloudfront.types.vpc_origin_endpoint_config


class VpcOrigin(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The VPC origin ID.</p>"""
    arn: "capo_cloudfront.types.string.string"
    """<p>The VPC origin ARN.</p>"""
    account_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The account ID of the Amazon Web Services account that owns the VPC origin.</p>"""
    status: "capo_cloudfront.types.string.string"
    """<p>The VPC origin status.</p>"""
    created_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The VPC origin created time.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The VPC origin last modified time.</p>"""
    vpc_origin_endpoint_config: (
        "capo_cloudfront.types.vpc_origin_endpoint_config.VpcOriginEndpointConfig"
    )
    """<p>The VPC origin endpoint configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: VpcOrigin, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Arn").text = str(value["arn"])
    if "account_id" in value:
        SubElement(el, "AccountId").text = str(value["account_id"])
    SubElement(el, "Status").text = str(value["status"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["created_time"], el, "CreatedTime"
    )
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    import capo_cloudfront.types.vpc_origin_endpoint_config

    capo_cloudfront.types.vpc_origin_endpoint_config.serialize_xml(
        value["vpc_origin_endpoint_config"], el, "VpcOriginEndpointConfig"
    )


def deserialize_xml(el: Element) -> VpcOrigin:
    out: VpcOrigin = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        out["arn"] = ""
    child_account_id = el.find("AccountId")
    if child_account_id is not None:
        out["account_id"] = str(child_account_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    else:
        out["status"] = ""
    child_created_time = el.find("CreatedTime")
    if child_created_time is not None:
        import capo_cloudfront.types.timestamp

        out["created_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_created_time
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_vpc_origin_endpoint_config = el.find("VpcOriginEndpointConfig")
    if child_vpc_origin_endpoint_config is not None:
        import capo_cloudfront.types.vpc_origin_endpoint_config

        out["vpc_origin_endpoint_config"] = (
            capo_cloudfront.types.vpc_origin_endpoint_config.deserialize_xml(
                child_vpc_origin_endpoint_config
            )
        )
    else:
        raise DeserializationError("VpcOrigin.vpc_origin_endpoint_config required")
    return out
