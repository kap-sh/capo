"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DescribeChannelModeratorResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_moderator


class DescribeChannelModeratorResponse(TypedDict, closed=True):
    channel_moderator: NotRequired[
        "capo_chime_sdk_messaging.types.channel_moderator.ChannelModerator"
    ]
    """<p>The details of the channel moderator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelModeratorResponse) -> dict:
    out: dict = {}
    if "channel_moderator" in value:
        import capo_chime_sdk_messaging.types.channel_moderator

        out["ChannelModerator"] = (
            capo_chime_sdk_messaging.types.channel_moderator.serialize_json(
                value["channel_moderator"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeChannelModeratorResponse:
    out: DescribeChannelModeratorResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelModerator") is not None:
        import capo_chime_sdk_messaging.types.channel_moderator

        out["channel_moderator"] = (
            capo_chime_sdk_messaging.types.channel_moderator.deserialize_json(
                data["ChannelModerator"]
            )
        )
    return out


def redact_sensitive(value: DescribeChannelModeratorResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_moderator" in value:
        import capo_chime_sdk_messaging.types.channel_moderator

        out["channel_moderator"] = (
            capo_chime_sdk_messaging.types.channel_moderator.redact_sensitive(
                value["channel_moderator"]
            )
        )
    return out
