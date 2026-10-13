"""Generated from Smithy shape ``com.amazonaws.mpa#UntagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mpa.types.string
    import capo_mpa.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_mpa.types.string.String"
    """<p>Amazon Resource Name (ARN) for the resource you want to untag.</p>"""
    tag_keys: "capo_mpa.types.tag_key_list.TagKeyList"
    """<p>Array of tag key-value pairs that you want to untag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    import capo_mpa.types.tag_key_list

    out["TagKeys"] = capo_mpa.types.tag_key_list.serialize_json(value["tag_keys"])
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("TagKeys") is not None:
        import capo_mpa.types.tag_key_list

        out["tag_keys"] = capo_mpa.types.tag_key_list.deserialize_json(data["TagKeys"])
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out


def redact_sensitive(value: UntagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tag_keys" in value:
        out["tag_keys"] = "*** Sensitive Data Redacted ***"
    return out
