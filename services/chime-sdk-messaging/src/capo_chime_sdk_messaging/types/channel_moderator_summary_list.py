"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelModeratorSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_moderator_summary

ChannelModeratorSummaryList: TypeAlias = list[
    "capo_chime_sdk_messaging.types.channel_moderator_summary.ChannelModeratorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelModeratorSummaryList) -> list:
    import capo_chime_sdk_messaging.types.channel_moderator_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_messaging.types.channel_moderator_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ChannelModeratorSummaryList:
    import capo_chime_sdk_messaging.types.channel_moderator_summary

    out: ChannelModeratorSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_messaging.types.channel_moderator_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ChannelModeratorSummaryList) -> list[Any]:
    import capo_chime_sdk_messaging.types.channel_moderator_summary

    return [
        capo_chime_sdk_messaging.types.channel_moderator_summary.redact_sensitive(item)
        for item in value
    ]
