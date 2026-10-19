"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#UpdateWorkloadEstimateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bcm_pricing_calculator.types.resource_id
    import capo_bcm_pricing_calculator.types.workload_estimate_name


class UpdateWorkloadEstimateRequest(TypedDict, closed=True):
    identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the workload estimate to update. </p>"""
    name: NotRequired[
        "capo_bcm_pricing_calculator.types.workload_estimate_name.WorkloadEstimateName"
    ]
    """<p> The new name for the workload estimate. </p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p> The new expiration date for the workload estimate. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateWorkloadEstimateRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "name" in value:
        out["name"] = value["name"]
    if "expires_at" in value:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["expiresAt"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["expires_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateWorkloadEstimateRequest:
    out: UpdateWorkloadEstimateRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("expiresAt") is not None:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["expires_at"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["expiresAt"]
            )
        )
    return out
