"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelBanSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_ban_summary

ChannelBanSummaryList: TypeAlias = list[
    "capo_chime_sdk_messaging.types.channel_ban_summary.ChannelBanSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelBanSummaryList) -> list:
    import capo_chime_sdk_messaging.types.channel_ban_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_messaging.types.channel_ban_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ChannelBanSummaryList:
    import capo_chime_sdk_messaging.types.channel_ban_summary

    out: ChannelBanSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_messaging.types.channel_ban_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ChannelBanSummaryList) -> list[Any]:
    import capo_chime_sdk_messaging.types.channel_ban_summary

    return [
        capo_chime_sdk_messaging.types.channel_ban_summary.redact_sensitive(item)
        for item in value
    ]
