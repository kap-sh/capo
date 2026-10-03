"""Generated from Smithy shape ``com.amazonaws.mediatailor#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_mediatailor.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) associated with the resource.</p>"""
    tags: "capo_mediatailor.types.__map_of__string.__mapOf__string"
    """<p>The tags to assign to the resource. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_mediatailor.types.__map_of__string

    out["tags"] = capo_mediatailor.types.__map_of__string.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
