"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#CustomParameterMap``."""

from typing import TypeAlias

CustomParameterMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CustomParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> CustomParameterMap:
    out: CustomParameterMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
