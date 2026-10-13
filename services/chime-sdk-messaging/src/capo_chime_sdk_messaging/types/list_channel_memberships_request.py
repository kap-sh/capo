"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelMembershipsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_membership_type
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.max_results
    import capo_chime_sdk_messaging.types.next_token
    import capo_chime_sdk_messaging.types.sub_channel_id


class ListChannelMembershipsRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The maximum number of channel memberships that you want returned.</p>"""
    type: NotRequired[
        "capo_chime_sdk_messaging.types.channel_membership_type.ChannelMembershipType"
    ]
    """<p>The membership type of a user, <code>DEFAULT</code> or <code>HIDDEN</code>. Default members are returned as part of <code>ListChannelMemberships</code> if no type is specified. Hidden members are only returned if the type filter in <code>ListChannelMemberships</code> equals <code>HIDDEN</code>.</p>"""
    max_results: NotRequired["capo_chime_sdk_messaging.types.max_results.MaxResults"]
    """<p>The maximum number of channel memberships that you want returned.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested channel memberships are returned.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the request.</p> <note> <p>Only required when listing a user's memberships in a particular sub-channel of an elastic channel.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelMembershipsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChannelMembershipsRequest:
    out: ListChannelMembershipsRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListChannelMembershipsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
