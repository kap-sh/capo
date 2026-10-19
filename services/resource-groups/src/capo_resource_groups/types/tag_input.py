"""Generated from Smithy shape ``com.amazonaws.resourcegroups#TagInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group_arn_v2
    import capo_resource_groups.types.tags


class TagInput(TypedDict, closed=True):
    arn: "capo_resource_groups.types.group_arn_v2.GroupArnV2"
    """<p>The Amazon resource name (ARN) of the resource group to which to add tags.</p>"""
    tags: "capo_resource_groups.types.tags.Tags"
    """<p>The tags to add to the specified resource group. A tag is a string-to-string map of key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagInput) -> dict:
    out: dict = {}
    import capo_resource_groups.types.tags

    out["Tags"] = capo_resource_groups.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagInput:
    out: TagInput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_resource_groups.types.tags

        out["tags"] = capo_resource_groups.types.tags.deserialize_json(data["Tags"])
    else:
        out["tags"] = {}
    return out
