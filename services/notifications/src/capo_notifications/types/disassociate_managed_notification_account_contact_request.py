"""Generated from Smithy shape ``com.amazonaws.notifications#DisassociateManagedNotificationAccountContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.account_contact_type
    import capo_notifications.types.managed_notification_configuration_os_arn


class DisassociateManagedNotificationAccountContactRequest(TypedDict, closed=True):
    contact_identifier: (
        "capo_notifications.types.account_contact_type.AccountContactType"
    )
    """<p>The unique value of an Account Contact Type to associate with the <code>ManagedNotificationConfiguration</code>.</p>"""
    managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to associate with the Account Contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateManagedNotificationAccountContactRequest) -> dict:
    out: dict = {}
    out["managedNotificationConfigurationArn"] = value[
        "managed_notification_configuration_arn"
    ]
    return out


def deserialize_json(
    data: dict,
) -> DisassociateManagedNotificationAccountContactRequest:
    out: DisassociateManagedNotificationAccountContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("managedNotificationConfigurationArn") is not None:
        out["managed_notification_configuration_arn"] = data[
            "managedNotificationConfigurationArn"
        ]
    else:
        out["managed_notification_configuration_arn"] = ""
    return out
