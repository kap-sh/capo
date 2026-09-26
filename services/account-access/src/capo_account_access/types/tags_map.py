"""Generated from Smithy shape ``com.amazonaws.accountaccess#TagsMap``."""

from typing import TypeAlias

TagsMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TagsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TagsMap:
    out: TagsMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
