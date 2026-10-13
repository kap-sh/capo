"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListSubChannelsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.max_results
    import capo_chime_sdk_messaging.types.next_token


class ListSubChannelsRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of elastic channel.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The <code>AppInstanceUserArn</code> of the user making the API call.</p>"""
    max_results: NotRequired["capo_chime_sdk_messaging.types.max_results.MaxResults"]
    """<p>The maximum number of sub-channels that you want to return.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested sub-channels are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubChannelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSubChannelsRequest:
    out: ListSubChannelsRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListSubChannelsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
