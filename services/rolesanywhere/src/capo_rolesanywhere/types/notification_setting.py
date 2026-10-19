"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#NotificationSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.notification_channel
    import capo_rolesanywhere.types.notification_event


class NotificationSetting(TypedDict, closed=True):
    enabled: "bool"
    """<p>Indicates whether the notification setting is enabled.</p>"""
    event: "capo_rolesanywhere.types.notification_event.NotificationEvent"
    """<p>The event to which this notification setting is applied.</p>"""
    threshold: NotRequired["int"]
    """<p>The number of days before a notification event. This value is required for a notification setting that is enabled.</p>"""
    channel: NotRequired[
        "capo_rolesanywhere.types.notification_channel.NotificationChannel"
    ]
    """<p>The specified channel of notification. IAM Roles Anywhere uses CloudWatch metrics, EventBridge, and Health Dashboard to notify for an event.</p> <note> <p>In the absence of a specific channel, IAM Roles Anywhere applies this setting to 'ALL' channels.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSetting) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    out["event"] = value["event"]
    if "threshold" in value:
        out["threshold"] = value["threshold"]
    if "channel" in value:
        out["channel"] = value["channel"]
    return out


def deserialize_json(data: dict) -> NotificationSetting:
    out: NotificationSetting = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if data.get("event") is not None:
        out["event"] = data["event"]
    else:
        out["event"] = ""
    if data.get("threshold") is not None:
        out["threshold"] = data["threshold"]
    if data.get("channel") is not None:
        out["channel"] = data["channel"]
    return out
