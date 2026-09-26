"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.arn
    import capo_network_security_manager.types.tag_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_network_security_manager.types.arn.Arn"
    """<p>The ARN of the resource to tag. The ARN must not include a <code>:DRAFT</code> qualifier.</p>"""
    tags: "capo_network_security_manager.types.tag_map.TagMap"
    """<p>The tags to add to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_network_security_manager.types.tag_map

    out["tags"] = capo_network_security_manager.types.tag_map.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_network_security_manager.types.tag_map

        out["tags"] = capo_network_security_manager.types.tag_map.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
