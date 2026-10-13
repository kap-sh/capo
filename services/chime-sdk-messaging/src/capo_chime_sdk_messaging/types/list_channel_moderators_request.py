"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelModeratorsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.max_results
    import capo_chime_sdk_messaging.types.next_token


class ListChannelModeratorsRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    max_results: NotRequired["capo_chime_sdk_messaging.types.max_results.MaxResults"]
    """<p>The maximum number of moderators that you want returned.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested moderators are returned.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelModeratorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChannelModeratorsRequest:
    out: ListChannelModeratorsRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListChannelModeratorsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
