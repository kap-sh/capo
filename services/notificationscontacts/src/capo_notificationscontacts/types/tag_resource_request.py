"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_notificationscontacts.types.email_contact_arn
    import capo_notificationscontacts.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    arn: "capo_notificationscontacts.types.email_contact_arn.EmailContactArn"
    """<p>The ARN of the configuration.</p>"""
    tags: "capo_notificationscontacts.types.tag_map.TagMap"
    """<p>A list of tags to apply to the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_notificationscontacts.types.tag_map

    out["tags"] = capo_notificationscontacts.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_notificationscontacts.types.tag_map

        out["tags"] = capo_notificationscontacts.types.tag_map.deserialize_json(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
