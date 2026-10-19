"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListCustomLineItemChargeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_type
    import capo_billingconductor.types.line_item_filters_list
    import capo_billingconductor.types.list_custom_line_item_flat_charge_details
    import capo_billingconductor.types.list_custom_line_item_percentage_charge_details


class ListCustomLineItemChargeDetails(TypedDict, closed=True):
    flat: NotRequired[
        "capo_billingconductor.types.list_custom_line_item_flat_charge_details.ListCustomLineItemFlatChargeDetails"
    ]
    """<p> A <code>ListCustomLineItemFlatChargeDetails</code> that describes the charge details of a flat custom line item. </p>"""
    percentage: NotRequired[
        "capo_billingconductor.types.list_custom_line_item_percentage_charge_details.ListCustomLineItemPercentageChargeDetails"
    ]
    """<p> A <code>ListCustomLineItemPercentageChargeDetails</code> that describes the charge details of a percentage custom line item. </p>"""
    type: "capo_billingconductor.types.custom_line_item_type.CustomLineItemType"
    """<p> The type of the custom line item that indicates whether the charge is a <code>fee</code> or <code>credit</code>. </p>"""
    line_item_filters: NotRequired[
        "capo_billingconductor.types.line_item_filters_list.LineItemFiltersList"
    ]
    """<p>A representation of the line item filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomLineItemChargeDetails) -> dict:
    out: dict = {}
    if "flat" in value:
        import capo_billingconductor.types.list_custom_line_item_flat_charge_details

        out["Flat"] = (
            capo_billingconductor.types.list_custom_line_item_flat_charge_details.serialize_json(
                value["flat"]
            )
        )
    if "percentage" in value:
        import capo_billingconductor.types.list_custom_line_item_percentage_charge_details

        out["Percentage"] = (
            capo_billingconductor.types.list_custom_line_item_percentage_charge_details.serialize_json(
                value["percentage"]
            )
        )
    import capo_billingconductor.types.custom_line_item_type

    out["Type"] = capo_billingconductor.types.custom_line_item_type.serialize_json(
        value["type"]
    )
    if "line_item_filters" in value:
        import capo_billingconductor.types.line_item_filters_list

        out["LineItemFilters"] = (
            capo_billingconductor.types.line_item_filters_list.serialize_json(
                value["line_item_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCustomLineItemChargeDetails:
    out: ListCustomLineItemChargeDetails = {}  # type: ignore[typeddict-item]
    if data.get("Flat") is not None:
        import capo_billingconductor.types.list_custom_line_item_flat_charge_details

        out["flat"] = (
            capo_billingconductor.types.list_custom_line_item_flat_charge_details.deserialize_json(
                data["Flat"]
            )
        )
    if data.get("Percentage") is not None:
        import capo_billingconductor.types.list_custom_line_item_percentage_charge_details

        out["percentage"] = (
            capo_billingconductor.types.list_custom_line_item_percentage_charge_details.deserialize_json(
                data["Percentage"]
            )
        )
    if data.get("Type") is not None:
        import capo_billingconductor.types.custom_line_item_type

        out["type"] = (
            capo_billingconductor.types.custom_line_item_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_billingconductor.types.custom_line_item_type.CustomLineItemType", ""
        )
    if data.get("LineItemFilters") is not None:
        import capo_billingconductor.types.line_item_filters_list

        out["line_item_filters"] = (
            capo_billingconductor.types.line_item_filters_list.deserialize_json(
                data["LineItemFilters"]
            )
        )
    return out
