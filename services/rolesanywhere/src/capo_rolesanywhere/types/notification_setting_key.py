"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#NotificationSettingKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.notification_channel
    import capo_rolesanywhere.types.notification_event


class NotificationSettingKey(TypedDict, closed=True):
    event: "capo_rolesanywhere.types.notification_event.NotificationEvent"
    """<p>The notification setting event to reset.</p>"""
    channel: NotRequired[
        "capo_rolesanywhere.types.notification_channel.NotificationChannel"
    ]
    """<p>The specified channel of notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSettingKey) -> dict:
    out: dict = {}
    out["event"] = value["event"]
    if "channel" in value:
        out["channel"] = value["channel"]
    return out


def deserialize_json(data: dict) -> NotificationSettingKey:
    out: NotificationSettingKey = {}  # type: ignore[typeddict-item]
    if data.get("event") is not None:
        out["event"] = data["event"]
    else:
        out["event"] = ""
    if data.get("channel") is not None:
        out["channel"] = data["channel"]
    return out
