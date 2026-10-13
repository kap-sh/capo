"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMembershipSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_membership_summary

ChannelMembershipSummaryList: TypeAlias = list[
    "capo_chime_sdk_messaging.types.channel_membership_summary.ChannelMembershipSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMembershipSummaryList) -> list:
    import capo_chime_sdk_messaging.types.channel_membership_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_messaging.types.channel_membership_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ChannelMembershipSummaryList:
    import capo_chime_sdk_messaging.types.channel_membership_summary

    out: ChannelMembershipSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_messaging.types.channel_membership_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ChannelMembershipSummaryList) -> list[Any]:
    import capo_chime_sdk_messaging.types.channel_membership_summary

    return [
        capo_chime_sdk_messaging.types.channel_membership_summary.redact_sensitive(item)
        for item in value
    ]
