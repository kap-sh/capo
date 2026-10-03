"""Generated from Smithy shape ``com.amazonaws.pi#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pi.types.amazon_resource_name
    import capo_pi.types.service_type


class ListTagsForResourceRequest(TypedDict, closed=True):
    service_type: "capo_pi.types.service_type.ServiceType"
    """<p>List the tags for the Amazon Web Services service for which Performance Insights returns metrics. Valid value is <code>RDS</code>.</p>"""
    resource_arn: "capo_pi.types.amazon_resource_name.AmazonResourceName"
    """<p>Lists all the tags for the Amazon RDS Performance Insights resource. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing"> Constructing an RDS Amazon Resource Name (ARN)</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    import capo_pi.types.service_type

    out["ServiceType"] = capo_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceType") is not None:
        import capo_pi.types.service_type

        out["service_type"] = capo_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    else:
        raise DeserializationError("ListTagsForResourceRequest.service_type required")
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    return out
