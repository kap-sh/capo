"""Generated from Smithy shape ``com.amazonaws.rekognition#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.resource_arn
    import capo_rekognition.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_rekognition.types.resource_arn.ResourceArn"
    """<p> Amazon Resource Name (ARN) of the model, collection, or stream processor that you want to remove the tags from. </p>"""
    tag_keys: "capo_rekognition.types.tag_key_list.TagKeyList"
    """<p> A list of the tags that you want to remove. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_rekognition.types.tag_key_list

    out["TagKeys"] = capo_rekognition.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_rekognition.types.tag_key_list

        out["tag_keys"] = capo_rekognition.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
