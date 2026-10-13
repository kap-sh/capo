"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdateCustomLineItemInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_arn
    import capo_billingconductor.types.custom_line_item_billing_period_range
    import capo_billingconductor.types.custom_line_item_description
    import capo_billingconductor.types.custom_line_item_name
    import capo_billingconductor.types.update_custom_line_item_charge_details


class UpdateCustomLineItemInput(TypedDict, closed=True):
    arn: "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    """<p> The ARN of the custom line item to be updated. </p>"""
    name: NotRequired[
        "capo_billingconductor.types.custom_line_item_name.CustomLineItemName"
    ]
    """<p> The new name for the custom line item. </p>"""
    description: NotRequired[
        "capo_billingconductor.types.custom_line_item_description.CustomLineItemDescription"
    ]
    """<p> The new line item description of the custom line item. </p>"""
    charge_details: NotRequired[
        "capo_billingconductor.types.update_custom_line_item_charge_details.UpdateCustomLineItemChargeDetails"
    ]
    """<p> A <code>ListCustomLineItemChargeDetails</code> containing the new charge details for the custom line item. </p>"""
    billing_period_range: NotRequired[
        "capo_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomLineItemInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "charge_details" in value:
        import capo_billingconductor.types.update_custom_line_item_charge_details

        out["ChargeDetails"] = (
            capo_billingconductor.types.update_custom_line_item_charge_details.serialize_json(
                value["charge_details"]
            )
        )
    if "billing_period_range" in value:
        import capo_billingconductor.types.custom_line_item_billing_period_range

        out["BillingPeriodRange"] = (
            capo_billingconductor.types.custom_line_item_billing_period_range.serialize_json(
                value["billing_period_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCustomLineItemInput:
    out: UpdateCustomLineItemInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdateCustomLineItemInput.arn required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ChargeDetails") is not None:
        import capo_billingconductor.types.update_custom_line_item_charge_details

        out["charge_details"] = (
            capo_billingconductor.types.update_custom_line_item_charge_details.deserialize_json(
                data["ChargeDetails"]
            )
        )
    if data.get("BillingPeriodRange") is not None:
        import capo_billingconductor.types.custom_line_item_billing_period_range

        out["billing_period_range"] = (
            capo_billingconductor.types.custom_line_item_billing_period_range.deserialize_json(
                data["BillingPeriodRange"]
            )
        )
    return out


def redact_sensitive(value: UpdateCustomLineItemInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
