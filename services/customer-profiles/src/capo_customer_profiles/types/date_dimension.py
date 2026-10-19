"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DateDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.date_dimension_type
    import capo_customer_profiles.types.date_values


class DateDimension(TypedDict, closed=True):
    dimension_type: "capo_customer_profiles.types.date_dimension_type.DateDimensionType"
    """<p>The action to segment with.</p>"""
    values: "capo_customer_profiles.types.date_values.DateValues"
    """<p>The values to apply the DimensionType on. To reference a calculated attribute or profile attribute as a dynamic value, use handlebar notation: <code>{{_profile.ProfileAttributeName}}</code> or <code>{{_calculated_attribute.CalculatedAttributeName}}</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateDimension) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.date_dimension_type

    out["DimensionType"] = (
        capo_customer_profiles.types.date_dimension_type.serialize_json(
            value["dimension_type"]
        )
    )
    import capo_customer_profiles.types.date_values

    out["Values"] = capo_customer_profiles.types.date_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> DateDimension:
    out: DateDimension = {}  # type: ignore[typeddict-item]
    if data.get("DimensionType") is not None:
        import capo_customer_profiles.types.date_dimension_type

        out["dimension_type"] = (
            capo_customer_profiles.types.date_dimension_type.deserialize_json(
                data["DimensionType"]
            )
        )
    else:
        import typing

        out["dimension_type"] = typing.cast(
            "capo_customer_profiles.types.date_dimension_type.DateDimensionType", ""
        )
    if data.get("Values") is not None:
        import capo_customer_profiles.types.date_values

        out["values"] = capo_customer_profiles.types.date_values.deserialize_json(
            data["Values"]
        )
    else:
        out["values"] = []
    return out
