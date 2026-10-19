"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#DeleteScalingPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.scaling_plan_name
    import capo_auto_scaling_plans.types.scaling_plan_version


class DeleteScalingPlanRequest(TypedDict, closed=True):
    scaling_plan_name: "capo_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName"
    """<p>The name of the scaling plan.</p>"""
    scaling_plan_version: (
        "capo_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion"
    )
    """<p>The version number of the scaling plan. Currently, the only valid value is <code>1</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteScalingPlanRequest) -> dict:
    out: dict = {}
    out["ScalingPlanName"] = value["scaling_plan_name"]
    out["ScalingPlanVersion"] = value["scaling_plan_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteScalingPlanRequest:
    out: DeleteScalingPlanRequest = {}  # type: ignore[typeddict-item]
    if data.get("ScalingPlanName") is not None:
        out["scaling_plan_name"] = data["ScalingPlanName"]
    else:
        out["scaling_plan_name"] = ""
    if data.get("ScalingPlanVersion") is not None:
        out["scaling_plan_version"] = data["ScalingPlanVersion"]
    else:
        out["scaling_plan_version"] = 0
    return out
