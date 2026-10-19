"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource. Tagging is only supported for directories.</p>"""
    tags: "capo_clouddirectory.types.tag_list.TagList"
    """<p>A list of tag key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_clouddirectory.types.tag_list

    out["Tags"] = capo_clouddirectory.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_clouddirectory.types.tag_list

        out["tags"] = capo_clouddirectory.types.tag_list.deserialize_json(data["Tags"])
    else:
        out["tags"] = []
    return out
