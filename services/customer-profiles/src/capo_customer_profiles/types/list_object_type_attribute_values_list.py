"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListObjectTypeAttributeValuesList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.list_object_type_attribute_values_item

ListObjectTypeAttributeValuesList: TypeAlias = list[
    "capo_customer_profiles.types.list_object_type_attribute_values_item.ListObjectTypeAttributeValuesItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectTypeAttributeValuesList) -> list:
    import capo_customer_profiles.types.list_object_type_attribute_values_item

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.list_object_type_attribute_values_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListObjectTypeAttributeValuesList:
    import capo_customer_profiles.types.list_object_type_attribute_values_item

    out: ListObjectTypeAttributeValuesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_customer_profiles.types.list_object_type_attribute_values_item.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ListObjectTypeAttributeValuesList) -> list[Any]:
    import capo_customer_profiles.types.list_object_type_attribute_values_item

    return [
        capo_customer_profiles.types.list_object_type_attribute_values_item.redact_sensitive(
            item
        )
        for item in value
    ]
