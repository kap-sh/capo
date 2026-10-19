"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioUsageModificationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.account_id
    import capo_bcm_pricing_calculator.types.availability_zone
    import capo_bcm_pricing_calculator.types.historical_usage_entity
    import capo_bcm_pricing_calculator.types.key
    import capo_bcm_pricing_calculator.types.operation
    import capo_bcm_pricing_calculator.types.service_code
    import capo_bcm_pricing_calculator.types.usage_amounts
    import capo_bcm_pricing_calculator.types.usage_group
    import capo_bcm_pricing_calculator.types.usage_type


class BatchCreateBillScenarioUsageModificationEntry(TypedDict, closed=True):
    service_code: "capo_bcm_pricing_calculator.types.service_code.ServiceCode"
    """<p> The Amazon Web Services service code for this usage modification. This identifies the specific Amazon Web Services service to the customer as a unique short abbreviation. For example, <code>AmazonEC2</code> and <code>AWSKMS</code>. </p>"""
    usage_type: "capo_bcm_pricing_calculator.types.usage_type.UsageType"
    """<p> Describes the usage details of the usage line item. </p>"""
    operation: "capo_bcm_pricing_calculator.types.operation.Operation"
    """<p> The specific operation associated with this usage modification. Describes the specific Amazon Web Services operation that this usage line models. For example, <code>RunInstances</code> indicates the operation of an Amazon EC2 instance. </p>"""
    availability_zone: NotRequired[
        "capo_bcm_pricing_calculator.types.availability_zone.AvailabilityZone"
    ]
    """<p> The Availability Zone that this usage line uses. </p>"""
    key: "capo_bcm_pricing_calculator.types.key.Key"
    """<p> A unique identifier for this entry in the batch operation. This can be any valid string. This key is useful to identify errors associated with any usage entry as any error is returned with this key. </p>"""
    group: NotRequired["capo_bcm_pricing_calculator.types.usage_group.UsageGroup"]
    """<p> An optional group identifier for the usage modification. </p>"""
    usage_account_id: "capo_bcm_pricing_calculator.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID to which this usage will be applied to. </p>"""
    amounts: NotRequired["capo_bcm_pricing_calculator.types.usage_amounts.UsageAmounts"]
    """<p> The amount of usage you want to create for the service use you are modeling. </p>"""
    historical_usage: NotRequired[
        "capo_bcm_pricing_calculator.types.historical_usage_entity.HistoricalUsageEntity"
    ]
    """<p> Historical usage data associated with this modification, if available. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchCreateBillScenarioUsageModificationEntry,
) -> dict:
    out: dict = {}
    out["serviceCode"] = value["service_code"]
    out["usageType"] = value["usage_type"]
    out["operation"] = value["operation"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    out["key"] = value["key"]
    if "group" in value:
        out["group"] = value["group"]
    out["usageAccountId"] = value["usage_account_id"]
    if "amounts" in value:
        import capo_bcm_pricing_calculator.types.usage_amounts

        out["amounts"] = (
            capo_bcm_pricing_calculator.types.usage_amounts.serialize_aws_json_1_0(
                value["amounts"]
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


def deserialize_aws_json_1_0(
    data: dict,
) -> BatchCreateBillScenarioUsageModificationEntry:
    out: BatchCreateBillScenarioUsageModificationEntry = {}  # type: ignore[typeddict-item]
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
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
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
    if data.get("amounts") is not None:
        import capo_bcm_pricing_calculator.types.usage_amounts

        out["amounts"] = (
            capo_bcm_pricing_calculator.types.usage_amounts.deserialize_aws_json_1_0(
                data["amounts"]
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
