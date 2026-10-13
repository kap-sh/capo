"""Generated from Smithy shape ``com.amazonaws.ivs#Channels``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ivs.types.channel

Channels: TypeAlias = list["capo_ivs.types.channel.Channel"]


# --- restJson1 ser/de ---
def serialize_json(value: Channels) -> list:
    import capo_ivs.types.channel

    out: list = []
    for item in value:
        out.append(capo_ivs.types.channel.serialize_json(item))
    return out


def deserialize_json(data: list) -> Channels:
    import capo_ivs.types.channel

    out: Channels = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ivs.types.channel.deserialize_json(item))
    return out


def redact_sensitive(value: Channels) -> list[Any]:
    import capo_ivs.types.channel

    return [capo_ivs.types.channel.redact_sensitive(item) for item in value]
