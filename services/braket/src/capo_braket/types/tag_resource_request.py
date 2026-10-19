"""Generated from Smithy shape ``com.amazonaws.braket#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_braket.types.tags_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>Specify the <code>resourceArn</code> of the resource to which a tag will be added.</p>"""
    tags: "capo_braket.types.tags_map.TagsMap"
    """<p>Specify the tags to add to the resource. Tags can be specified as a key-value map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_braket.types.tags_map

    out["tags"] = capo_braket.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
