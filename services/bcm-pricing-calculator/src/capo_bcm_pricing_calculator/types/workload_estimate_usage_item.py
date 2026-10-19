"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#WorkloadEstimateUsageItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.account_id
    import capo_bcm_pricing_calculator.types.currency_code
    import capo_bcm_pricing_calculator.types.historical_usage_entity
    import capo_bcm_pricing_calculator.types.operation
    import capo_bcm_pricing_calculator.types.resource_id
    import capo_bcm_pricing_calculator.types.service_code
    import capo_bcm_pricing_calculator.types.usage_group
    import capo_bcm_pricing_calculator.types.usage_type
    import capo_bcm_pricing_calculator.types.workload_estimate_cost_status
    import capo_bcm_pricing_calculator.types.workload_estimate_usage_quantity


class WorkloadEstimateUsageItem(TypedDict, closed=True):
    service_code: "capo_bcm_pricing_calculator.types.service_code.ServiceCode"
    """<p> The Amazon Web Services service code associated with this usage item. </p>"""
    usage_type: "capo_bcm_pricing_calculator.types.usage_type.UsageType"
    """<p> The type of usage for this item. </p>"""
    operation: "capo_bcm_pricing_calculator.types.operation.Operation"
    """<p> The specific operation associated with this usage item. </p>"""
    location: NotRequired["str"]
    """<p> The location associated with this usage item. </p>"""
    id: NotRequired["capo_bcm_pricing_calculator.types.resource_id.ResourceId"]
    """<p> The unique identifier of this usage item. </p>"""
    usage_account_id: NotRequired[
        "capo_bcm_pricing_calculator.types.account_id.AccountId"
    ]
    """<p> The Amazon Web Services account ID associated with this usage item. </p>"""
    group: NotRequired["capo_bcm_pricing_calculator.types.usage_group.UsageGroup"]
    """<p> The group identifier for this usage item. </p>"""
    quantity: NotRequired[
        "capo_bcm_pricing_calculator.types.workload_estimate_usage_quantity.WorkloadEstimateUsageQuantity"
    ]
    """<p> The estimated usage quantity for this item. </p>"""
    cost: NotRequired["float"]
    """<p> The estimated cost for this usage item. </p>"""
    currency: NotRequired[
        "capo_bcm_pricing_calculator.types.currency_code.CurrencyCode"
    ]
    """<p> The currency of the estimated cost. </p>"""
    status: NotRequired[
        "capo_bcm_pricing_calculator.types.workload_estimate_cost_status.WorkloadEstimateCostStatus"
    ]
    """<p> The current status of this usage item. </p>"""
    historical_usage: NotRequired[
        "capo_bcm_pricing_calculator.types.historical_usage_entity.HistoricalUsageEntity"
    ]
    """<p> Historical usage data associated with this item, if available. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkloadEstimateUsageItem) -> dict:
    out: dict = {}
    out["serviceCode"] = value["service_code"]
    out["usageType"] = value["usage_type"]
    out["operation"] = value["operation"]
    if "location" in value:
        out["location"] = value["location"]
    if "id" in value:
        out["id"] = value["id"]
    if "usage_account_id" in value:
        out["usageAccountId"] = value["usage_account_id"]
    if "group" in value:
        out["group"] = value["group"]
    if "quantity" in value:
        import capo_bcm_pricing_calculator.types.workload_estimate_usage_quantity

        out["quantity"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_usage_quantity.serialize_aws_json_1_0(
                value["quantity"]
            )
        )
    if "cost" in value:
        out["cost"] = (
            "NaN"
            if value["cost"] != value["cost"]
            else "Infinity"
            if value["cost"] == float("inf")
            else "-Infinity"
            if value["cost"] == float("-inf")
            else value["cost"]
        )
    if "currency" in value:
        import capo_bcm_pricing_calculator.types.currency_code

        out["currency"] = (
            capo_bcm_pricing_calculator.types.currency_code.serialize_aws_json_1_0(
                value["currency"]
            )
        )
    if "status" in value:
        import capo_bcm_pricing_calculator.types.workload_estimate_cost_status

        out["status"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_cost_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "historical_usage" in value:
        import capo_bcm_pricing_calculator.types.historical_usage_entity

        out["historicalUsage"] = (
            capo_bcm_pricing_calculator.types.historical_usage_entity.serialize_aws_json_1_0(
                value["historical_usage"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkloadEstimateUsageItem:
    out: WorkloadEstimateUsageItem = {}  # type: ignore[typeddict-item]
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
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("usageAccountId") is not None:
        out["usage_account_id"] = data["usageAccountId"]
    if data.get("group") is not None:
        out["group"] = data["group"]
    if data.get("quantity") is not None:
        import capo_bcm_pricing_calculator.types.workload_estimate_usage_quantity

        out["quantity"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_usage_quantity.deserialize_aws_json_1_0(
                data["quantity"]
            )
        )
    if data.get("cost") is not None:
        out["cost"] = float(data["cost"])
    if data.get("currency") is not None:
        import capo_bcm_pricing_calculator.types.currency_code

        out["currency"] = (
            capo_bcm_pricing_calculator.types.currency_code.deserialize_aws_json_1_0(
                data["currency"]
            )
        )
    if data.get("status") is not None:
        import capo_bcm_pricing_calculator.types.workload_estimate_cost_status

        out["status"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_cost_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("historicalUsage") is not None:
        import capo_bcm_pricing_calculator.types.historical_usage_entity

        out["historical_usage"] = (
            capo_bcm_pricing_calculator.types.historical_usage_entity.deserialize_aws_json_1_0(
                data["historicalUsage"]
            )
        )
    return out
