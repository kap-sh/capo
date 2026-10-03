"""Generated from Smithy shape ``com.amazonaws.freetier#FreeTierUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_freetier.types.generic_double
    import capo_freetier.types.generic_string


class FreeTierUsage(TypedDict, closed=True):
    service: NotRequired["capo_freetier.types.generic_string.GenericString"]
    """<p>The name of the Amazon Web Services service providing the Free Tier offer. For example, this can be Amazon Elastic Compute Cloud.</p>"""
    operation: NotRequired["capo_freetier.types.generic_string.GenericString"]
    """<p>Describes <code>usageType</code> more granularly with the specific Amazon Web Services service API operation. For example, this can be the <code>RunInstances</code> API operation for Amazon Elastic Compute Cloud.</p>"""
    usage_type: NotRequired["capo_freetier.types.generic_string.GenericString"]
    """<p>Describes the usage details of the offer. For example, this might be <code>Global-BoxUsage:freetrial</code>.</p>"""
    region: NotRequired["capo_freetier.types.generic_string.GenericString"]
    """<p>Describes the Amazon Web Services Region for which this offer is applicable</p>"""
    actual_usage_amount: "capo_freetier.types.generic_double.GenericDouble"
    """<p>Describes the actual usage accrued month-to-day (MTD) that you've used so far.</p>"""
    forecasted_usage_amount: "capo_freetier.types.generic_double.GenericDouble"
    """<p>Describes the forecasted usage by the month that you're expected to use.</p>"""
    limit: "capo_freetier.types.generic_double.GenericDouble"
    """<p>Describes the maximum usage allowed in Free Tier.</p>"""
    unit: NotRequired["capo_freetier.types.generic_string.GenericString"]
    """<p>Describes the unit of the <code>usageType</code>, such as <code>Hrs</code>.</p>"""
    description: NotRequired["capo_freetier.types.generic_string.GenericString"]
    """<p>The description of the Free Tier offer.</p>"""
    free_tier_type: NotRequired["capo_freetier.types.generic_string.GenericString"]
    """<p>Describes the type of the Free Tier offer. For example, the offer can be <code>"12 Months Free"</code>, <code>"Always Free"</code>, and <code>"Free Trial"</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FreeTierUsage) -> dict:
    out: dict = {}
    if "service" in value:
        out["service"] = value["service"]
    if "operation" in value:
        out["operation"] = value["operation"]
    if "usage_type" in value:
        out["usageType"] = value["usage_type"]
    if "region" in value:
        out["region"] = value["region"]
    out["actualUsageAmount"] = (
        "NaN"
        if value.get("actual_usage_amount", 0) != value.get("actual_usage_amount", 0)
        else "Infinity"
        if value.get("actual_usage_amount", 0) == float("inf")
        else "-Infinity"
        if value.get("actual_usage_amount", 0) == float("-inf")
        else value.get("actual_usage_amount", 0)
    )
    out["forecastedUsageAmount"] = (
        "NaN"
        if value.get("forecasted_usage_amount", 0)
        != value.get("forecasted_usage_amount", 0)
        else "Infinity"
        if value.get("forecasted_usage_amount", 0) == float("inf")
        else "-Infinity"
        if value.get("forecasted_usage_amount", 0) == float("-inf")
        else value.get("forecasted_usage_amount", 0)
    )
    out["limit"] = (
        "NaN"
        if value.get("limit", 0) != value.get("limit", 0)
        else "Infinity"
        if value.get("limit", 0) == float("inf")
        else "-Infinity"
        if value.get("limit", 0) == float("-inf")
        else value.get("limit", 0)
    )
    if "unit" in value:
        out["unit"] = value["unit"]
    if "description" in value:
        out["description"] = value["description"]
    if "free_tier_type" in value:
        out["freeTierType"] = value["free_tier_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FreeTierUsage:
    out: FreeTierUsage = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        out["service"] = data["service"]
    if data.get("operation") is not None:
        out["operation"] = data["operation"]
    if data.get("usageType") is not None:
        out["usage_type"] = data["usageType"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("actualUsageAmount") is not None:
        out["actual_usage_amount"] = float(data["actualUsageAmount"])
    else:
        out["actual_usage_amount"] = 0
    if data.get("forecastedUsageAmount") is not None:
        out["forecasted_usage_amount"] = float(data["forecastedUsageAmount"])
    else:
        out["forecasted_usage_amount"] = 0
    if data.get("limit") is not None:
        out["limit"] = float(data["limit"])
    else:
        out["limit"] = 0
    if data.get("unit") is not None:
        out["unit"] = data["unit"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("freeTierType") is not None:
        out["free_tier_type"] = data["freeTierType"]
    return out
