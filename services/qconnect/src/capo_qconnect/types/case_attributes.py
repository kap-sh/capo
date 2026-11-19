"""Generated from Smithy shape ``com.amazonaws.qconnect#CaseAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_attribute_key
    import capo_qconnect.types.message_template_attribute_value

CaseAttributes: TypeAlias = dict[
    "capo_qconnect.types.message_template_attribute_key.MessageTemplateAttributeKey",
    "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CaseAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> CaseAttributes:
    out: CaseAttributes = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
