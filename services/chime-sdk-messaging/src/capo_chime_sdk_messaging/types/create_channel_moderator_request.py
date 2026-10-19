"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#CreateChannelModeratorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn


class CreateChannelModeratorRequest(TypedDict, closed=True):
    channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel.</p>"""
    channel_moderator_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The <code>AppInstanceUserArn</code> of the moderator.</p>"""
    chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelModeratorRequest) -> dict:
    out: dict = {}
    out["ChannelModeratorArn"] = value["channel_moderator_arn"]
    return out


def deserialize_json(data: dict) -> CreateChannelModeratorRequest:
    out: CreateChannelModeratorRequest = {}  # type: ignore[typeddict-item]
    if data.get("ChannelModeratorArn") is not None:
        out["channel_moderator_arn"] = data["ChannelModeratorArn"]
    else:
        out["channel_moderator_arn"] = ""
    return out
