"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#AuthorizationContext``."""

from typing import TypeAlias

AuthorizationContext: TypeAlias = dict["str", "object"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AuthorizationContext) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AuthorizationContext:
    out: AuthorizationContext = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
