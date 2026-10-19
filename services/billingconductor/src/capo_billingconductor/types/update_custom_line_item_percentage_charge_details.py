"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdateCustomLineItemPercentageChargeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_percentage_charge_value


class UpdateCustomLineItemPercentageChargeDetails(TypedDict, closed=True):
    percentage_value: "capo_billingconductor.types.custom_line_item_percentage_charge_value.CustomLineItemPercentageChargeValue"
    """<p> The custom line item's new percentage value. This will be multiplied against the combined value of its associated resources to determine its charge value. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomLineItemPercentageChargeDetails) -> dict:
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
    return out


def deserialize_json(data: dict) -> UpdateCustomLineItemPercentageChargeDetails:
    out: UpdateCustomLineItemPercentageChargeDetails = {}  # type: ignore[typeddict-item]
    if data.get("PercentageValue") is not None:
        out["percentage_value"] = float(data["PercentageValue"])
    else:
        out["percentage_value"] = 0.0
    return out
