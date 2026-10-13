"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemVersionListElement``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.account_id
    import capo_billingconductor.types.billing_group_arn
    import capo_billingconductor.types.billing_period
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


class CustomLineItemVersionListElement(TypedDict, closed=True):
    name: NotRequired[
        "capo_billingconductor.types.custom_line_item_name.CustomLineItemName"
    ]
    """<p>The name of the custom line item.</p>"""
    charge_details: NotRequired[
        "capo_billingconductor.types.list_custom_line_item_charge_details.ListCustomLineItemChargeDetails"
    ]
    currency_code: NotRequired["capo_billingconductor.types.currency_code.CurrencyCode"]
    """<p>The charge value currency of the custom line item.</p>"""
    description: NotRequired[
        "capo_billingconductor.types.custom_line_item_description.CustomLineItemDescription"
    ]
    """<p>The description of the custom line item.</p>"""
    product_code: NotRequired[
        "capo_billingconductor.types.custom_line_item_product_code.CustomLineItemProductCode"
    ]
    """<p>The product code that’s associated with the custom line item.</p>"""
    billing_group_arn: NotRequired[
        "capo_billingconductor.types.billing_group_arn.BillingGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the billing group that the custom line item applies to.</p>"""
    creation_time: "capo_billingconductor.types.instant.Instant"
    """<p>The time when the custom line item version was created.</p>"""
    last_modified_time: "capo_billingconductor.types.instant.Instant"
    """<p>The most recent time that the custom line item version was modified.</p>"""
    association_size: (
        "capo_billingconductor.types.number_of_associations.NumberOfAssociations"
    )
    """<p>The number of resources that are associated with the custom line item.</p>"""
    start_billing_period: NotRequired[
        "capo_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p>The start billing period of the custom line item version.</p>"""
    end_billing_period: NotRequired[
        "capo_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p>The end billing period of the custom line item version.</p>"""
    arn: NotRequired[
        "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    ]
    """<p> A list of custom line item Amazon Resource Names (ARNs) to retrieve information. </p>"""
    start_time: "capo_billingconductor.types.instant.Instant"
    """<p> The inclusive start time. </p>"""
    account_id: NotRequired["capo_billingconductor.types.account_id.AccountId"]
    """<p>The Amazon Web Services account in which this custom line item will be applied to.</p>"""
    computation_rule: NotRequired[
        "capo_billingconductor.types.computation_rule_enum.ComputationRuleEnum"
    ]
    """<p> The computation rule for a specific version of a custom line item, determining how charges are computed and reflected in the bill. </p>"""
    presentation_details: NotRequired[
        "capo_billingconductor.types.presentation_object.PresentationObject"
    ]
    """<p> Presentation configuration for a specific version of a custom line item, specifying how charges are displayed in the bill. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemVersionListElement) -> dict:
    out: dict = {}
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
    if "start_billing_period" in value:
        out["StartBillingPeriod"] = value["start_billing_period"]
    if "end_billing_period" in value:
        out["EndBillingPeriod"] = value["end_billing_period"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    out["StartTime"] = value.get("start_time", 0)
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


def deserialize_json(data: dict) -> CustomLineItemVersionListElement:
    out: CustomLineItemVersionListElement = {}  # type: ignore[typeddict-item]
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
    if data.get("StartBillingPeriod") is not None:
        out["start_billing_period"] = data["StartBillingPeriod"]
    if data.get("EndBillingPeriod") is not None:
        out["end_billing_period"] = data["EndBillingPeriod"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("StartTime") is not None:
        out["start_time"] = data["StartTime"]
    else:
        out["start_time"] = 0
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


def redact_sensitive(value: CustomLineItemVersionListElement) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
