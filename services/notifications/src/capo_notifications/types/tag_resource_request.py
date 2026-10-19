"""Generated from Smithy shape ``com.amazonaws.notifications#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.notification_configuration_arn
    import capo_notifications.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The Amazon Resource Name (ARN) to use to tag a resource.</p>"""
    tags: "capo_notifications.types.tag_map.TagMap"
    """<p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_notifications.types.tag_map

    out["tags"] = capo_notifications.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_notifications.types.tag_map

        out["tags"] = capo_notifications.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
