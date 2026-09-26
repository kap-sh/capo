"""Generated from Smithy shape ``com.amazonaws.supportauthz#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_supportauthz.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supportauthz.types.arn
    import capo_supportauthz.types.tags


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_supportauthz.types.arn.Arn"
    """<p>The ARN of the resource to tag.</p>"""
    tags: "capo_supportauthz.types.tags.Tags"
    """<p>The tags to add to the resource. Maximum of 50 tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_supportauthz.types.tags

    out["tags"] = capo_supportauthz.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_supportauthz.types.tags

        out["tags"] = capo_supportauthz.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
