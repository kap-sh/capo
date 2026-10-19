"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FilterAttributeDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.filter_dimension_type
    import capo_customer_profiles.types.value_list


class FilterAttributeDimension(TypedDict, closed=True):
    dimension_type: (
        "capo_customer_profiles.types.filter_dimension_type.FilterDimensionType"
    )
    """<p>The action to filter with.</p>"""
    values: "capo_customer_profiles.types.value_list.ValueList"
    """<p>The values to apply the DimensionType on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterAttributeDimension) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.filter_dimension_type

    out["DimensionType"] = (
        capo_customer_profiles.types.filter_dimension_type.serialize_json(
            value["dimension_type"]
        )
    )
    import capo_customer_profiles.types.value_list

    out["Values"] = capo_customer_profiles.types.value_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> FilterAttributeDimension:
    out: FilterAttributeDimension = {}  # type: ignore[typeddict-item]
    if data.get("DimensionType") is not None:
        import capo_customer_profiles.types.filter_dimension_type

        out["dimension_type"] = (
            capo_customer_profiles.types.filter_dimension_type.deserialize_json(
                data["DimensionType"]
            )
        )
    else:
        import typing

        out["dimension_type"] = typing.cast(
            "capo_customer_profiles.types.filter_dimension_type.FilterDimensionType", ""
        )
    if data.get("Values") is not None:
        import capo_customer_profiles.types.value_list

        out["values"] = capo_customer_profiles.types.value_list.deserialize_json(
            data["Values"]
        )
    else:
        out["values"] = []
    return out
