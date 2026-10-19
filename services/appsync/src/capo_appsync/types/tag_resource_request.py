"""Generated from Smithy shape ``com.amazonaws.appsync#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.resource_arn
    import capo_appsync.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_appsync.types.resource_arn.ResourceArn"
    """<p>The <code>GraphqlApi</code> Amazon Resource Name (ARN).</p>"""
    tags: "capo_appsync.types.tag_map.TagMap"
    """<p>A <code>TagMap</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_appsync.types.tag_map

    out["tags"] = capo_appsync.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_appsync.types.tag_map

        out["tags"] = capo_appsync.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
