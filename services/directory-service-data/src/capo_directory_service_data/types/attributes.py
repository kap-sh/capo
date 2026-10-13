"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#Attributes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service_data.types.attribute_value
    import capo_directory_service_data.types.ldap_display_name

Attributes: TypeAlias = dict[
    "capo_directory_service_data.types.ldap_display_name.LdapDisplayName",
    "capo_directory_service_data.types.attribute_value.AttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Attributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_directory_service_data.types.attribute_value

        out[key] = capo_directory_service_data.types.attribute_value.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> Attributes:
    out: Attributes = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_directory_service_data.types.attribute_value

        out[key] = capo_directory_service_data.types.attribute_value.deserialize_json(
            value
        )
    return out


def redact_sensitive(value: Attributes) -> dict[str, Any]:
    import capo_directory_service_data.types.attribute_value

    return {
        key: capo_directory_service_data.types.attribute_value.redact_sensitive(item)
        for key, item in value.items()
    }
