"""Generated from Smithy shape ``com.amazonaws.supplychain#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.asc_resource_arn
    import capo_supplychain.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_supplychain.types.asc_resource_arn.AscResourceArn"
    """<p>The Amazon Web Services Supply chain resource ARN that needs to be tagged.</p>"""
    tags: "capo_supplychain.types.tag_map.TagMap"
    """<p>The tags of the Amazon Web Services Supply chain resource to be created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_supplychain.types.tag_map

    out["tags"] = capo_supplychain.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_supplychain.types.tag_map

        out["tags"] = capo_supplychain.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
