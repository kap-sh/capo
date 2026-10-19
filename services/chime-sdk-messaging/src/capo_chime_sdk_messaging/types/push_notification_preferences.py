"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#PushNotificationPreferences``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.allow_notifications
    import capo_chime_sdk_messaging.types.filter_rule


class PushNotificationPreferences(TypedDict, closed=True):
    allow_notifications: (
        "capo_chime_sdk_messaging.types.allow_notifications.AllowNotifications"
    )
    """<p>Enum value that indicates which push notifications to send to the requested member of a channel. <code>ALL</code> sends all push notifications, <code>NONE</code> sends no push notifications, <code>FILTERED</code> sends only filtered push notifications. </p>"""
    filter_rule: NotRequired["capo_chime_sdk_messaging.types.filter_rule.FilterRule"]
    """<p>The simple JSON object used to send a subset of a push notification to the requested member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PushNotificationPreferences) -> dict:
    out: dict = {}
    import capo_chime_sdk_messaging.types.allow_notifications

    out["AllowNotifications"] = (
        capo_chime_sdk_messaging.types.allow_notifications.serialize_json(
            value["allow_notifications"]
        )
    )
    if "filter_rule" in value:
        out["FilterRule"] = value["filter_rule"]
    return out


def deserialize_json(data: dict) -> PushNotificationPreferences:
    out: PushNotificationPreferences = {}  # type: ignore[typeddict-item]
    if data.get("AllowNotifications") is not None:
        import capo_chime_sdk_messaging.types.allow_notifications

        out["allow_notifications"] = (
            capo_chime_sdk_messaging.types.allow_notifications.deserialize_json(
                data["AllowNotifications"]
            )
        )
    else:
        import typing

        out["allow_notifications"] = typing.cast(
            "capo_chime_sdk_messaging.types.allow_notifications.AllowNotifications", ""
        )
    if data.get("FilterRule") is not None:
        out["filter_rule"] = data["FilterRule"]
    return out


def redact_sensitive(value: PushNotificationPreferences) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filter_rule" in value:
        out["filter_rule"] = "*** Sensitive Data Redacted ***"
    return out
