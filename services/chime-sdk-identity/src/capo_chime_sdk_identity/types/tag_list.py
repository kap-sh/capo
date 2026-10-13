"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#TagList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.tag

TagList: TypeAlias = list["capo_chime_sdk_identity.types.tag.Tag"]


# --- restJson1 ser/de ---
def serialize_json(value: TagList) -> list:
    import capo_chime_sdk_identity.types.tag

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_identity.types.tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagList:
    import capo_chime_sdk_identity.types.tag

    out: TagList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_chime_sdk_identity.types.tag.deserialize_json(item))
    return out


def redact_sensitive(value: TagList) -> list[Any]:
    import capo_chime_sdk_identity.types.tag

    return [capo_chime_sdk_identity.types.tag.redact_sensitive(item) for item in value]
