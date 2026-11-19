"""Generated from Smithy shape ``com.amazonaws.qconnect#CalculatedAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_attribute_key
    import capo_qconnect.types.message_template_attribute_value

CalculatedAttributes: TypeAlias = dict[
    "capo_qconnect.types.message_template_attribute_key.MessageTemplateAttributeKey",
    "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CalculatedAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> CalculatedAttributes:
    out: CalculatedAttributes = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
