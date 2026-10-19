"""Generated from Smithy shape ``com.amazonaws.scheduler#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.tag_list
    import capo_scheduler.types.tag_resource_arn


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_scheduler.types.tag_resource_arn.TagResourceArn"
    """<p>The Amazon Resource Name (ARN) of the schedule group that you are adding tags to.</p>"""
    tags: "capo_scheduler.types.tag_list.TagList"
    """<p>The list of tags to associate with the schedule group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_scheduler.types.tag_list

    out["Tags"] = capo_scheduler.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_scheduler.types.tag_list

        out["tags"] = capo_scheduler.types.tag_list.deserialize_json(data["Tags"])
    else:
        out["tags"] = []
    return out
