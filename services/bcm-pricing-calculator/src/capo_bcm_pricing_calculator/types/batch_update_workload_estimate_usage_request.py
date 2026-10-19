"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateWorkloadEstimateUsageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entries
    import capo_bcm_pricing_calculator.types.resource_id


class BatchUpdateWorkloadEstimateUsageRequest(TypedDict, closed=True):
    workload_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The ID of the Workload estimate for which you want to modify the usage lines. </p>"""
    usage: "capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entries.BatchUpdateWorkloadEstimateUsageEntries"
    """<p> List of usage line amounts and usage group that you want to update in a Workload estimate identified by the usage ID. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchUpdateWorkloadEstimateUsageRequest) -> dict:
    out: dict = {}
    out["workloadEstimateId"] = value["workload_estimate_id"]
    import capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entries

    out["usage"] = (
        capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entries.serialize_aws_json_1_0(
            value["usage"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchUpdateWorkloadEstimateUsageRequest:
    out: BatchUpdateWorkloadEstimateUsageRequest = {}  # type: ignore[typeddict-item]
    if data.get("workloadEstimateId") is not None:
        out["workload_estimate_id"] = data["workloadEstimateId"]
    else:
        out["workload_estimate_id"] = ""
    if data.get("usage") is not None:
        import capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entries

        out["usage"] = (
            capo_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entries.deserialize_aws_json_1_0(
                data["usage"]
            )
        )
    else:
        out["usage"] = []
    return out
