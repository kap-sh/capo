"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DescribeChannelBanResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_ban


class DescribeChannelBanResponse(TypedDict, closed=True):
    channel_ban: NotRequired["capo_chime_sdk_messaging.types.channel_ban.ChannelBan"]
    """<p>The details of the ban.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelBanResponse) -> dict:
    out: dict = {}
    if "channel_ban" in value:
        import capo_chime_sdk_messaging.types.channel_ban

        out["ChannelBan"] = capo_chime_sdk_messaging.types.channel_ban.serialize_json(
            value["channel_ban"]
        )
    return out


def deserialize_json(data: dict) -> DescribeChannelBanResponse:
    out: DescribeChannelBanResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChannelBan") is not None:
        import capo_chime_sdk_messaging.types.channel_ban

        out["channel_ban"] = (
            capo_chime_sdk_messaging.types.channel_ban.deserialize_json(
                data["ChannelBan"]
            )
        )
    return out


def redact_sensitive(value: DescribeChannelBanResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_ban" in value:
        import capo_chime_sdk_messaging.types.channel_ban

        out["channel_ban"] = (
            capo_chime_sdk_messaging.types.channel_ban.redact_sensitive(
                value["channel_ban"]
            )
        )
    return out
