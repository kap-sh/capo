"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.amazon_resource_arn
    import capo_lookoutequipment.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_lookoutequipment.types.amazon_resource_arn.AmazonResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to which the tag is currently associated. </p>"""
    tag_keys: "capo_lookoutequipment.types.tag_key_list.TagKeyList"
    """<p>Specifies the key of the tag to be removed from a specified resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_lookoutequipment.types.tag_key_list

    out["TagKeys"] = capo_lookoutequipment.types.tag_key_list.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_lookoutequipment.types.tag_key_list

        out["tag_keys"] = (
            capo_lookoutequipment.types.tag_key_list.deserialize_aws_json_1_0(
                data["TagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
