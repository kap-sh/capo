"""Generated from Smithy shape ``com.amazonaws.drs#TagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.arn
    import capo_drs.types.tags_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_drs.types.arn.ARN"
    """<p>ARN of the resource for which tags are to be added or updated.</p>"""
    tags: "capo_drs.types.tags_map.TagsMap"
    """<p>Array of tags to be added or updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_drs.types.tags_map

    out["tags"] = capo_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out


def redact_sensitive(value: TagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
