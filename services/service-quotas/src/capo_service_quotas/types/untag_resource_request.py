"""Generated from Smithy shape ``com.amazonaws.servicequotas#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_service_quotas.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_quotas.types.amazon_resource_name
    import capo_service_quotas.types.input_tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_service_quotas.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) for the applied quota that you want to untag. You can get this information by using the Service Quotas console, or by listing the quotas using the <a href="https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html">list-service-quotas</a> CLI command or the <a href="https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServiceQuotas.html">ListServiceQuotas</a> Amazon Web Services API operation.</p>"""
    tag_keys: "capo_service_quotas.types.input_tag_keys.InputTagKeys"
    """<p>The keys of the tags that you want to remove from the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_service_quotas.types.input_tag_keys

    out["TagKeys"] = capo_service_quotas.types.input_tag_keys.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if data.get("TagKeys") is not None:
        import capo_service_quotas.types.input_tag_keys

        out["tag_keys"] = (
            capo_service_quotas.types.input_tag_keys.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
