"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#CreateChannelModeratorResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.identity


class CreateChannelModeratorResponse(TypedDict, closed=True):
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    channel_moderator: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>The ARNs of the channel and the moderator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelModeratorResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "channel_moderator" in value:
        import capo_chime_sdk_messaging.types.identity

        out["ChannelModerator"] = (
            capo_chime_sdk_messaging.types.identity.serialize_json(
                value["channel_moderator"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateChannelModeratorResponse:
    out: CreateChannelModeratorResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelArn") is not None:
        out["channel_arn"] = data["ChannelArn"]
    if data.get("ChannelModerator") is not None:
        import capo_chime_sdk_messaging.types.identity

        out["channel_moderator"] = (
            capo_chime_sdk_messaging.types.identity.deserialize_json(
                data["ChannelModerator"]
            )
        )
    return out


def redact_sensitive(value: CreateChannelModeratorResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_moderator" in value:
        import capo_chime_sdk_messaging.types.identity

        out["channel_moderator"] = (
            capo_chime_sdk_messaging.types.identity.redact_sensitive(
                value["channel_moderator"]
            )
        )
    return out
