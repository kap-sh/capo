"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.attribute_dimension_type
    import capo_customer_profiles.types.values


class AttributeDimension(TypedDict, closed=True):
    dimension_type: (
        "capo_customer_profiles.types.attribute_dimension_type.AttributeDimensionType"
    )
    """<p>The action to segment with.</p>"""
    values: "capo_customer_profiles.types.values.Values"
    """<p>The values to apply the DimensionType on. To reference a calculated attribute or profile attribute as a dynamic value, use handlebar notation: <code>{{_profile.ProfileAttributeName}}</code> or <code>{{_calculated_attribute.CalculatedAttributeName}}</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeDimension) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.attribute_dimension_type

    out["DimensionType"] = (
        capo_customer_profiles.types.attribute_dimension_type.serialize_json(
            value["dimension_type"]
        )
    )
    import capo_customer_profiles.types.values

    out["Values"] = capo_customer_profiles.types.values.serialize_json(value["values"])
    return out


def deserialize_json(data: dict) -> AttributeDimension:
    out: AttributeDimension = {}  # type: ignore[typeddict-item]
    if data.get("DimensionType") is not None:
        import capo_customer_profiles.types.attribute_dimension_type

        out["dimension_type"] = (
            capo_customer_profiles.types.attribute_dimension_type.deserialize_json(
                data["DimensionType"]
            )
        )
    else:
        import typing

        out["dimension_type"] = typing.cast(
            "capo_customer_profiles.types.attribute_dimension_type.AttributeDimensionType",
            "",
        )
    if data.get("Values") is not None:
        import capo_customer_profiles.types.values

        out["values"] = capo_customer_profiles.types.values.deserialize_json(
            data["Values"]
        )
    else:
        out["values"] = []
    return out
