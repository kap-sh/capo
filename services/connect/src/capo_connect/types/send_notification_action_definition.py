"""Generated from Smithy shape ``com.amazonaws.connect#SendNotificationActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.content
    import capo_connect.types.notification_content_type
    import capo_connect.types.notification_delivery_type
    import capo_connect.types.notification_recipient_type
    import capo_connect.types.subject


class SendNotificationActionDefinition(TypedDict, closed=True):
    delivery_method: (
        "capo_connect.types.notification_delivery_type.NotificationDeliveryType"
    )
    """<p>Notification delivery method.</p>"""
    subject: NotRequired["capo_connect.types.subject.Subject"]
    """<p>The subject of the email if the delivery method is <code>EMAIL</code>. Supports variable injection. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html">JSONPath reference</a> in the <i>Connect Customer Administrators Guide</i>.</p>"""
    content: "capo_connect.types.content.Content"
    """<p>Notification content. Supports variable injection. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html">JSONPath reference</a> in the <i>Connect Customer Administrators Guide</i>.</p>"""
    content_type: "capo_connect.types.notification_content_type.NotificationContentType"
    """<p>Content type format.</p>"""
    recipient: (
        "capo_connect.types.notification_recipient_type.NotificationRecipientType"
    )
    """<p>Notification recipient.</p>"""
    exclusion: NotRequired[
        "capo_connect.types.notification_recipient_type.NotificationRecipientType"
    ]
    """<p>Recipients to exclude from notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendNotificationActionDefinition) -> dict:
    out: dict = {}
    import capo_connect.types.notification_delivery_type

    out["DeliveryMethod"] = (
        capo_connect.types.notification_delivery_type.serialize_json(
            value["delivery_method"]
        )
    )
    if "subject" in value:
        out["Subject"] = value["subject"]
    out["Content"] = value["content"]
    import capo_connect.types.notification_content_type

    out["ContentType"] = capo_connect.types.notification_content_type.serialize_json(
        value["content_type"]
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
    return out


def deserialize_json(data: dict) -> SendNotificationActionDefinition:
    out: SendNotificationActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryMethod") is not None:
        import capo_connect.types.notification_delivery_type

        out["delivery_method"] = (
            capo_connect.types.notification_delivery_type.deserialize_json(
                data["DeliveryMethod"]
            )
        )
    else:
        raise DeserializationError(
            "SendNotificationActionDefinition.delivery_method required"
        )
    if data.get("Subject") is not None:
        out["subject"] = data["Subject"]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("SendNotificationActionDefinition.content required")
    if data.get("ContentType") is not None:
        import capo_connect.types.notification_content_type

        out["content_type"] = (
            capo_connect.types.notification_content_type.deserialize_json(
                data["ContentType"]
            )
        )
    else:
        raise DeserializationError(
            "SendNotificationActionDefinition.content_type required"
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
            "SendNotificationActionDefinition.recipient required"
        )
    if data.get("Exclusion") is not None:
        import capo_connect.types.notification_recipient_type

        out["exclusion"] = (
            capo_connect.types.notification_recipient_type.deserialize_json(
                data["Exclusion"]
            )
        )
    return out
