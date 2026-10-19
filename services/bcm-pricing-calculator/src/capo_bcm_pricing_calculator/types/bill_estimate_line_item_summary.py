"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillEstimateLineItemSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.account_id
    import capo_bcm_pricing_calculator.types.availability_zone
    import capo_bcm_pricing_calculator.types.cost_amount
    import capo_bcm_pricing_calculator.types.operation
    import capo_bcm_pricing_calculator.types.resource_id
    import capo_bcm_pricing_calculator.types.savings_plan_arns
    import capo_bcm_pricing_calculator.types.service_code
    import capo_bcm_pricing_calculator.types.usage_quantity_result
    import capo_bcm_pricing_calculator.types.usage_type


class BillEstimateLineItemSummary(TypedDict, closed=True):
    service_code: "capo_bcm_pricing_calculator.types.service_code.ServiceCode"
    """<p> The Amazon Web Services service code associated with this line item. </p>"""
    usage_type: "capo_bcm_pricing_calculator.types.usage_type.UsageType"
    """<p> The type of usage for this line item. </p>"""
    operation: "capo_bcm_pricing_calculator.types.operation.Operation"
    """<p> The specific operation associated with this line item. </p>"""
    location: NotRequired["str"]
    """<p> The location associated with this line item. </p>"""
    availability_zone: NotRequired[
        "capo_bcm_pricing_calculator.types.availability_zone.AvailabilityZone"
    ]
    """<p> The availability zone associated with this line item, if applicable. </p>"""
    id: NotRequired["capo_bcm_pricing_calculator.types.resource_id.ResourceId"]
    """<p> The unique identifier of this line item. </p>"""
    line_item_id: NotRequired["str"]
    """<p> The line item identifier from the original bill. </p>"""
    line_item_type: NotRequired["str"]
    """<p> The type of this line item (e.g., Usage, Tax, Credit). </p>"""
    payer_account_id: NotRequired[
        "capo_bcm_pricing_calculator.types.account_id.AccountId"
    ]
    """<p> The Amazon Web Services account ID of the payer for this line item. </p>"""
    usage_account_id: NotRequired[
        "capo_bcm_pricing_calculator.types.account_id.AccountId"
    ]
    """<p> The Amazon Web Services account ID associated with the usage for this line item. </p>"""
    estimated_usage_quantity: NotRequired[
        "capo_bcm_pricing_calculator.types.usage_quantity_result.UsageQuantityResult"
    ]
    """<p> The estimated usage quantity for this line item. </p>"""
    estimated_cost: NotRequired[
        "capo_bcm_pricing_calculator.types.cost_amount.CostAmount"
    ]
    """<p> The estimated cost for this line item. </p>"""
    historical_usage_quantity: NotRequired[
        "capo_bcm_pricing_calculator.types.usage_quantity_result.UsageQuantityResult"
    ]
    """<p> The historical usage quantity for this line item. </p>"""
    historical_cost: NotRequired[
        "capo_bcm_pricing_calculator.types.cost_amount.CostAmount"
    ]
    """<p> The historical cost for this line item. </p>"""
    savings_plan_arns: NotRequired[
        "capo_bcm_pricing_calculator.types.savings_plan_arns.SavingsPlanArns"
    ]
    """<p> The Amazon Resource Names (ARNs) of any Savings Plans applied to this line item. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillEstimateLineItemSummary) -> dict:
    out: dict = {}
    out["serviceCode"] = value["service_code"]
    out["usageType"] = value["usage_type"]
    out["operation"] = value["operation"]
    if "location" in value:
        out["location"] = value["location"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "id" in value:
        out["id"] = value["id"]
    if "line_item_id" in value:
        out["lineItemId"] = value["line_item_id"]
    if "line_item_type" in value:
        out["lineItemType"] = value["line_item_type"]
    if "payer_account_id" in value:
        out["payerAccountId"] = value["payer_account_id"]
    if "usage_account_id" in value:
        out["usageAccountId"] = value["usage_account_id"]
    if "estimated_usage_quantity" in value:
        import capo_bcm_pricing_calculator.types.usage_quantity_result

        out["estimatedUsageQuantity"] = (
            capo_bcm_pricing_calculator.types.usage_quantity_result.serialize_aws_json_1_0(
                value["estimated_usage_quantity"]
            )
        )
    if "estimated_cost" in value:
        import capo_bcm_pricing_calculator.types.cost_amount

        out["estimatedCost"] = (
            capo_bcm_pricing_calculator.types.cost_amount.serialize_aws_json_1_0(
                value["estimated_cost"]
            )
        )
    if "historical_usage_quantity" in value:
        import capo_bcm_pricing_calculator.types.usage_quantity_result

        out["historicalUsageQuantity"] = (
            capo_bcm_pricing_calculator.types.usage_quantity_result.serialize_aws_json_1_0(
                value["historical_usage_quantity"]
            )
        )
    if "historical_cost" in value:
        import capo_bcm_pricing_calculator.types.cost_amount

        out["historicalCost"] = (
            capo_bcm_pricing_calculator.types.cost_amount.serialize_aws_json_1_0(
                value["historical_cost"]
            )
        )
    if "savings_plan_arns" in value:
        import capo_bcm_pricing_calculator.types.savings_plan_arns

        out["savingsPlanArns"] = (
            capo_bcm_pricing_calculator.types.savings_plan_arns.serialize_aws_json_1_0(
                value["savings_plan_arns"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BillEstimateLineItemSummary:
    out: BillEstimateLineItemSummary = {}  # type: ignore[typeddict-item]
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    else:
        out["service_code"] = ""
    if data.get("usageType") is not None:
        out["usage_type"] = data["usageType"]
    else:
        out["usage_type"] = ""
    if data.get("operation") is not None:
        out["operation"] = data["operation"]
    else:
        out["operation"] = ""
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("lineItemId") is not None:
        out["line_item_id"] = data["lineItemId"]
    if data.get("lineItemType") is not None:
        out["line_item_type"] = data["lineItemType"]
    if data.get("payerAccountId") is not None:
        out["payer_account_id"] = data["payerAccountId"]
    if data.get("usageAccountId") is not None:
        out["usage_account_id"] = data["usageAccountId"]
    if data.get("estimatedUsageQuantity") is not None:
        import capo_bcm_pricing_calculator.types.usage_quantity_result

        out["estimated_usage_quantity"] = (
            capo_bcm_pricing_calculator.types.usage_quantity_result.deserialize_aws_json_1_0(
                data["estimatedUsageQuantity"]
            )
        )
    if data.get("estimatedCost") is not None:
        import capo_bcm_pricing_calculator.types.cost_amount

        out["estimated_cost"] = (
            capo_bcm_pricing_calculator.types.cost_amount.deserialize_aws_json_1_0(
                data["estimatedCost"]
            )
        )
    if data.get("historicalUsageQuantity") is not None:
        import capo_bcm_pricing_calculator.types.usage_quantity_result

        out["historical_usage_quantity"] = (
            capo_bcm_pricing_calculator.types.usage_quantity_result.deserialize_aws_json_1_0(
                data["historicalUsageQuantity"]
            )
        )
    if data.get("historicalCost") is not None:
        import capo_bcm_pricing_calculator.types.cost_amount

        out["historical_cost"] = (
            capo_bcm_pricing_calculator.types.cost_amount.deserialize_aws_json_1_0(
                data["historicalCost"]
            )
        )
    if data.get("savingsPlanArns") is not None:
        import capo_bcm_pricing_calculator.types.savings_plan_arns

        out["savings_plan_arns"] = (
            capo_bcm_pricing_calculator.types.savings_plan_arns.deserialize_aws_json_1_0(
                data["savingsPlanArns"]
            )
        )
    return out
