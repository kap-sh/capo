"""Generated from Smithy shape ``com.amazonaws.notifications#ManagedNotificationChannelAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.channel_association_override_option
    import capo_notifications.types.channel_type


class ManagedNotificationChannelAssociationSummary(TypedDict, closed=True):
    channel_identifier: "str"
    """<p>The unique identifier for the notification channel.</p>"""
    channel_type: "capo_notifications.types.channel_type.ChannelType"
    """<p>The type of notification channel used for message delivery.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>ACCOUNT_CONTACT</code> </p> <ul> <li> <p>Delivers notifications to Account Managed contacts through the User Notification Service.</p> </li> </ul> </li> <li> <p> <code>MOBILE</code> </p> <ul> <li> <p>Delivers notifications through the Amazon Web Services Console Mobile Application to mobile devices.</p> </li> </ul> </li> <li> <p> <code>CHATBOT</code> </p> <ul> <li> <p>Delivers notifications through Amazon Q Developer in chat applications to collaboration platforms (Slack, Chime).</p> </li> </ul> </li> <li> <p> <code>EMAIL</code> </p> <ul> <li> <p>Delivers notifications to email addresses.</p> </li> </ul> </li> </ul> </li> </ul>"""
    override_option: NotRequired[
        "capo_notifications.types.channel_association_override_option.ChannelAssociationOverrideOption"
    ]
    """<p>Controls whether users can modify channel associations for a notification configuration.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>ENABLED</code> </p> <ul> <li> <p>Users can associate or disassociate channels with the notification configuration.</p> </li> </ul> </li> <li> <p> <code>DISABLED</code> </p> <ul> <li> <p>Users cannot associate or disassociate channels with the notification configuration.</p> </li> </ul> </li> </ul> </li> </ul>"""
    is_sensitive_events_subscribed: NotRequired["bool"]
    """<p>Specifies whether this channel association is subscribed to sensitive events. Defaults to false for associations created without the flag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedNotificationChannelAssociationSummary) -> dict:
    out: dict = {}
    out["channelIdentifier"] = value["channel_identifier"]
    import capo_notifications.types.channel_type

    out["channelType"] = capo_notifications.types.channel_type.serialize_json(
        value["channel_type"]
    )
    if "override_option" in value:
        out["overrideOption"] = value["override_option"]
    if "is_sensitive_events_subscribed" in value:
        out["isSensitiveEventsSubscribed"] = value["is_sensitive_events_subscribed"]
    return out


def deserialize_json(data: dict) -> ManagedNotificationChannelAssociationSummary:
    out: ManagedNotificationChannelAssociationSummary = {}  # type: ignore[typeddict-item]
    if data.get("channelIdentifier") is not None:
        out["channel_identifier"] = data["channelIdentifier"]
    else:
        out["channel_identifier"] = ""
    if data.get("channelType") is not None:
        import capo_notifications.types.channel_type

        out["channel_type"] = capo_notifications.types.channel_type.deserialize_json(
            data["channelType"]
        )
    else:
        import typing

        out["channel_type"] = typing.cast(
            "capo_notifications.types.channel_type.ChannelType", ""
        )
    if data.get("overrideOption") is not None:
        out["override_option"] = data["overrideOption"]
    if data.get("isSensitiveEventsSubscribed") is not None:
        out["is_sensitive_events_subscribed"] = data["isSensitiveEventsSubscribed"]
    return out
