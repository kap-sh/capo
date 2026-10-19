"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateWorkloadEstimateUsageEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.account_id
    import capo_bcm_pricing_calculator.types.historical_usage_entity
    import capo_bcm_pricing_calculator.types.key
    import capo_bcm_pricing_calculator.types.operation
    import capo_bcm_pricing_calculator.types.service_code
    import capo_bcm_pricing_calculator.types.usage_group
    import capo_bcm_pricing_calculator.types.usage_type


class BatchCreateWorkloadEstimateUsageEntry(TypedDict, closed=True):
    service_code: "capo_bcm_pricing_calculator.types.service_code.ServiceCode"
    """<p> The Amazon Web Services service code for this usage estimate. </p>"""
    usage_type: "capo_bcm_pricing_calculator.types.usage_type.UsageType"
    """<p> The type of usage being estimated. </p>"""
    operation: "capo_bcm_pricing_calculator.types.operation.Operation"
    """<p> The specific operation associated with this usage estimate. </p>"""
    key: "capo_bcm_pricing_calculator.types.key.Key"
    """<p> A unique identifier for this entry in the batch operation. </p>"""
    group: NotRequired["capo_bcm_pricing_calculator.types.usage_group.UsageGroup"]
    """<p> An optional group identifier for the usage estimate. </p>"""
    usage_account_id: "capo_bcm_pricing_calculator.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID associated with this usage estimate. </p>"""
    amount: "float"
    """<p> The estimated usage amount. </p>"""
    historical_usage: NotRequired[
        "capo_bcm_pricing_calculator.types.historical_usage_entity.HistoricalUsageEntity"
    ]
    """<p> Historical usage data associated with this estimate, if available. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateWorkloadEstimateUsageEntry) -> dict:
    out: dict = {}
    out["serviceCode"] = value["service_code"]
    out["usageType"] = value["usage_type"]
    out["operation"] = value["operation"]
    out["key"] = value["key"]
    if "group" in value:
        out["group"] = value["group"]
    out["usageAccountId"] = value["usage_account_id"]
    out["amount"] = (
        "NaN"
        if value["amount"] != value["amount"]
        else "Infinity"
        if value["amount"] == float("inf")
        else "-Infinity"
        if value["amount"] == float("-inf")
        else value["amount"]
    )
    if "historical_usage" in value:
        import capo_bcm_pricing_calculator.types.historical_usage_entity

        out["historicalUsage"] = (
            capo_bcm_pricing_calculator.types.historical_usage_entity.serialize_aws_json_1_0(
                value["historical_usage"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateWorkloadEstimateUsageEntry:
    out: BatchCreateWorkloadEstimateUsageEntry = {}  # type: ignore[typeddict-item]
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
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("group") is not None:
        out["group"] = data["group"]
    if data.get("usageAccountId") is not None:
        out["usage_account_id"] = data["usageAccountId"]
    else:
        out["usage_account_id"] = ""
    if data.get("amount") is not None:
        out["amount"] = float(data["amount"])
    else:
        out["amount"] = 0.0
    if data.get("historicalUsage") is not None:
        import capo_bcm_pricing_calculator.types.historical_usage_entity

        out["historical_usage"] = (
            capo_bcm_pricing_calculator.types.historical_usage_entity.deserialize_aws_json_1_0(
                data["historicalUsage"]
            )
        )
    return out
