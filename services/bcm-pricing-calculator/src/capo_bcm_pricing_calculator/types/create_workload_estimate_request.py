"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#CreateWorkloadEstimateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.client_token
    import capo_bcm_pricing_calculator.types.tags
    import capo_bcm_pricing_calculator.types.workload_estimate_name
    import capo_bcm_pricing_calculator.types.workload_estimate_rate_type


class CreateWorkloadEstimateRequest(TypedDict, closed=True):
    name: (
        "capo_bcm_pricing_calculator.types.workload_estimate_name.WorkloadEstimateName"
    )
    """<p> A descriptive name for the workload estimate. </p>"""
    client_token: NotRequired[
        "capo_bcm_pricing_calculator.types.client_token.ClientToken"
    ]
    """<p> A unique, case-sensitive identifier to ensure idempotency of the request. </p>"""
    rate_type: NotRequired[
        "capo_bcm_pricing_calculator.types.workload_estimate_rate_type.WorkloadEstimateRateType"
    ]
    """<p> The type of pricing rates to use for the estimate. </p>"""
    tags: NotRequired["capo_bcm_pricing_calculator.types.tags.Tags"]
    """<p> The tags to apply to the workload estimate. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateWorkloadEstimateRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "rate_type" in value:
        import capo_bcm_pricing_calculator.types.workload_estimate_rate_type

        out["rateType"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_rate_type.serialize_aws_json_1_0(
                value["rate_type"]
            )
        )
    if "tags" in value:
        import capo_bcm_pricing_calculator.types.tags

        out["tags"] = capo_bcm_pricing_calculator.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateWorkloadEstimateRequest:
    out: CreateWorkloadEstimateRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("rateType") is not None:
        import capo_bcm_pricing_calculator.types.workload_estimate_rate_type

        out["rate_type"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_rate_type.deserialize_aws_json_1_0(
                data["rateType"]
            )
        )
    if data.get("tags") is not None:
        import capo_bcm_pricing_calculator.types.tags

        out["tags"] = capo_bcm_pricing_calculator.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
