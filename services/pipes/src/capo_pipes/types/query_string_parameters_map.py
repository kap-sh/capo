"""Generated from Smithy shape ``com.amazonaws.pipes#QueryStringParametersMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.query_string_key
    import capo_pipes.types.query_string_value

QueryStringParametersMap: TypeAlias = dict[
    "capo_pipes.types.query_string_key.QueryStringKey",
    "capo_pipes.types.query_string_value.QueryStringValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: QueryStringParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> QueryStringParametersMap:
    out: QueryStringParametersMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: QueryStringParametersMap) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
