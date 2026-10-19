"""Generated from Smithy shape ``com.amazonaws.notifications#AssociateManagedNotificationAdditionalChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.channel_arn
    import capo_notifications.types.managed_notification_configuration_os_arn


class AssociateManagedNotificationAdditionalChannelRequest(TypedDict, closed=True):
    channel_arn: "capo_notifications.types.channel_arn.ChannelArn"
    """<p>The Amazon Resource Name (ARN) of the Channel to associate with the <code>ManagedNotificationConfiguration</code>.</p> <p>Supported ARNs include Amazon Q Developer in chat applications, the Console Mobile Application, and email (notifications-contacts).</p>"""
    managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to associate with the additional Channel.</p>"""
    is_sensitive_events_subscribed: NotRequired["bool"]
    """<p>Specifies whether this channel is subscribed to sensitive events. The <code>notifications:SubscribeSensitiveEvents</code> permission controls access to sensitive events. Defaults to false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateManagedNotificationAdditionalChannelRequest) -> dict:
    out: dict = {}
    out["managedNotificationConfigurationArn"] = value[
        "managed_notification_configuration_arn"
    ]
    if "is_sensitive_events_subscribed" in value:
        out["isSensitiveEventsSubscribed"] = value["is_sensitive_events_subscribed"]
    return out


def deserialize_json(
    data: dict,
) -> AssociateManagedNotificationAdditionalChannelRequest:
    out: AssociateManagedNotificationAdditionalChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("managedNotificationConfigurationArn") is not None:
        out["managed_notification_configuration_arn"] = data[
            "managedNotificationConfigurationArn"
        ]
    else:
        out["managed_notification_configuration_arn"] = ""
    if data.get("isSensitiveEventsSubscribed") is not None:
        out["is_sensitive_events_subscribed"] = data["isSensitiveEventsSubscribed"]
    return out
