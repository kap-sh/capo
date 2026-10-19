"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemPercentageChargeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_associations_list
    import capo_billingconductor.types.custom_line_item_percentage_charge_value


class CustomLineItemPercentageChargeDetails(TypedDict, closed=True):
    percentage_value: "capo_billingconductor.types.custom_line_item_percentage_charge_value.CustomLineItemPercentageChargeValue"
    """<p>The custom line item's percentage value. This will be multiplied against the combined value of its associated resources to determine its charge value. </p>"""
    associated_values: NotRequired[
        "capo_billingconductor.types.custom_line_item_associations_list.CustomLineItemAssociationsList"
    ]
    """<p>A list of resource ARNs to associate to the percentage custom line item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemPercentageChargeDetails) -> dict:
    out: dict = {}
    out["PercentageValue"] = (
        "NaN"
        if value["percentage_value"] != value["percentage_value"]
        else "Infinity"
        if value["percentage_value"] == float("inf")
        else "-Infinity"
        if value["percentage_value"] == float("-inf")
        else value["percentage_value"]
    )
    if "associated_values" in value:
        import capo_billingconductor.types.custom_line_item_associations_list

        out["AssociatedValues"] = (
            capo_billingconductor.types.custom_line_item_associations_list.serialize_json(
                value["associated_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomLineItemPercentageChargeDetails:
    out: CustomLineItemPercentageChargeDetails = {}  # type: ignore[typeddict-item]
    if data.get("PercentageValue") is not None:
        out["percentage_value"] = float(data["PercentageValue"])
    else:
        out["percentage_value"] = 0.0
    if data.get("AssociatedValues") is not None:
        import capo_billingconductor.types.custom_line_item_associations_list

        out["associated_values"] = (
            capo_billingconductor.types.custom_line_item_associations_list.deserialize_json(
                data["AssociatedValues"]
            )
        )
    return out
