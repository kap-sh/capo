"""Generated from Smithy shape ``com.amazonaws.dynamodb#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.resource_arn_string
    import capo_dynamodb.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_dynamodb.types.resource_arn_string.ResourceArnString"
    """<p>The DynamoDB resource that the tags will be removed from. This value is an Amazon Resource Name (ARN).</p>"""
    tag_keys: "capo_dynamodb.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys. Existing tags of the resource whose keys are members of this list will be removed from the DynamoDB resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_dynamodb.types.tag_key_list

    out["TagKeys"] = capo_dynamodb.types.tag_key_list.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_dynamodb.types.tag_key_list

        out["tag_keys"] = capo_dynamodb.types.tag_key_list.deserialize_aws_json_1_0(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
