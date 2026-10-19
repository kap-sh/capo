"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#DescribeScalingPlanResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.max_results
    import capo_auto_scaling_plans.types.next_token
    import capo_auto_scaling_plans.types.scaling_plan_name
    import capo_auto_scaling_plans.types.scaling_plan_version


class DescribeScalingPlanResourcesRequest(TypedDict, closed=True):
    scaling_plan_name: "capo_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName"
    """<p>The name of the scaling plan.</p>"""
    scaling_plan_version: (
        "capo_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion"
    )
    """<p>The version number of the scaling plan. Currently, the only valid value is <code>1</code>.</p>"""
    max_results: NotRequired["capo_auto_scaling_plans.types.max_results.MaxResults"]
    """<p>The maximum number of scalable resources to return. The value must be between 1 and 50. The default value is 50.</p>"""
    next_token: NotRequired["capo_auto_scaling_plans.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeScalingPlanResourcesRequest) -> dict:
    out: dict = {}
    out["ScalingPlanName"] = value["scaling_plan_name"]
    out["ScalingPlanVersion"] = value["scaling_plan_version"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeScalingPlanResourcesRequest:
    out: DescribeScalingPlanResourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ScalingPlanName") is not None:
        out["scaling_plan_name"] = data["ScalingPlanName"]
    else:
        out["scaling_plan_name"] = ""
    if data.get("ScalingPlanVersion") is not None:
        out["scaling_plan_version"] = data["ScalingPlanVersion"]
    else:
        out["scaling_plan_version"] = 0
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
