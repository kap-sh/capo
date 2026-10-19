"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SortAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.field_name
    import capo_customer_profiles.types.segment_sort_data_type
    import capo_customer_profiles.types.segment_sort_order
    import capo_customer_profiles.types.sort_attribute_type


class SortAttribute(TypedDict, closed=True):
    name: "capo_customer_profiles.types.field_name.fieldName"
    """<p>The name of the attribute to sort by.</p>"""
    data_type: NotRequired[
        "capo_customer_profiles.types.segment_sort_data_type.SegmentSortDataType"
    ]
    """<p>The data type of the sort attribute (e.g., string, number, date).</p>"""
    order: "capo_customer_profiles.types.segment_sort_order.SegmentSortOrder"
    """<p>The sort order for the attribute (ascending or descending).</p>"""
    type: "capo_customer_profiles.types.sort_attribute_type.SortAttributeType"
    """<p>The type of attribute (e.g., profile, calculated).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SortAttribute) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "data_type" in value:
        import capo_customer_profiles.types.segment_sort_data_type

        out["DataType"] = (
            capo_customer_profiles.types.segment_sort_data_type.serialize_json(
                value["data_type"]
            )
        )
    import capo_customer_profiles.types.segment_sort_order

    out["Order"] = capo_customer_profiles.types.segment_sort_order.serialize_json(
        value["order"]
    )
    import capo_customer_profiles.types.sort_attribute_type

    out["Type"] = capo_customer_profiles.types.sort_attribute_type.serialize_json(
        value.get("type", "PROFILE")
    )
    return out


def deserialize_json(data: dict) -> SortAttribute:
    out: SortAttribute = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("DataType") is not None:
        import capo_customer_profiles.types.segment_sort_data_type

        out["data_type"] = (
            capo_customer_profiles.types.segment_sort_data_type.deserialize_json(
                data["DataType"]
            )
        )
    if data.get("Order") is not None:
        import capo_customer_profiles.types.segment_sort_order

        out["order"] = capo_customer_profiles.types.segment_sort_order.deserialize_json(
            data["Order"]
        )
    else:
        import typing

        out["order"] = typing.cast(
            "capo_customer_profiles.types.segment_sort_order.SegmentSortOrder", ""
        )
    if data.get("Type") is not None:
        import capo_customer_profiles.types.sort_attribute_type

        out["type"] = capo_customer_profiles.types.sort_attribute_type.deserialize_json(
            data["Type"]
        )
    else:
        out["type"] = "PROFILE"
    return out
