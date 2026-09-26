"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.tag_key

TagKeyList: TypeAlias = list["capo_network_security_manager.types.tag_key.TagKey"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeyList) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeyList:
    return [item for item in data if item is not None]
