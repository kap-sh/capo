"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CalculatedCustomAttributes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.calculated_attribute_dimension
    import capo_customer_profiles.types.type_name

CalculatedCustomAttributes: TypeAlias = dict[
    "capo_customer_profiles.types.type_name.typeName",
    "capo_customer_profiles.types.calculated_attribute_dimension.CalculatedAttributeDimension",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CalculatedCustomAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_customer_profiles.types.calculated_attribute_dimension

        out[key] = (
            capo_customer_profiles.types.calculated_attribute_dimension.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> CalculatedCustomAttributes:
    out: CalculatedCustomAttributes = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_customer_profiles.types.calculated_attribute_dimension

        out[key] = (
            capo_customer_profiles.types.calculated_attribute_dimension.deserialize_json(
                value
            )
        )
    return out


def redact_sensitive(value: CalculatedCustomAttributes) -> dict[str, Any]:
    import capo_customer_profiles.types.calculated_attribute_dimension

    return {
        key: capo_customer_profiles.types.calculated_attribute_dimension.redact_sensitive(
            item
        )
        for key, item in value.items()
    }
