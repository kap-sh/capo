"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resource_arn
    import capo_marketplace_catalog.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_marketplace_catalog.types.resource_arn.ResourceARN"
    """<p>Required. The Amazon Resource Name (ARN) associated with the resource you want to tag.</p>"""
    tags: "capo_marketplace_catalog.types.tag_list.TagList"
    """<p>Required. A list of objects specifying each key name and value. Number of objects allowed: 1-50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_marketplace_catalog.types.tag_list

    out["Tags"] = capo_marketplace_catalog.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_marketplace_catalog.types.tag_list

        out["tags"] = capo_marketplace_catalog.types.tag_list.deserialize_json(
            data["Tags"]
        )
    else:
        out["tags"] = []
    return out
