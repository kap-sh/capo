"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateWorkloadEstimateUsageEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.resource_id
    import capo_bcm_pricing_calculator.types.usage_group


class BatchUpdateWorkloadEstimateUsageEntry(TypedDict, closed=True):
    id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the usage estimate to update. </p>"""
    group: NotRequired["capo_bcm_pricing_calculator.types.usage_group.UsageGroup"]
    """<p> The updated group identifier for the usage estimate. </p>"""
    amount: NotRequired["float"]
    """<p> The updated estimated usage amount. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchUpdateWorkloadEstimateUsageEntry) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "group" in value:
        out["group"] = value["group"]
    if "amount" in value:
        out["amount"] = (
            "NaN"
            if value["amount"] != value["amount"]
            else "Infinity"
            if value["amount"] == float("inf")
            else "-Infinity"
            if value["amount"] == float("-inf")
            else value["amount"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchUpdateWorkloadEstimateUsageEntry:
    out: BatchUpdateWorkloadEstimateUsageEntry = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("group") is not None:
        out["group"] = data["group"]
    if data.get("amount") is not None:
        out["amount"] = float(data["amount"])
    return out
