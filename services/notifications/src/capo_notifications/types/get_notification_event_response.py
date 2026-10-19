"""Generated from Smithy shape ``com.amazonaws.notifications#GetNotificationEventResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.creation_time
    import capo_notifications.types.notification_configuration_arn
    import capo_notifications.types.notification_event_arn
    import capo_notifications.types.notification_event_schema


class GetNotificationEventResponse(TypedDict, closed=True):
    arn: "capo_notifications.types.notification_event_arn.NotificationEventArn"
    """<p>The ARN of the resource.</p>"""
    notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The ARN of the <code>NotificationConfiguration</code>.</p>"""
    creation_time: "capo_notifications.types.creation_time.CreationTime"
    """<p>The creation time of the <code>NotificationEvent</code>.</p>"""
    content: (
        "capo_notifications.types.notification_event_schema.NotificationEventSchema"
    )
    """<p>The content of the <code>NotificationEvent</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotificationEventResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["notificationConfigurationArn"] = value["notification_configuration_arn"]
    import capo_notifications.types.creation_time

    out["creationTime"] = capo_notifications.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import capo_notifications.types.notification_event_schema

    out["content"] = capo_notifications.types.notification_event_schema.serialize_json(
        value["content"]
    )
    return out


def deserialize_json(data: dict) -> GetNotificationEventResponse:
    out: GetNotificationEventResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("notificationConfigurationArn") is not None:
        out["notification_configuration_arn"] = data["notificationConfigurationArn"]
    else:
        out["notification_configuration_arn"] = ""
    if data.get("creationTime") is not None:
        import capo_notifications.types.creation_time

        out["creation_time"] = capo_notifications.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("content") is not None:
        import capo_notifications.types.notification_event_schema

        out["content"] = (
            capo_notifications.types.notification_event_schema.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("GetNotificationEventResponse.content required")
    return out
