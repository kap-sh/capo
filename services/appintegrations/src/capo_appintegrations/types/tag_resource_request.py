"""Generated from Smithy shape ``com.amazonaws.appintegrations#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appintegrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appintegrations.types.arn
    import capo_appintegrations.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_appintegrations.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "capo_appintegrations.types.tag_map.TagMap"
    """<p>The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_appintegrations.types.tag_map

    out["tags"] = capo_appintegrations.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_appintegrations.types.tag_map

        out["tags"] = capo_appintegrations.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
