"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMembershipForAppInstanceUserSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.app_instance_user_membership_summary
    import capo_chime_sdk_messaging.types.channel_summary


class ChannelMembershipForAppInstanceUserSummary(TypedDict, closed=True):
    channel_summary: NotRequired[
        "capo_chime_sdk_messaging.types.channel_summary.ChannelSummary"
    ]
    """<p>Returns the channel data for an <code>AppInstance</code>.</p>"""
    app_instance_user_membership_summary: NotRequired[
        "capo_chime_sdk_messaging.types.app_instance_user_membership_summary.AppInstanceUserMembershipSummary"
    ]
    """<p>Returns the channel membership data for an <code>AppInstance</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMembershipForAppInstanceUserSummary) -> dict:
    out: dict = {}
    if "channel_summary" in value:
        import capo_chime_sdk_messaging.types.channel_summary

        out["ChannelSummary"] = (
            capo_chime_sdk_messaging.types.channel_summary.serialize_json(
                value["channel_summary"]
            )
        )
    if "app_instance_user_membership_summary" in value:
        import capo_chime_sdk_messaging.types.app_instance_user_membership_summary

        out["AppInstanceUserMembershipSummary"] = (
            capo_chime_sdk_messaging.types.app_instance_user_membership_summary.serialize_json(
                value["app_instance_user_membership_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChannelMembershipForAppInstanceUserSummary:
    out: ChannelMembershipForAppInstanceUserSummary = {}  # type: ignore[typeddict-item]
    if data.get("ChannelSummary") is not None:
        import capo_chime_sdk_messaging.types.channel_summary

        out["channel_summary"] = (
            capo_chime_sdk_messaging.types.channel_summary.deserialize_json(
                data["ChannelSummary"]
            )
        )
    if data.get("AppInstanceUserMembershipSummary") is not None:
        import capo_chime_sdk_messaging.types.app_instance_user_membership_summary

        out["app_instance_user_membership_summary"] = (
            capo_chime_sdk_messaging.types.app_instance_user_membership_summary.deserialize_json(
                data["AppInstanceUserMembershipSummary"]
            )
        )
    return out


def redact_sensitive(
    value: ChannelMembershipForAppInstanceUserSummary,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_summary" in value:
        import capo_chime_sdk_messaging.types.channel_summary

        out["channel_summary"] = (
            capo_chime_sdk_messaging.types.channel_summary.redact_sensitive(
                value["channel_summary"]
            )
        )
    return out
