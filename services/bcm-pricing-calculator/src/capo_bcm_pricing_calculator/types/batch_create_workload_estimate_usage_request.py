"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateWorkloadEstimateUsageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entries
    import capo_bcm_pricing_calculator.types.client_token
    import capo_bcm_pricing_calculator.types.resource_id


class BatchCreateWorkloadEstimateUsageRequest(TypedDict, closed=True):
    workload_estimate_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The ID of the Workload estimate for which you want to create the modeled usage. </p>"""
    usage: "capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entries.BatchCreateWorkloadEstimateUsageEntries"
    """<p> List of usage that you want to model in the Workload estimate. </p>"""
    client_token: NotRequired[
        "capo_bcm_pricing_calculator.types.client_token.ClientToken"
    ]
    """<p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateWorkloadEstimateUsageRequest) -> dict:
    out: dict = {}
    out["workloadEstimateId"] = value["workload_estimate_id"]
    import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entries

    out["usage"] = (
        capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entries.serialize_aws_json_1_0(
            value["usage"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateWorkloadEstimateUsageRequest:
    out: BatchCreateWorkloadEstimateUsageRequest = {}  # type: ignore[typeddict-item]
    if data.get("workloadEstimateId") is not None:
        out["workload_estimate_id"] = data["workloadEstimateId"]
    else:
        out["workload_estimate_id"] = ""
    if data.get("usage") is not None:
        import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entries

        out["usage"] = (
            capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entries.deserialize_aws_json_1_0(
                data["usage"]
            )
        )
    else:
        out["usage"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
