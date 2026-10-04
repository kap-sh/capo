"""Generated from Smithy shape ``com.amazonaws.endusermessaging#ContextMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_endusermessaging.types.context_key
    import capo_endusermessaging.types.context_value

ContextMap: TypeAlias = dict[
    "capo_endusermessaging.types.context_key.ContextKey",
    "capo_endusermessaging.types.context_value.ContextValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ContextMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ContextMap:
    out: ContextMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
