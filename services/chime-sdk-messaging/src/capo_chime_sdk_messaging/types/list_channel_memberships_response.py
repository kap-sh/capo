"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelMembershipsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_membership_summary_list
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.next_token


class ListChannelMembershipsResponse(TypedDict, closed=True):
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    channel_memberships: NotRequired[
        "capo_chime_sdk_messaging.types.channel_membership_summary_list.ChannelMembershipSummaryList"
    ]
    """<p>The information for the requested channel memberships.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested channel memberships are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelMembershipsResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "channel_memberships" in value:
        import capo_chime_sdk_messaging.types.channel_membership_summary_list

        out["ChannelMemberships"] = (
            capo_chime_sdk_messaging.types.channel_membership_summary_list.serialize_json(
                value["channel_memberships"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelMembershipsResponse:
    out: ListChannelMembershipsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelArn") is not None:
        out["channel_arn"] = data["ChannelArn"]
    if data.get("ChannelMemberships") is not None:
        import capo_chime_sdk_messaging.types.channel_membership_summary_list

        out["channel_memberships"] = (
            capo_chime_sdk_messaging.types.channel_membership_summary_list.deserialize_json(
                data["ChannelMemberships"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListChannelMembershipsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_memberships" in value:
        import capo_chime_sdk_messaging.types.channel_membership_summary_list

        out["channel_memberships"] = (
            capo_chime_sdk_messaging.types.channel_membership_summary_list.redact_sensitive(
                value["channel_memberships"]
            )
        )
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
