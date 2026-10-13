"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelMessagesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_message_summary_list
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.next_token
    import capo_chime_sdk_messaging.types.sub_channel_id


class ListChannelMessagesResponse(TypedDict, closed=True):
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel containing the requested messages.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested messages are returned.</p>"""
    channel_messages: NotRequired[
        "capo_chime_sdk_messaging.types.channel_message_summary_list.ChannelMessageSummaryList"
    ]
    """<p>The information about, and content of, each requested message.</p>"""
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelMessagesResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "channel_messages" in value:
        import capo_chime_sdk_messaging.types.channel_message_summary_list

        out["ChannelMessages"] = (
            capo_chime_sdk_messaging.types.channel_message_summary_list.serialize_json(
                value["channel_messages"]
            )
        )
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    return out


def deserialize_json(data: dict) -> ListChannelMessagesResponse:
    out: ListChannelMessagesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelArn") is not None:
        out["channel_arn"] = data["ChannelArn"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ChannelMessages") is not None:
        import capo_chime_sdk_messaging.types.channel_message_summary_list

        out["channel_messages"] = (
            capo_chime_sdk_messaging.types.channel_message_summary_list.deserialize_json(
                data["ChannelMessages"]
            )
        )
    if data.get("SubChannelId") is not None:
        out["sub_channel_id"] = data["SubChannelId"]
    return out


def redact_sensitive(value: ListChannelMessagesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    if "channel_messages" in value:
        import capo_chime_sdk_messaging.types.channel_message_summary_list

        out["channel_messages"] = (
            capo_chime_sdk_messaging.types.channel_message_summary_list.redact_sensitive(
                value["channel_messages"]
            )
        )
    return out
