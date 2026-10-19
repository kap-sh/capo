"""Generated from Smithy shape ``com.amazonaws.billingconductor#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.arn
    import capo_billingconductor.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_billingconductor.types.arn.Arn"
    """<p> The Amazon Resource Name (ARN) of the resource to which to add tags. </p>"""
    tags: "capo_billingconductor.types.tag_map.TagMap"
    """<p> The tags to add to the resource as a list of key-value pairs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_billingconductor.types.tag_map

    out["Tags"] = capo_billingconductor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_billingconductor.types.tag_map

        out["tags"] = capo_billingconductor.types.tag_map.deserialize_json(data["Tags"])
    else:
        out["tags"] = {}
    return out
