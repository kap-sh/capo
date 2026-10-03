"""Generated from Smithy shape ``com.amazonaws.backup#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.tags


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_backup.types.arn.ARN"
    """<p>The ARN that uniquely identifies the resource.</p>"""
    tags: "capo_backup.types.tags.Tags"
    """<p>Key-value pairs that are used to help organize your resources. You can assign your own metadata to the resources you create. For clarity, this is the structure to assign tags: <code>[{"Key":"string","Value":"string"}]</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_backup.types.tags

    out["Tags"] = capo_backup.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_backup.types.tags

        out["tags"] = capo_backup.types.tags.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
