"""Generated from Smithy shape ``com.amazonaws.notifications#UpdateManagedNotificationChannelAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.managed_notification_channel_identifier
    import capo_notifications.types.managed_notification_configuration_os_arn


class UpdateManagedNotificationChannelAssociationRequest(TypedDict, closed=True):
    managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> whose Channel association property you want to update.</p>"""
    channel_identifier: "capo_notifications.types.managed_notification_channel_identifier.ManagedNotificationChannelIdentifier"
    """<p>The identifier of the channel association to update. You can specify one of the following:</p> <ul> <li> <p>An Account contact identifier.</p> </li> <li> <p>A Channel ARN.</p> </li> </ul>"""
    is_sensitive_events_subscribed: NotRequired["bool"]
    """<p>Specifies whether the association is subscribed to sensitive events. The <code>notifications:SubscribeSensitiveEvents</code> permission controls access to sensitive events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateManagedNotificationChannelAssociationRequest) -> dict:
    out: dict = {}
    out["managedNotificationConfigurationArn"] = value[
        "managed_notification_configuration_arn"
    ]
    out["channelIdentifier"] = value["channel_identifier"]
    if "is_sensitive_events_subscribed" in value:
        out["isSensitiveEventsSubscribed"] = value["is_sensitive_events_subscribed"]
    return out


def deserialize_json(data: dict) -> UpdateManagedNotificationChannelAssociationRequest:
    out: UpdateManagedNotificationChannelAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("managedNotificationConfigurationArn") is not None:
        out["managed_notification_configuration_arn"] = data[
            "managedNotificationConfigurationArn"
        ]
    else:
        out["managed_notification_configuration_arn"] = ""
    if data.get("channelIdentifier") is not None:
        out["channel_identifier"] = data["channelIdentifier"]
    else:
        out["channel_identifier"] = ""
    if data.get("isSensitiveEventsSubscribed") is not None:
        out["is_sensitive_events_subscribed"] = data["isSensitiveEventsSubscribed"]
    return out
