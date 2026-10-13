"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMembershipPreferences``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.push_notification_preferences


class ChannelMembershipPreferences(TypedDict, closed=True):
    push_notifications: NotRequired[
        "capo_chime_sdk_messaging.types.push_notification_preferences.PushNotificationPreferences"
    ]
    """<p>The push notification configuration of a message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMembershipPreferences) -> dict:
    out: dict = {}
    if "push_notifications" in value:
        import capo_chime_sdk_messaging.types.push_notification_preferences

        out["PushNotifications"] = (
            capo_chime_sdk_messaging.types.push_notification_preferences.serialize_json(
                value["push_notifications"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChannelMembershipPreferences:
    out: ChannelMembershipPreferences = {}  # type: ignore[typeddict-item]
    if data.get("PushNotifications") is not None:
        import capo_chime_sdk_messaging.types.push_notification_preferences

        out["push_notifications"] = (
            capo_chime_sdk_messaging.types.push_notification_preferences.deserialize_json(
                data["PushNotifications"]
            )
        )
    return out


def redact_sensitive(value: ChannelMembershipPreferences) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "push_notifications" in value:
        import capo_chime_sdk_messaging.types.push_notification_preferences

        out["push_notifications"] = (
            capo_chime_sdk_messaging.types.push_notification_preferences.redact_sensitive(
                value["push_notifications"]
            )
        )
    return out
