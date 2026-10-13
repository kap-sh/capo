"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMembershipForAppInstanceUserSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary

ChannelMembershipForAppInstanceUserSummaryList: TypeAlias = list[
    "capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary.ChannelMembershipForAppInstanceUserSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMembershipForAppInstanceUserSummaryList) -> list:
    import capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ChannelMembershipForAppInstanceUserSummaryList:
    import capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary

    out: ChannelMembershipForAppInstanceUserSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(
    value: ChannelMembershipForAppInstanceUserSummaryList,
) -> list[Any]:
    import capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary

    return [
        capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary.redact_sensitive(
            item
        )
        for item in value
    ]
