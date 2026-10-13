"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#Context``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_personalize_runtime.types.attribute_name
    import capo_personalize_runtime.types.attribute_value

Context: TypeAlias = dict[
    "capo_personalize_runtime.types.attribute_name.AttributeName",
    "capo_personalize_runtime.types.attribute_value.AttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Context) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Context:
    out: Context = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: Context) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
