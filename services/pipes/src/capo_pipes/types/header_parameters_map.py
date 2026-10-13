"""Generated from Smithy shape ``com.amazonaws.pipes#HeaderParametersMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.header_key
    import capo_pipes.types.header_value

HeaderParametersMap: TypeAlias = dict[
    "capo_pipes.types.header_key.HeaderKey", "capo_pipes.types.header_value.HeaderValue"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: HeaderParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> HeaderParametersMap:
    out: HeaderParametersMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: HeaderParametersMap) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
