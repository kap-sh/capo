"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_summary

ChannelSummaryList: TypeAlias = list[
    "capo_chime_sdk_messaging.types.channel_summary.ChannelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelSummaryList) -> list:
    import capo_chime_sdk_messaging.types.channel_summary

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_messaging.types.channel_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChannelSummaryList:
    import capo_chime_sdk_messaging.types.channel_summary

    out: ChannelSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_messaging.types.channel_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ChannelSummaryList) -> list[Any]:
    import capo_chime_sdk_messaging.types.channel_summary

    return [
        capo_chime_sdk_messaging.types.channel_summary.redact_sensitive(item)
        for item in value
    ]
