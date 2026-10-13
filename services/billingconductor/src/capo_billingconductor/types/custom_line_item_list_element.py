"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemListElement``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.account_id
    import capo_billingconductor.types.billing_group_arn
    import capo_billingconductor.types.computation_rule_enum
    import capo_billingconductor.types.currency_code
    import capo_billingconductor.types.custom_line_item_arn
    import capo_billingconductor.types.custom_line_item_description
    import capo_billingconductor.types.custom_line_item_name
    import capo_billingconductor.types.custom_line_item_product_code
    import capo_billingconductor.types.instant
    import capo_billingconductor.types.list_custom_line_item_charge_details
    import capo_billingconductor.types.number_of_associations
    import capo_billingconductor.types.presentation_object


class CustomLineItemListElement(TypedDict, closed=True):
    arn: NotRequired[
        "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    ]
    """<p>The Amazon Resource Names (ARNs) for custom line items.</p>"""
    name: NotRequired[
        "capo_billingconductor.types.custom_line_item_name.CustomLineItemName"
    ]
    """<p>The custom line item's name.</p>"""
    charge_details: NotRequired[
        "capo_billingconductor.types.list_custom_line_item_charge_details.ListCustomLineItemChargeDetails"
    ]
    """<p>A <code>ListCustomLineItemChargeDetails</code> that describes the charge details of a custom line item.</p>"""
    currency_code: NotRequired["capo_billingconductor.types.currency_code.CurrencyCode"]
    """<p>The custom line item's charge value currency. Only one of the valid values can be used.</p>"""
    description: NotRequired[
        "capo_billingconductor.types.custom_line_item_description.CustomLineItemDescription"
    ]
    """<p>The custom line item's description. This is shown on the Bills page in association with the charge value.</p>"""
    product_code: NotRequired[
        "capo_billingconductor.types.custom_line_item_product_code.CustomLineItemProductCode"
    ]
    """<p>The product code that's associated with the custom line item.</p>"""
    billing_group_arn: NotRequired[
        "capo_billingconductor.types.billing_group_arn.BillingGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.</p>"""
    creation_time: "capo_billingconductor.types.instant.Instant"
    """<p>The time created.</p>"""
    last_modified_time: "capo_billingconductor.types.instant.Instant"
    """<p>The most recent time when the custom line item was modified.</p>"""
    association_size: (
        "capo_billingconductor.types.number_of_associations.NumberOfAssociations"
    )
    """<p>The number of resources that are associated to the custom line item.</p>"""
    account_id: NotRequired["capo_billingconductor.types.account_id.AccountId"]
    """<p>The Amazon Web Services account in which this custom line item will be applied to.</p>"""
    computation_rule: NotRequired[
        "capo_billingconductor.types.computation_rule_enum.ComputationRuleEnum"
    ]
    """<p> The computation rule that determines how the custom line item charges are computed and reflected in the bill. </p>"""
    presentation_details: NotRequired[
        "capo_billingconductor.types.presentation_object.PresentationObject"
    ]
    """<p> Configuration details specifying how the custom line item charges are presented, including which service the charges are shown under. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemListElement) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "charge_details" in value:
        import capo_billingconductor.types.list_custom_line_item_charge_details

        out["ChargeDetails"] = (
            capo_billingconductor.types.list_custom_line_item_charge_details.serialize_json(
                value["charge_details"]
            )
        )
    if "currency_code" in value:
        import capo_billingconductor.types.currency_code

        out["CurrencyCode"] = capo_billingconductor.types.currency_code.serialize_json(
            value["currency_code"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "product_code" in value:
        out["ProductCode"] = value["product_code"]
    if "billing_group_arn" in value:
        out["BillingGroupArn"] = value["billing_group_arn"]
    out["CreationTime"] = value.get("creation_time", 0)
    out["LastModifiedTime"] = value.get("last_modified_time", 0)
    out["AssociationSize"] = value.get("association_size", 0)
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "computation_rule" in value:
        import capo_billingconductor.types.computation_rule_enum

        out["ComputationRule"] = (
            capo_billingconductor.types.computation_rule_enum.serialize_json(
                value["computation_rule"]
            )
        )
    if "presentation_details" in value:
        import capo_billingconductor.types.presentation_object

        out["PresentationDetails"] = (
            capo_billingconductor.types.presentation_object.serialize_json(
                value["presentation_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomLineItemListElement:
    out: CustomLineItemListElement = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ChargeDetails") is not None:
        import capo_billingconductor.types.list_custom_line_item_charge_details

        out["charge_details"] = (
            capo_billingconductor.types.list_custom_line_item_charge_details.deserialize_json(
                data["ChargeDetails"]
            )
        )
    if data.get("CurrencyCode") is not None:
        import capo_billingconductor.types.currency_code

        out["currency_code"] = (
            capo_billingconductor.types.currency_code.deserialize_json(
                data["CurrencyCode"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ProductCode") is not None:
        out["product_code"] = data["ProductCode"]
    if data.get("BillingGroupArn") is not None:
        out["billing_group_arn"] = data["BillingGroupArn"]
    if data.get("CreationTime") is not None:
        out["creation_time"] = data["CreationTime"]
    else:
        out["creation_time"] = 0
    if data.get("LastModifiedTime") is not None:
        out["last_modified_time"] = data["LastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    if data.get("AssociationSize") is not None:
        out["association_size"] = data["AssociationSize"]
    else:
        out["association_size"] = 0
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("ComputationRule") is not None:
        import capo_billingconductor.types.computation_rule_enum

        out["computation_rule"] = (
            capo_billingconductor.types.computation_rule_enum.deserialize_json(
                data["ComputationRule"]
            )
        )
    if data.get("PresentationDetails") is not None:
        import capo_billingconductor.types.presentation_object

        out["presentation_details"] = (
            capo_billingconductor.types.presentation_object.deserialize_json(
                data["PresentationDetails"]
            )
        )
    return out


def redact_sensitive(value: CustomLineItemListElement) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
