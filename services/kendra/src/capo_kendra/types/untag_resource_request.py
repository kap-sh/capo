"""Generated from Smithy shape ``com.amazonaws.kendra#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.amazon_resource_name
    import capo_kendra.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_kendra.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the index, FAQ, data source, or other resource to remove a tag. For example, the ARN of an index is constructed as follows: <i>arn:aws:kendra:your-region:your-account-id:index/index-id</i> For information on how to construct an ARN for all types of Amazon Kendra resources, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkendra.html#amazonkendra-resources-for-iam-policies">Resource types</a>.</p>"""
    tag_keys: "capo_kendra.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys to remove from the index, FAQ, data source, or other resource. If a tag key doesn't exist for the resource, it is ignored.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_kendra.types.tag_key_list

    out["TagKeys"] = capo_kendra.types.tag_key_list.serialize_aws_json_1_1(
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
        import capo_kendra.types.tag_key_list

        out["tag_keys"] = capo_kendra.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
