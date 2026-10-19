"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillEstimateInputUsageModificationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.account_id
    import capo_bcm_pricing_calculator.types.availability_zone
    import capo_bcm_pricing_calculator.types.historical_usage_entity
    import capo_bcm_pricing_calculator.types.operation
    import capo_bcm_pricing_calculator.types.resource_id
    import capo_bcm_pricing_calculator.types.service_code
    import capo_bcm_pricing_calculator.types.usage_group
    import capo_bcm_pricing_calculator.types.usage_quantities
    import capo_bcm_pricing_calculator.types.usage_type


class BillEstimateInputUsageModificationSummary(TypedDict, closed=True):
    service_code: "capo_bcm_pricing_calculator.types.service_code.ServiceCode"
    """<p> The Amazon Web Services service code for this usage modification. </p>"""
    usage_type: "capo_bcm_pricing_calculator.types.usage_type.UsageType"
    """<p> The type of usage being modified. </p>"""
    operation: "capo_bcm_pricing_calculator.types.operation.Operation"
    """<p> The specific operation associated with this usage modification. </p>"""
    location: NotRequired["str"]
    """<p> The location associated with this usage modification. </p>"""
    availability_zone: NotRequired[
        "capo_bcm_pricing_calculator.types.availability_zone.AvailabilityZone"
    ]
    """<p> The availability zone associated with this usage modification, if applicable. </p>"""
    id: NotRequired["capo_bcm_pricing_calculator.types.resource_id.ResourceId"]
    """<p> The unique identifier of the usage modification. </p>"""
    group: NotRequired["capo_bcm_pricing_calculator.types.usage_group.UsageGroup"]
    """<p> The group identifier for the usage modification. </p>"""
    usage_account_id: NotRequired[
        "capo_bcm_pricing_calculator.types.account_id.AccountId"
    ]
    """<p> The Amazon Web Services account ID associated with this usage modification. </p>"""
    quantities: NotRequired[
        "capo_bcm_pricing_calculator.types.usage_quantities.UsageQuantities"
    ]
    """<p> The modified usage quantities. </p>"""
    historical_usage: NotRequired[
        "capo_bcm_pricing_calculator.types.historical_usage_entity.HistoricalUsageEntity"
    ]
    """<p> Historical usage data associated with this modification, if available. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillEstimateInputUsageModificationSummary) -> dict:
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
    if "group" in value:
        out["group"] = value["group"]
    if "usage_account_id" in value:
        out["usageAccountId"] = value["usage_account_id"]
    if "quantities" in value:
        import capo_bcm_pricing_calculator.types.usage_quantities

        out["quantities"] = (
            capo_bcm_pricing_calculator.types.usage_quantities.serialize_aws_json_1_0(
                value["quantities"]
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


def deserialize_aws_json_1_0(data: dict) -> BillEstimateInputUsageModificationSummary:
    out: BillEstimateInputUsageModificationSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("group") is not None:
        out["group"] = data["group"]
    if data.get("usageAccountId") is not None:
        out["usage_account_id"] = data["usageAccountId"]
    if data.get("quantities") is not None:
        import capo_bcm_pricing_calculator.types.usage_quantities

        out["quantities"] = (
            capo_bcm_pricing_calculator.types.usage_quantities.deserialize_aws_json_1_0(
                data["quantities"]
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
