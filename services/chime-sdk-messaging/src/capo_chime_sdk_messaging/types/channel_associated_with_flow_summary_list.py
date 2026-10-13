"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelAssociatedWithFlowSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_associated_with_flow_summary

ChannelAssociatedWithFlowSummaryList: TypeAlias = list[
    "capo_chime_sdk_messaging.types.channel_associated_with_flow_summary.ChannelAssociatedWithFlowSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelAssociatedWithFlowSummaryList) -> list:
    import capo_chime_sdk_messaging.types.channel_associated_with_flow_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_messaging.types.channel_associated_with_flow_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ChannelAssociatedWithFlowSummaryList:
    import capo_chime_sdk_messaging.types.channel_associated_with_flow_summary

    out: ChannelAssociatedWithFlowSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_messaging.types.channel_associated_with_flow_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ChannelAssociatedWithFlowSummaryList) -> list[Any]:
    import capo_chime_sdk_messaging.types.channel_associated_with_flow_summary

    return [
        capo_chime_sdk_messaging.types.channel_associated_with_flow_summary.redact_sensitive(
            item
        )
        for item in value
    ]
