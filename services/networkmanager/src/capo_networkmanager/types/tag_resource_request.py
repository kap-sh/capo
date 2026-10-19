"""Generated from Smithy shape ``com.amazonaws.networkmanager#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.resource_arn
    import capo_networkmanager.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_networkmanager.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "capo_networkmanager.types.tag_list.TagList"
    """<p>The tags to apply to the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_networkmanager.types.tag_list

    out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    else:
        out["tags"] = []
    return out
