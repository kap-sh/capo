"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#TagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.tag_key
    import capo_network_security_manager.types.tag_value

TagMap: TypeAlias = dict[
    "capo_network_security_manager.types.tag_key.TagKey",
    "capo_network_security_manager.types.tag_value.TagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TagMap:
    out: TagMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
