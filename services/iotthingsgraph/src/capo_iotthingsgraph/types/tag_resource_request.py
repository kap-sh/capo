"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.resource_arn
    import capo_iotthingsgraph.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_iotthingsgraph.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource whose tags are returned.</p>"""
    tags: "capo_iotthingsgraph.types.tag_list.TagList"
    """<p>A list of tags to add to the resource.></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_iotthingsgraph.types.tag_list

    out["tags"] = capo_iotthingsgraph.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_iotthingsgraph.types.tag_list

        out["tags"] = capo_iotthingsgraph.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        out["tags"] = []
    return out
