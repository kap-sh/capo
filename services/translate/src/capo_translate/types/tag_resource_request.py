"""Generated from Smithy shape ``com.amazonaws.translate#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_translate.types.resource_arn
    import capo_translate.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_translate.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the given Amazon Translate resource to which you want to associate the tags. </p>"""
    tags: "capo_translate.types.tag_list.TagList"
    """<p>Tags being associated with a specific Amazon Translate resource. There can be a maximum of 50 tags (both existing and pending) associated with a specific resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_translate.types.tag_list

    out["Tags"] = capo_translate.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_translate.types.tag_list

        out["tags"] = capo_translate.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        out["tags"] = []
    return out
