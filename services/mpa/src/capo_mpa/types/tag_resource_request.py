"""Generated from Smithy shape ``com.amazonaws.mpa#TagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mpa.types.string
    import capo_mpa.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_mpa.types.string.String"
    """<p>Amazon Resource Name (ARN) for the resource you want to tag.</p>"""
    tags: "capo_mpa.types.tags.Tags"
    """<p>Tags that you have added to the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_mpa.types.tags

    out["Tags"] = capo_mpa.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_mpa.types.tags

        out["tags"] = capo_mpa.types.tags.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out


def redact_sensitive(value: TagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
