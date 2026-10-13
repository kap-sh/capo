"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelModeratorsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_moderator_summary_list
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.next_token


class ListChannelModeratorsResponse(TypedDict, closed=True):
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested moderators are returned.</p>"""
    channel_moderators: NotRequired[
        "capo_chime_sdk_messaging.types.channel_moderator_summary_list.ChannelModeratorSummaryList"
    ]
    """<p>The information about and names of each moderator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelModeratorsResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "channel_moderators" in value:
        import capo_chime_sdk_messaging.types.channel_moderator_summary_list

        out["ChannelModerators"] = (
            capo_chime_sdk_messaging.types.channel_moderator_summary_list.serialize_json(
                value["channel_moderators"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListChannelModeratorsResponse:
    out: ListChannelModeratorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelArn") is not None:
        out["channel_arn"] = data["ChannelArn"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ChannelModerators") is not None:
        import capo_chime_sdk_messaging.types.channel_moderator_summary_list

        out["channel_moderators"] = (
            capo_chime_sdk_messaging.types.channel_moderator_summary_list.deserialize_json(
                data["ChannelModerators"]
            )
        )
    return out


def redact_sensitive(value: ListChannelModeratorsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    if "channel_moderators" in value:
        import capo_chime_sdk_messaging.types.channel_moderator_summary_list

        out["channel_moderators"] = (
            capo_chime_sdk_messaging.types.channel_moderator_summary_list.redact_sensitive(
                value["channel_moderators"]
            )
        )
    return out
