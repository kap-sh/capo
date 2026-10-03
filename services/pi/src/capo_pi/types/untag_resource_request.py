"""Generated from Smithy shape ``com.amazonaws.pi#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pi.types.amazon_resource_name
    import capo_pi.types.service_type
    import capo_pi.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    service_type: "capo_pi.types.service_type.ServiceType"
    """<p>List the tags for the Amazon Web Services service for which Performance Insights returns metrics. Valid value is <code>RDS</code>.</p>"""
    resource_arn: "capo_pi.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon RDS Performance Insights resource that the tags are added to. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing"> Constructing an RDS Amazon Resource Name (ARN)</a>.</p>"""
    tag_keys: "capo_pi.types.tag_key_list.TagKeyList"
    """<p>The metadata assigned to an Amazon RDS Performance Insights resource consisting of a key-value pair.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    import capo_pi.types.service_type

    out["ServiceType"] = capo_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["ResourceARN"] = value["resource_arn"]
    import capo_pi.types.tag_key_list

    out["TagKeys"] = capo_pi.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceType") is not None:
        import capo_pi.types.service_type

        out["service_type"] = capo_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.service_type required")
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if data.get("TagKeys") is not None:
        import capo_pi.types.tag_key_list

        out["tag_keys"] = capo_pi.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
