"""Generated from Smithy shape ``com.amazonaws.securitylake#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.amazon_resource_name
    import capo_securitylake.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_securitylake.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Amazon Security Lake resource to add or update the tags for.</p>"""
    tags: "capo_securitylake.types.tag_list.TagList"
    """<p>An array of objects, one for each tag (key and value) to associate with the Amazon Security Lake resource. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_securitylake.types.tag_list

    out["tags"] = capo_securitylake.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_securitylake.types.tag_list

        out["tags"] = capo_securitylake.types.tag_list.deserialize_json(data["tags"])
    else:
        out["tags"] = []
    return out
