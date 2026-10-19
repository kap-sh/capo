"""Generated from Smithy shape ``com.amazonaws.notifications#AssociateManagedNotificationAccountContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.account_contact_type
    import capo_notifications.types.managed_notification_configuration_os_arn


class AssociateManagedNotificationAccountContactRequest(TypedDict, closed=True):
    contact_identifier: (
        "capo_notifications.types.account_contact_type.AccountContactType"
    )
    """<p>A unique value of an Account Contact Type to associate with the <code>ManagedNotificationConfiguration</code>.</p>"""
    managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to associate with the Account Contact.</p>"""
    is_sensitive_events_subscribed: NotRequired["bool"]
    """<p>Specifies whether this contact is subscribed to sensitive events. The <code>notifications:SubscribeSensitiveEvents</code> permission controls access to sensitive events. Defaults to false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateManagedNotificationAccountContactRequest) -> dict:
    out: dict = {}
    out["managedNotificationConfigurationArn"] = value[
        "managed_notification_configuration_arn"
    ]
    if "is_sensitive_events_subscribed" in value:
        out["isSensitiveEventsSubscribed"] = value["is_sensitive_events_subscribed"]
    return out


def deserialize_json(data: dict) -> AssociateManagedNotificationAccountContactRequest:
    out: AssociateManagedNotificationAccountContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("managedNotificationConfigurationArn") is not None:
        out["managed_notification_configuration_arn"] = data[
            "managedNotificationConfigurationArn"
        ]
    else:
        out["managed_notification_configuration_arn"] = ""
    if data.get("isSensitiveEventsSubscribed") is not None:
        out["is_sensitive_events_subscribed"] = data["isSensitiveEventsSubscribed"]
    return out
