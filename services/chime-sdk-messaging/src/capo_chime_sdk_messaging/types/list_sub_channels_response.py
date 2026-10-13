"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListSubChannelsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.next_token
    import capo_chime_sdk_messaging.types.sub_channel_summary_list


class ListSubChannelsResponse(TypedDict, closed=True):
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of elastic channel.</p>"""
    sub_channels: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_summary_list.SubChannelSummaryList"
    ]
    """<p>The information about each sub-channel.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested sub-channels are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubChannelsResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "sub_channels" in value:
        import capo_chime_sdk_messaging.types.sub_channel_summary_list

        out["SubChannels"] = (
            capo_chime_sdk_messaging.types.sub_channel_summary_list.serialize_json(
                value["sub_channels"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSubChannelsResponse:
    out: ListSubChannelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelArn") is not None:
        out["channel_arn"] = data["ChannelArn"]
    if data.get("SubChannels") is not None:
        import capo_chime_sdk_messaging.types.sub_channel_summary_list

        out["sub_channels"] = (
            capo_chime_sdk_messaging.types.sub_channel_summary_list.deserialize_json(
                data["SubChannels"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListSubChannelsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
