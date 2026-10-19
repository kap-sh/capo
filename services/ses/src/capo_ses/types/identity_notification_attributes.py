"""Generated from Smithy shape ``com.amazonaws.ses#IdentityNotificationAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.enabled
    import capo_ses.types.notification_topic


class IdentityNotificationAttributes(TypedDict, closed=True):
    bounce_topic: "capo_ses.types.notification_topic.NotificationTopic"
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES publishes bounce notifications.</p>"""
    complaint_topic: "capo_ses.types.notification_topic.NotificationTopic"
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES publishes complaint notifications.</p>"""
    delivery_topic: "capo_ses.types.notification_topic.NotificationTopic"
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES publishes delivery notifications.</p>"""
    forwarding_enabled: "capo_ses.types.enabled.Enabled"
    """<p>Describes whether Amazon SES forwards bounce and complaint notifications as email. <code>true</code> indicates that Amazon SES forwards bounce and complaint notifications as email, while <code>false</code> indicates that bounce and complaint notifications are published only to the specified bounce and complaint Amazon SNS topics.</p>"""
    headers_in_bounce_notifications_enabled: "capo_ses.types.enabled.Enabled"
    """<p>Describes whether Amazon SES includes the original email headers in Amazon SNS notifications of type <code>Bounce</code>. A value of <code>true</code> specifies that Amazon SES includes headers in bounce notifications, and a value of <code>false</code> specifies that Amazon SES does not include headers in bounce notifications.</p>"""
    headers_in_complaint_notifications_enabled: "capo_ses.types.enabled.Enabled"
    """<p>Describes whether Amazon SES includes the original email headers in Amazon SNS notifications of type <code>Complaint</code>. A value of <code>true</code> specifies that Amazon SES includes headers in complaint notifications, and a value of <code>false</code> specifies that Amazon SES does not include headers in complaint notifications.</p>"""
    headers_in_delivery_notifications_enabled: "capo_ses.types.enabled.Enabled"
    """<p>Describes whether Amazon SES includes the original email headers in Amazon SNS notifications of type <code>Delivery</code>. A value of <code>true</code> specifies that Amazon SES includes headers in delivery notifications, and a value of <code>false</code> specifies that Amazon SES does not include headers in delivery notifications.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: IdentityNotificationAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}BounceTopic", str(value["bounce_topic"])))
    pairs.append((f"{key_prefix}ComplaintTopic", str(value["complaint_topic"])))
    pairs.append((f"{key_prefix}DeliveryTopic", str(value["delivery_topic"])))
    pairs.append(
        (
            f"{key_prefix}ForwardingEnabled",
            "true" if value.get("forwarding_enabled", False) else "false",
        )
    )
    pairs.append(
        (
            f"{key_prefix}HeadersInBounceNotificationsEnabled",
            "true"
            if value.get("headers_in_bounce_notifications_enabled", False)
            else "false",
        )
    )
    pairs.append(
        (
            f"{key_prefix}HeadersInComplaintNotificationsEnabled",
            "true"
            if value.get("headers_in_complaint_notifications_enabled", False)
            else "false",
        )
    )
    pairs.append(
        (
            f"{key_prefix}HeadersInDeliveryNotificationsEnabled",
            "true"
            if value.get("headers_in_delivery_notifications_enabled", False)
            else "false",
        )
    )


def deserialize_query(el: Element) -> IdentityNotificationAttributes:
    out: IdentityNotificationAttributes = {}  # type: ignore[typeddict-item]
    child_bounce_topic = el.find("BounceTopic")
    if child_bounce_topic is not None:
        out["bounce_topic"] = str(child_bounce_topic.text or "")
    else:
        out["bounce_topic"] = ""
    child_complaint_topic = el.find("ComplaintTopic")
    if child_complaint_topic is not None:
        out["complaint_topic"] = str(child_complaint_topic.text or "")
    else:
        out["complaint_topic"] = ""
    child_delivery_topic = el.find("DeliveryTopic")
    if child_delivery_topic is not None:
        out["delivery_topic"] = str(child_delivery_topic.text or "")
    else:
        out["delivery_topic"] = ""
    child_forwarding_enabled = el.find("ForwardingEnabled")
    if child_forwarding_enabled is not None:
        out["forwarding_enabled"] = (
            child_forwarding_enabled.text or ""
        ).lower() == "true"
    else:
        out["forwarding_enabled"] = False
    child_headers_in_bounce_notifications_enabled = el.find(
        "HeadersInBounceNotificationsEnabled"
    )
    if child_headers_in_bounce_notifications_enabled is not None:
        out["headers_in_bounce_notifications_enabled"] = (
            child_headers_in_bounce_notifications_enabled.text or ""
        ).lower() == "true"
    else:
        out["headers_in_bounce_notifications_enabled"] = False
    child_headers_in_complaint_notifications_enabled = el.find(
        "HeadersInComplaintNotificationsEnabled"
    )
    if child_headers_in_complaint_notifications_enabled is not None:
        out["headers_in_complaint_notifications_enabled"] = (
            child_headers_in_complaint_notifications_enabled.text or ""
        ).lower() == "true"
    else:
        out["headers_in_complaint_notifications_enabled"] = False
    child_headers_in_delivery_notifications_enabled = el.find(
        "HeadersInDeliveryNotificationsEnabled"
    )
    if child_headers_in_delivery_notifications_enabled is not None:
        out["headers_in_delivery_notifications_enabled"] = (
            child_headers_in_delivery_notifications_enabled.text or ""
        ).lower() == "true"
    else:
        out["headers_in_delivery_notifications_enabled"] = False
    return out
