"""Generated from Smithy shape ``com.amazonaws.memorydb#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string
    import capo_memorydb.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_memorydb.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the resource to which the tags are to be added.</p>"""
    tags: "capo_memorydb.types.tag_list.TagList"
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_memorydb.types.tag_list

    out["Tags"] = capo_memorydb.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_memorydb.types.tag_list

        out["tags"] = capo_memorydb.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        out["tags"] = []
    return out
