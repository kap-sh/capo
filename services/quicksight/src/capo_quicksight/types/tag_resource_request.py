"""Generated from Smithy shape ``com.amazonaws.quicksight#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>"""
    tags: "capo_quicksight.types.tag_list.TagList"
    """<p>Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.tag_list

    out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    else:
        out["tags"] = []
    return out
