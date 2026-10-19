"""Generated from Smithy shape ``com.amazonaws.iot#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.resource_arn
    import capo_iot.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_iot.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource.</p>"""
    tags: "capo_iot.types.tag_list.TagList"
    """<p>The new or modified tags for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_iot.types.tag_list

    out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    else:
        out["tags"] = []
    return out
