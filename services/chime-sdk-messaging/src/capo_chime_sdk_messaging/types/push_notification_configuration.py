"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#PushNotificationConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.push_notification_body
    import capo_chime_sdk_messaging.types.push_notification_title
    import capo_chime_sdk_messaging.types.push_notification_type


class PushNotificationConfiguration(TypedDict, closed=True):
    title: NotRequired[
        "capo_chime_sdk_messaging.types.push_notification_title.PushNotificationTitle"
    ]
    """<p>The title of the push notification.</p>"""
    body: NotRequired[
        "capo_chime_sdk_messaging.types.push_notification_body.PushNotificationBody"
    ]
    """<p>The body of the push notification.</p>"""
    type: NotRequired[
        "capo_chime_sdk_messaging.types.push_notification_type.PushNotificationType"
    ]
    """<p>Enum value that indicates the type of the push notification for a message. <code>DEFAULT</code>: Normal mobile push notification. <code>VOIP</code>: VOIP mobile push notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PushNotificationConfiguration) -> dict:
    out: dict = {}
    if "title" in value:
        out["Title"] = value["title"]
    if "body" in value:
        out["Body"] = value["body"]
    if "type" in value:
        import capo_chime_sdk_messaging.types.push_notification_type

        out["Type"] = (
            capo_chime_sdk_messaging.types.push_notification_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> PushNotificationConfiguration:
    out: PushNotificationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    if data.get("Type") is not None:
        import capo_chime_sdk_messaging.types.push_notification_type

        out["type"] = (
            capo_chime_sdk_messaging.types.push_notification_type.deserialize_json(
                data["Type"]
            )
        )
    return out


def redact_sensitive(value: PushNotificationConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    return out
