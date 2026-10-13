"""Generated from Smithy shape ``com.amazonaws.ivs#UpdateChannelResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.channel


class UpdateChannelResponse(TypedDict, closed=True):
    channel: NotRequired["capo_ivs.types.channel.Channel"]
    """<p>Object specifying the updated channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelResponse) -> dict:
    out: dict = {}
    if "channel" in value:
        import capo_ivs.types.channel

        out["channel"] = capo_ivs.types.channel.serialize_json(value["channel"])
    return out


def deserialize_json(data: dict) -> UpdateChannelResponse:
    out: UpdateChannelResponse = {}  # type: ignore[typeddict-item]
    if data.get("channel") is not None:
        import capo_ivs.types.channel

        out["channel"] = capo_ivs.types.channel.deserialize_json(data["channel"])
    return out


def redact_sensitive(value: UpdateChannelResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel" in value:
        import capo_ivs.types.channel

        out["channel"] = capo_ivs.types.channel.redact_sensitive(value["channel"])
    return out
