"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#TagList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.tag

TagList: TypeAlias = list["capo_chime_sdk_voice.types.tag.Tag"]


# --- restJson1 ser/de ---
def serialize_json(value: TagList) -> list:
    import capo_chime_sdk_voice.types.tag

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_voice.types.tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagList:
    import capo_chime_sdk_voice.types.tag

    out: TagList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_chime_sdk_voice.types.tag.deserialize_json(item))
    return out


def redact_sensitive(value: TagList) -> list[Any]:
    import capo_chime_sdk_voice.types.tag

    return [capo_chime_sdk_voice.types.tag.redact_sensitive(item) for item in value]
