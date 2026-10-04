"""Generated from Smithy shape ``com.amazonaws.connect#SendInAppNotificationActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.configurable_notification_priority
    import capo_connect.types.notification_content
    import capo_connect.types.notification_recipient_type


class SendInAppNotificationActionDefinition(TypedDict, closed=True):
    content: "capo_connect.types.notification_content.NotificationContent"
    """<p>Notification content. Supports variable injection. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html">JSONPath reference</a> in the <i>Connect Customer Administrators Guide</i>.</p>"""
    recipient: (
        "capo_connect.types.notification_recipient_type.NotificationRecipientType"
    )
    """<p>Notification recipient.</p>"""
    exclusion: NotRequired[
        "capo_connect.types.notification_recipient_type.NotificationRecipientType"
    ]
    """<p>Recipients to exclude from notification.</p>"""
    priority: NotRequired[
        "capo_connect.types.configurable_notification_priority.ConfigurableNotificationPriority"
    ]
    """<p>Notification priority.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendInAppNotificationActionDefinition) -> dict:
    out: dict = {}
    import capo_connect.types.notification_content

    out["Content"] = capo_connect.types.notification_content.serialize_json(
        value["content"]
    )
    import capo_connect.types.notification_recipient_type

    out["Recipient"] = capo_connect.types.notification_recipient_type.serialize_json(
        value["recipient"]
    )
    if "exclusion" in value:
        import capo_connect.types.notification_recipient_type

        out["Exclusion"] = (
            capo_connect.types.notification_recipient_type.serialize_json(
                value["exclusion"]
            )
        )
    if "priority" in value:
        import capo_connect.types.configurable_notification_priority

        out["Priority"] = (
            capo_connect.types.configurable_notification_priority.serialize_json(
                value["priority"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendInAppNotificationActionDefinition:
    out: SendInAppNotificationActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        import capo_connect.types.notification_content

        out["content"] = capo_connect.types.notification_content.deserialize_json(
            data["Content"]
        )
    else:
        raise DeserializationError(
            "SendInAppNotificationActionDefinition.content required"
        )
    if data.get("Recipient") is not None:
        import capo_connect.types.notification_recipient_type

        out["recipient"] = (
            capo_connect.types.notification_recipient_type.deserialize_json(
                data["Recipient"]
            )
        )
    else:
        raise DeserializationError(
            "SendInAppNotificationActionDefinition.recipient required"
        )
    if data.get("Exclusion") is not None:
        import capo_connect.types.notification_recipient_type

        out["exclusion"] = (
            capo_connect.types.notification_recipient_type.deserialize_json(
                data["Exclusion"]
            )
        )
    if data.get("Priority") is not None:
        import capo_connect.types.configurable_notification_priority

        out["priority"] = (
            capo_connect.types.configurable_notification_priority.deserialize_json(
                data["Priority"]
            )
        )
    return out
