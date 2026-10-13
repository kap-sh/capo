"""Generated from Smithy shape ``com.amazonaws.ivs#GetChannelResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.channel


class GetChannelResponse(TypedDict, closed=True):
    channel: NotRequired["capo_ivs.types.channel.Channel"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelResponse) -> dict:
    out: dict = {}
    if "channel" in value:
        import capo_ivs.types.channel

        out["channel"] = capo_ivs.types.channel.serialize_json(value["channel"])
    return out


def deserialize_json(data: dict) -> GetChannelResponse:
    out: GetChannelResponse = {}  # type: ignore[typeddict-item]
    if data.get("channel") is not None:
        import capo_ivs.types.channel

        out["channel"] = capo_ivs.types.channel.deserialize_json(data["channel"])
    return out


def redact_sensitive(value: GetChannelResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel" in value:
        import capo_ivs.types.channel

        out["channel"] = capo_ivs.types.channel.redact_sensitive(value["channel"])
    return out
