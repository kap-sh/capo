"""Generated from Smithy shape ``com.amazonaws.lambdaweb#EnvironmentVariables``."""

from typing import TypeAlias

EnvironmentVariables: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EnvironmentVariables) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> EnvironmentVariables:
    out: EnvironmentVariables = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
