"""Generated from Smithy shape ``com.amazonaws.keyspaces#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.arn
    import capo_keyspaces.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_keyspaces.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the Amazon Keyspaces resource to which to add tags.</p>"""
    tags: "capo_keyspaces.types.tag_list.TagList"
    """<p>The tags to be assigned to the Amazon Keyspaces resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_keyspaces.types.tag_list

    out["tags"] = capo_keyspaces.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_keyspaces.types.tag_list

        out["tags"] = capo_keyspaces.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        out["tags"] = []
    return out
