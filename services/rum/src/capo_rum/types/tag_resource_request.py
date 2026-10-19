"""Generated from Smithy shape ``com.amazonaws.rum#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rum.types.arn
    import capo_rum.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_rum.types.arn.Arn"
    """<p>The ARN of the CloudWatch RUM resource that you're adding tags to.</p>"""
    tags: "capo_rum.types.tag_map.TagMap"
    """<p>The list of key-value pairs to associate with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_rum.types.tag_map

    out["Tags"] = capo_rum.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_rum.types.tag_map

        out["tags"] = capo_rum.types.tag_map.deserialize_json(data["Tags"])
    else:
        out["tags"] = {}
    return out
