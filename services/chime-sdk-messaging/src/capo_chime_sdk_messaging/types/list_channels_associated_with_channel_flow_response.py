"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelsAssociatedWithChannelFlowResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_associated_with_flow_summary_list
    import capo_chime_sdk_messaging.types.next_token


class ListChannelsAssociatedWithChannelFlowResponse(TypedDict, closed=True):
    channels: NotRequired[
        "capo_chime_sdk_messaging.types.channel_associated_with_flow_summary_list.ChannelAssociatedWithFlowSummaryList"
    ]
    """<p>The information about each channel.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested channels are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsAssociatedWithChannelFlowResponse) -> dict:
    out: dict = {}
    if "channels" in value:
        import capo_chime_sdk_messaging.types.channel_associated_with_flow_summary_list

        out["Channels"] = (
            capo_chime_sdk_messaging.types.channel_associated_with_flow_summary_list.serialize_json(
                value["channels"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelsAssociatedWithChannelFlowResponse:
    out: ListChannelsAssociatedWithChannelFlowResponse = {}  # type: ignore[typeddict-item]
    if data.get("Channels") is not None:
        import capo_chime_sdk_messaging.types.channel_associated_with_flow_summary_list

        out["channels"] = (
            capo_chime_sdk_messaging.types.channel_associated_with_flow_summary_list.deserialize_json(
                data["Channels"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(
    value: ListChannelsAssociatedWithChannelFlowResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channels" in value:
        import capo_chime_sdk_messaging.types.channel_associated_with_flow_summary_list

        out["channels"] = (
            capo_chime_sdk_messaging.types.channel_associated_with_flow_summary_list.redact_sensitive(
                value["channels"]
            )
        )
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
