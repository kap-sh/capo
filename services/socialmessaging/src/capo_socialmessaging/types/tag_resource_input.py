"""Generated from Smithy shape ``com.amazonaws.socialmessaging#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.arn
    import capo_socialmessaging.types.tag_list


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_socialmessaging.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource to tag.</p>"""
    tags: "capo_socialmessaging.types.tag_list.TagList"
    """<p>The tags to add to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_socialmessaging.types.tag_list

    out["tags"] = capo_socialmessaging.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_socialmessaging.types.tag_list

        out["tags"] = capo_socialmessaging.types.tag_list.deserialize_json(data["tags"])
    else:
        out["tags"] = []
    return out
