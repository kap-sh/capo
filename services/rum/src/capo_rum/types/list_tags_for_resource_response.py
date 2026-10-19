"""Generated from Smithy shape ``com.amazonaws.rum#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rum.types.arn
    import capo_rum.types.tag_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    resource_arn: "capo_rum.types.arn.Arn"
    """<p>The ARN of the resource that you are viewing.</p>"""
    tags: "capo_rum.types.tag_map.TagMap"
    """<p>The list of tag keys and values associated with the resource you specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_rum.types.tag_map

    out["Tags"] = capo_rum.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_rum.types.tag_map

        out["tags"] = capo_rum.types.tag_map.deserialize_json(data["Tags"])
    else:
        out["tags"] = {}
    return out
