"""Generated from Smithy shape ``com.amazonaws.notifications#GetManagedNotificationEventResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.creation_time
    import capo_notifications.types.managed_notification_configuration_os_arn
    import capo_notifications.types.managed_notification_event
    import capo_notifications.types.managed_notification_event_arn


class GetManagedNotificationEventResponse(TypedDict, closed=True):
    arn: "capo_notifications.types.managed_notification_event_arn.ManagedNotificationEventArn"
    """<p>The ARN of the resource.</p>"""
    managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The ARN of the <code>ManagedNotificationConfiguration</code>.</p>"""
    creation_time: "capo_notifications.types.creation_time.CreationTime"
    """<p>The creation time of the <code>ManagedNotificationEvent</code>.</p>"""
    content: (
        "capo_notifications.types.managed_notification_event.ManagedNotificationEvent"
    )
    """<p>The content of the <code>ManagedNotificationEvent</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedNotificationEventResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["managedNotificationConfigurationArn"] = value[
        "managed_notification_configuration_arn"
    ]
    import capo_notifications.types.creation_time

    out["creationTime"] = capo_notifications.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import capo_notifications.types.managed_notification_event

    out["content"] = capo_notifications.types.managed_notification_event.serialize_json(
        value["content"]
    )
    return out


def deserialize_json(data: dict) -> GetManagedNotificationEventResponse:
    out: GetManagedNotificationEventResponse = {}  # type: ignore[typeddict-item]
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
        import capo_notifications.types.managed_notification_event

        out["content"] = (
            capo_notifications.types.managed_notification_event.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError(
            "GetManagedNotificationEventResponse.content required"
        )
    return out


def redact_sensitive(value: GetManagedNotificationEventResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_notifications.types.managed_notification_event

        out["content"] = (
            capo_notifications.types.managed_notification_event.redact_sensitive(
                value["content"]
            )
        )
    return out
