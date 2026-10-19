"""Generated from Smithy shape ``com.amazonaws.mailmanager#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.tag_key_list
    import capo_mailmanager.types.taggable_resource_arn


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_mailmanager.types.taggable_resource_arn.TaggableResourceArn"
    """<p> The Amazon Resource Name (ARN) of the resource that you want to untag. </p>"""
    tag_keys: "capo_mailmanager.types.tag_key_list.TagKeyList"
    """<p> The keys of the key-value pairs for the tag or tags you want to remove from the specified resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_mailmanager.types.tag_key_list

    out["TagKeys"] = capo_mailmanager.types.tag_key_list.serialize_aws_json_1_0(
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
        import capo_mailmanager.types.tag_key_list

        out["tag_keys"] = capo_mailmanager.types.tag_key_list.deserialize_aws_json_1_0(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
