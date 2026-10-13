"""Generated from Smithy shape ``com.amazonaws.mediapackage#__listOfChannel``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackage.types.channel

__listOfChannel: TypeAlias = list["capo_mediapackage.types.channel.Channel"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfChannel) -> list:
    import capo_mediapackage.types.channel

    out: list = []
    for item in value:
        out.append(capo_mediapackage.types.channel.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfChannel:
    import capo_mediapackage.types.channel

    out: __listOfChannel = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mediapackage.types.channel.deserialize_json(item))
    return out


def redact_sensitive(value: __listOfChannel) -> list[Any]:
    import capo_mediapackage.types.channel

    return [capo_mediapackage.types.channel.redact_sensitive(item) for item in value]
