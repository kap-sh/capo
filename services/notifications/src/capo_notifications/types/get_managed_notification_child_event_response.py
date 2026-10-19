"""Generated from Smithy shape ``com.amazonaws.notifications#GetManagedNotificationChildEventResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.creation_time
    import capo_notifications.types.managed_notification_child_event
    import capo_notifications.types.managed_notification_child_event_arn
    import capo_notifications.types.managed_notification_configuration_os_arn


class GetManagedNotificationChildEventResponse(TypedDict, closed=True):
    arn: "capo_notifications.types.managed_notification_child_event_arn.ManagedNotificationChildEventArn"
    """<p>The ARN of the resource.</p>"""
    managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> associated with the <code>ManagedNotificationChildEvent</code>.</p>"""
    creation_time: "capo_notifications.types.creation_time.CreationTime"
    """<p>The creation time of the <code>ManagedNotificationChildEvent</code>.</p>"""
    content: "capo_notifications.types.managed_notification_child_event.ManagedNotificationChildEvent"
    """<p>The content of the <code>ManagedNotificationChildEvent</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedNotificationChildEventResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["managedNotificationConfigurationArn"] = value[
        "managed_notification_configuration_arn"
    ]
    import capo_notifications.types.creation_time

    out["creationTime"] = capo_notifications.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import capo_notifications.types.managed_notification_child_event

    out["content"] = (
        capo_notifications.types.managed_notification_child_event.serialize_json(
            value["content"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetManagedNotificationChildEventResponse:
    out: GetManagedNotificationChildEventResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("managedNotificationConfigurationArn") is not None:
        out["managed_notification_configuration_arn"] = data[
            "managedNotificationConfigurationArn"
        ]
    else:
        out["managed_notification_configuration_arn"] = ""
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
        import capo_notifications.types.managed_notification_child_event

        out["content"] = (
            capo_notifications.types.managed_notification_child_event.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError(
            "GetManagedNotificationChildEventResponse.content required"
        )
    return out
