"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelMessagesRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.max_results
    import capo_chime_sdk_messaging.types.next_token
    import capo_chime_sdk_messaging.types.sort_order
    import capo_chime_sdk_messaging.types.sub_channel_id
    import capo_chime_sdk_messaging.types.timestamp


class ListChannelMessagesRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    sort_order: NotRequired["capo_chime_sdk_messaging.types.sort_order.SortOrder"]
    """<p>The order in which you want messages sorted. Default is Descending, based on time created.</p>"""
    not_before: NotRequired["capo_chime_sdk_messaging.types.timestamp.Timestamp"]
    """<p>The initial or starting time stamp for your requested messages.</p>"""
    not_after: NotRequired["capo_chime_sdk_messaging.types.timestamp.Timestamp"]
    """<p>The final or ending time stamp for your requested messages.</p>"""
    max_results: NotRequired["capo_chime_sdk_messaging.types.max_results.MaxResults"]
    """<p>The maximum number of messages that you want returned.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested messages are returned.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the request.</p> <note> <p>Only required when listing the messages in a SubChannel that the user belongs to.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelMessagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChannelMessagesRequest:
    out: ListChannelMessagesRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListChannelMessagesRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
