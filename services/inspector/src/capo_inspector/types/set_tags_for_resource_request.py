"""Generated from Smithy shape ``com.amazonaws.inspector#SetTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.tag_list


class SetTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the assessment template that you want to set tags to.</p>"""
    tags: NotRequired["capo_inspector.types.tag_list.TagList"]
    """<p>A collection of key and value pairs that you want to set to the assessment template.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetTagsForResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    if "tags" in value:
        import capo_inspector.types.tag_list

        out["tags"] = capo_inspector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetTagsForResourceRequest:
    out: SetTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_inspector.types.tag_list

        out["tags"] = capo_inspector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
