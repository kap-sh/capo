"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdateCustomLineItemOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_group_full_arn
    import capo_billingconductor.types.custom_line_item_arn
    import capo_billingconductor.types.custom_line_item_description
    import capo_billingconductor.types.custom_line_item_name
    import capo_billingconductor.types.instant
    import capo_billingconductor.types.list_custom_line_item_charge_details
    import capo_billingconductor.types.number_of_associations


class UpdateCustomLineItemOutput(TypedDict, closed=True):
    arn: NotRequired[
        "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    ]
    """<p> The ARN of the successfully updated custom line item. </p>"""
    billing_group_arn: NotRequired[
        "capo_billingconductor.types.billing_group_full_arn.BillingGroupFullArn"
    ]
    """<p> The ARN of the billing group that the custom line item is applied to. </p>"""
    name: NotRequired[
        "capo_billingconductor.types.custom_line_item_name.CustomLineItemName"
    ]
    """<p> The name of the successfully updated custom line item. </p>"""
    description: NotRequired[
        "capo_billingconductor.types.custom_line_item_description.CustomLineItemDescription"
    ]
    """<p> The description of the successfully updated custom line item. </p>"""
    charge_details: NotRequired[
        "capo_billingconductor.types.list_custom_line_item_charge_details.ListCustomLineItemChargeDetails"
    ]
    """<p> A <code>ListCustomLineItemChargeDetails</code> containing the charge details of the successfully updated custom line item. </p>"""
    last_modified_time: "capo_billingconductor.types.instant.Instant"
    """<p> The most recent time when the custom line item was modified. </p>"""
    association_size: (
        "capo_billingconductor.types.number_of_associations.NumberOfAssociations"
    )
    """<p> The number of resources that are associated to the custom line item. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomLineItemOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "billing_group_arn" in value:
        out["BillingGroupArn"] = value["billing_group_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "charge_details" in value:
        import capo_billingconductor.types.list_custom_line_item_charge_details

        out["ChargeDetails"] = (
            capo_billingconductor.types.list_custom_line_item_charge_details.serialize_json(
                value["charge_details"]
            )
        )
    out["LastModifiedTime"] = value.get("last_modified_time", 0)
    out["AssociationSize"] = value.get("association_size", 0)
    return out


def deserialize_json(data: dict) -> UpdateCustomLineItemOutput:
    out: UpdateCustomLineItemOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("BillingGroupArn") is not None:
        out["billing_group_arn"] = data["BillingGroupArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ChargeDetails") is not None:
        import capo_billingconductor.types.list_custom_line_item_charge_details

        out["charge_details"] = (
            capo_billingconductor.types.list_custom_line_item_charge_details.deserialize_json(
                data["ChargeDetails"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        out["last_modified_time"] = data["LastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    if data.get("AssociationSize") is not None:
        out["association_size"] = data["AssociationSize"]
    else:
        out["association_size"] = 0
    return out


def redact_sensitive(value: UpdateCustomLineItemOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
