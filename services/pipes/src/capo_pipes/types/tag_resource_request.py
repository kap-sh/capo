"""Generated from Smithy shape ``com.amazonaws.pipes#TagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.pipe_arn
    import capo_pipes.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_pipes.types.pipe_arn.PipeArn"
    """<p>The ARN of the pipe.</p>"""
    tags: "capo_pipes.types.tag_map.TagMap"
    """<p>The list of key-value pairs associated with the pipe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_pipes.types.tag_map

    out["tags"] = capo_pipes.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_pipes.types.tag_map

        out["tags"] = capo_pipes.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out


def redact_sensitive(value: TagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_pipes.types.tag_map

        out["tags"] = capo_pipes.types.tag_map.redact_sensitive(value["tags"])
    return out
