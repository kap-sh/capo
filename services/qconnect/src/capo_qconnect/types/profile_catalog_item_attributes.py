"""Generated from Smithy shape ``com.amazonaws.qconnect#ProfileCatalogItemAttributes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_attribute_key
    import capo_qconnect.types.message_template_attribute_value

ProfileCatalogItemAttributes: TypeAlias = dict[
    "capo_qconnect.types.message_template_attribute_key.MessageTemplateAttributeKey",
    "capo_qconnect.types.message_template_attribute_value.MessageTemplateAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ProfileCatalogItemAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ProfileCatalogItemAttributes:
    out: ProfileCatalogItemAttributes = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: ProfileCatalogItemAttributes) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
