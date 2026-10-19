"""Generated from Smithy shape ``com.amazonaws.ses#SetIdentityHeadersInNotificationsEnabledRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.enabled
    import capo_ses.types.identity
    import capo_ses.types.notification_type


class SetIdentityHeadersInNotificationsEnabledRequest(TypedDict, closed=True):
    identity: "capo_ses.types.identity.Identity"
    """<p>The identity for which to enable or disable headers in notifications. Examples: <code>user@example.com</code>, <code>example.com</code>.</p>"""
    notification_type: "capo_ses.types.notification_type.NotificationType"
    """<p>The notification type for which to enable or disable headers in notifications. </p>"""
    enabled: "capo_ses.types.enabled.Enabled"
    """<p>Sets whether Amazon SES includes the original email headers in Amazon SNS notifications of the specified notification type. A value of <code>true</code> specifies that Amazon SES includes headers in notifications, and a value of <code>false</code> specifies that Amazon SES does not include headers in notifications.</p> <p>This value can only be set when <code>NotificationType</code> is already set to use a particular Amazon SNS topic.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetIdentityHeadersInNotificationsEnabledRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Identity", str(value["identity"])))
    import capo_ses.types.notification_type

    capo_ses.types.notification_type.serialize_query(
        value["notification_type"], pairs, f"{key_prefix}NotificationType"
    )
    pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))


def deserialize_query(el: Element) -> SetIdentityHeadersInNotificationsEnabledRequest:
    out: SetIdentityHeadersInNotificationsEnabledRequest = {}  # type: ignore[typeddict-item]
    child_identity = el.find("Identity")
    if child_identity is not None:
        out["identity"] = str(child_identity.text or "")
    else:
        out["identity"] = ""
    child_notification_type = el.find("NotificationType")
    if child_notification_type is not None:
        import capo_ses.types.notification_type

        out["notification_type"] = capo_ses.types.notification_type.deserialize_query(
            child_notification_type
        )
    else:
        import typing

        out["notification_type"] = typing.cast(
            "capo_ses.types.notification_type.NotificationType", ""
        )
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    return out
