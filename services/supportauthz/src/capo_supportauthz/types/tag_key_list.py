"""Generated from Smithy shape ``com.amazonaws.supportauthz#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supportauthz.types.tag_key

TagKeyList: TypeAlias = list["capo_supportauthz.types.tag_key.TagKey"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeyList) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeyList:
    return [item for item in data if item is not None]
