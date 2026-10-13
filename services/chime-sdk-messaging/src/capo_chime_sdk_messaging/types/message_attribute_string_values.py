"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#MessageAttributeStringValues``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.message_attribute_string_value

MessageAttributeStringValues: TypeAlias = list[
    "capo_chime_sdk_messaging.types.message_attribute_string_value.MessageAttributeStringValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageAttributeStringValues) -> list:
    return list(value)


def deserialize_json(data: list) -> MessageAttributeStringValues:
    return [item for item in data if item is not None]


def redact_sensitive(value: MessageAttributeStringValues) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
