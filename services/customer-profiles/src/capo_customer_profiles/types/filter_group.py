"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FilterGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.filter_dimension_list
    import capo_customer_profiles.types.type


class FilterGroup(TypedDict, closed=True):
    type: "capo_customer_profiles.types.type.Type"
    """<p>The type of logical relationship between the dimensions of the Filter group.</p>"""
    dimensions: "capo_customer_profiles.types.filter_dimension_list.FilterDimensionList"
    """<p>Object that holds the attributes to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterGroup) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.type

    out["Type"] = capo_customer_profiles.types.type.serialize_json(value["type"])
    import capo_customer_profiles.types.filter_dimension_list

    out["Dimensions"] = (
        capo_customer_profiles.types.filter_dimension_list.serialize_json(
            value["dimensions"]
        )
    )
    return out


def deserialize_json(data: dict) -> FilterGroup:
    out: FilterGroup = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_customer_profiles.types.type

        out["type"] = capo_customer_profiles.types.type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_customer_profiles.types.type.Type", "")
    if data.get("Dimensions") is not None:
        import capo_customer_profiles.types.filter_dimension_list

        out["dimensions"] = (
            capo_customer_profiles.types.filter_dimension_list.deserialize_json(
                data["Dimensions"]
            )
        )
    else:
        out["dimensions"] = []
    return out
