"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchDeleteWorkloadEstimateUsageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_entries
    import capo_bcm_pricing_calculator.types.resource_id


class BatchDeleteWorkloadEstimateUsageRequest(TypedDict, closed=True):
    workload_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The ID of the Workload estimate for which you want to delete the modeled usage. </p>"""
    ids: "capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_entries.BatchDeleteWorkloadEstimateUsageEntries"
    """<p> List of usage that you want to delete from the Workload estimate. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchDeleteWorkloadEstimateUsageRequest) -> dict:
    out: dict = {}
    out["workloadEstimateId"] = value["workload_estimate_id"]
    import capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_entries

    out["ids"] = (
        capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_entries.serialize_aws_json_1_0(
            value["ids"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchDeleteWorkloadEstimateUsageRequest:
    out: BatchDeleteWorkloadEstimateUsageRequest = {}  # type: ignore[typeddict-item]
    if data.get("workloadEstimateId") is not None:
        out["workload_estimate_id"] = data["workloadEstimateId"]
    else:
        out["workload_estimate_id"] = ""
    if data.get("ids") is not None:
        import capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_entries

        out["ids"] = (
            capo_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_entries.deserialize_aws_json_1_0(
                data["ids"]
            )
        )
    else:
        out["ids"] = []
    return out
