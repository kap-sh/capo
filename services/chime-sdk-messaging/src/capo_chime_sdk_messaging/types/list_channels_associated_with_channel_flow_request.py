"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelsAssociatedWithChannelFlowRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.max_results
    import capo_chime_sdk_messaging.types.next_token


class ListChannelsAssociatedWithChannelFlowRequest(TypedDict, closed=True):
    channel_flow_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel flow.</p>"""
    max_results: NotRequired["capo_chime_sdk_messaging.types.max_results.MaxResults"]
    """<p>The maximum number of channels that you want to return.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested channels are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsAssociatedWithChannelFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChannelsAssociatedWithChannelFlowRequest:
    out: ListChannelsAssociatedWithChannelFlowRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(
    value: ListChannelsAssociatedWithChannelFlowRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
