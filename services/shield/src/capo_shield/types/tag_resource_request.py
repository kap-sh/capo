"""Generated from Smithy shape ``com.amazonaws.shield#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_shield.types.resource_arn
    import capo_shield.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_shield.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to add or update tags for.</p>"""
    tags: "capo_shield.types.tag_list.TagList"
    """<p>The tags that you want to modify or add to the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_shield.types.tag_list

    out["Tags"] = capo_shield.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_shield.types.tag_list

        out["tags"] = capo_shield.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    else:
        out["tags"] = []
    return out
