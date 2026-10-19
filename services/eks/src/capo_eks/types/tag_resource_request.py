"""Generated from Smithy shape ``com.amazonaws.eks#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string
    import capo_eks.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_eks.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the resource to add tags to.</p>"""
    tags: "capo_eks.types.tag_map.TagMap"
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_eks.types.tag_map

    out["tags"] = capo_eks.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
