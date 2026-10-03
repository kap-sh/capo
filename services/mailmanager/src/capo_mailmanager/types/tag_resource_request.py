"""Generated from Smithy shape ``com.amazonaws.mailmanager#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.tag_list
    import capo_mailmanager.types.taggable_resource_arn


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_mailmanager.types.taggable_resource_arn.TaggableResourceArn"
    """<p> The Amazon Resource Name (ARN) of the resource that you want to tag. </p>"""
    tags: "capo_mailmanager.types.tag_list.TagList"
    """<p> The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_mailmanager.types.tag_list

    out["Tags"] = capo_mailmanager.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if data.get("Tags") is not None:
        import capo_mailmanager.types.tag_list

        out["tags"] = capo_mailmanager.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
