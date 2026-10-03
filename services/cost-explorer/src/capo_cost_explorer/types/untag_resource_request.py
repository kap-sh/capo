"""Generated from Smithy shape ``com.amazonaws.costexplorer#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.arn
    import capo_cost_explorer.types.resource_tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_cost_explorer.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource. For a list of supported resources, see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ResourceTag.html">ResourceTag</a>. </p>"""
    resource_tag_keys: (
        "capo_cost_explorer.types.resource_tag_key_list.ResourceTagKeyList"
    )
    """<p>A list of tag keys associated with tags that need to be removed from the resource. If you specify a tag key that doesn't exist, it's ignored. Although the maximum number of array members is 200, user-tag maximum is 50. The remaining are reserved for Amazon Web Services use. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_cost_explorer.types.resource_tag_key_list

    out["ResourceTagKeys"] = (
        capo_cost_explorer.types.resource_tag_key_list.serialize_aws_json_1_1(
            value["resource_tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if data.get("ResourceTagKeys") is not None:
        import capo_cost_explorer.types.resource_tag_key_list

        out["resource_tag_keys"] = (
            capo_cost_explorer.types.resource_tag_key_list.deserialize_aws_json_1_1(
                data["ResourceTagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.resource_tag_keys required")
    return out
