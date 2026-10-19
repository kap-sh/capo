"""Generated from Smithy shape ``com.amazonaws.datasync#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.tag_key_list
    import capo_datasync.types.taggable_resource_arn


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_datasync.types.taggable_resource_arn.TaggableResourceArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the resource to remove the tags from.</p>"""
    keys: "capo_datasync.types.tag_key_list.TagKeyList"
    """<p>Specifies the keys in the tags that you want to remove.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_datasync.types.tag_key_list

    out["Keys"] = capo_datasync.types.tag_key_list.serialize_aws_json_1_1(value["keys"])
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Keys") is not None:
        import capo_datasync.types.tag_key_list

        out["keys"] = capo_datasync.types.tag_key_list.deserialize_aws_json_1_1(
            data["Keys"]
        )
    else:
        out["keys"] = []
    return out
