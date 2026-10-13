"""Generated from Smithy shape ``com.amazonaws.repostspace#ChannelsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_repostspace.types.channel_data

ChannelsList: TypeAlias = list["capo_repostspace.types.channel_data.ChannelData"]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelsList) -> list:
    import capo_repostspace.types.channel_data

    out: list = []
    for item in value:
        out.append(capo_repostspace.types.channel_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChannelsList:
    import capo_repostspace.types.channel_data

    out: ChannelsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_repostspace.types.channel_data.deserialize_json(item))
    return out


def redact_sensitive(value: ChannelsList) -> list[Any]:
    import capo_repostspace.types.channel_data

    return [
        capo_repostspace.types.channel_data.redact_sensitive(item) for item in value
    ]
