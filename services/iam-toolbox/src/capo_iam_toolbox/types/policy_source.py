"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#PolicySource``."""

from typing import TypeAlias

PolicySource: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PolicySource) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> PolicySource:
    out: PolicySource = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
