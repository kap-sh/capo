"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DescribeChannelMembershipForAppInstanceUserResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary


class DescribeChannelMembershipForAppInstanceUserResponse(TypedDict, closed=True):
    channel_membership: NotRequired[
        "capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary.ChannelMembershipForAppInstanceUserSummary"
    ]
    """<p>The channel to which a user belongs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelMembershipForAppInstanceUserResponse) -> dict:
    out: dict = {}
    if "channel_membership" in value:
        import capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary

        out["ChannelMembership"] = (
            capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary.serialize_json(
                value["channel_membership"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeChannelMembershipForAppInstanceUserResponse:
    out: DescribeChannelMembershipForAppInstanceUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelMembership") is not None:
        import capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary

        out["channel_membership"] = (
            capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary.deserialize_json(
                data["ChannelMembership"]
            )
        )
    return out


def redact_sensitive(
    value: DescribeChannelMembershipForAppInstanceUserResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_membership" in value:
        import capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary

        out["channel_membership"] = (
            capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary.redact_sensitive(
                value["channel_membership"]
            )
        )
    return out
