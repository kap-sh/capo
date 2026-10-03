"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#UpdateScalingPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling_plans.errors import DeserializationError

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.application_source
    import capo_auto_scaling_plans.types.scaling_instructions
    import capo_auto_scaling_plans.types.scaling_plan_name
    import capo_auto_scaling_plans.types.scaling_plan_version


class UpdateScalingPlanRequest(TypedDict, closed=True):
    scaling_plan_name: "capo_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName"
    """<p>The name of the scaling plan.</p>"""
    scaling_plan_version: (
        "capo_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion"
    )
    """<p>The version number of the scaling plan. The only valid value is <code>1</code>. Currently, you cannot have multiple scaling plan versions.</p>"""
    application_source: NotRequired[
        "capo_auto_scaling_plans.types.application_source.ApplicationSource"
    ]
    """<p>A CloudFormation stack or set of tags.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ApplicationSource.html">ApplicationSource</a> in the <i>AWS Auto Scaling API Reference</i>.</p>"""
    scaling_instructions: NotRequired[
        "capo_auto_scaling_plans.types.scaling_instructions.ScalingInstructions"
    ]
    """<p>The scaling instructions.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ScalingInstruction.html">ScalingInstruction</a> in the <i>AWS Auto Scaling API Reference</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateScalingPlanRequest) -> dict:
    out: dict = {}
    out["ScalingPlanName"] = value["scaling_plan_name"]
    out["ScalingPlanVersion"] = value["scaling_plan_version"]
    if "application_source" in value:
        import capo_auto_scaling_plans.types.application_source

        out["ApplicationSource"] = (
            capo_auto_scaling_plans.types.application_source.serialize_aws_json_1_1(
                value["application_source"]
            )
        )
    if "scaling_instructions" in value:
        import capo_auto_scaling_plans.types.scaling_instructions

        out["ScalingInstructions"] = (
            capo_auto_scaling_plans.types.scaling_instructions.serialize_aws_json_1_1(
                value["scaling_instructions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateScalingPlanRequest:
    out: UpdateScalingPlanRequest = {}  # type: ignore[typeddict-item]
    if data.get("ScalingPlanName") is not None:
        out["scaling_plan_name"] = data["ScalingPlanName"]
    else:
        raise DeserializationError(
            "UpdateScalingPlanRequest.scaling_plan_name required"
        )
    if data.get("ScalingPlanVersion") is not None:
        out["scaling_plan_version"] = data["ScalingPlanVersion"]
    else:
        raise DeserializationError(
            "UpdateScalingPlanRequest.scaling_plan_version required"
        )
    if data.get("ApplicationSource") is not None:
        import capo_auto_scaling_plans.types.application_source

        out["application_source"] = (
            capo_auto_scaling_plans.types.application_source.deserialize_aws_json_1_1(
                data["ApplicationSource"]
            )
        )
    if data.get("ScalingInstructions") is not None:
        import capo_auto_scaling_plans.types.scaling_instructions

        out["scaling_instructions"] = (
            capo_auto_scaling_plans.types.scaling_instructions.deserialize_aws_json_1_1(
                data["ScalingInstructions"]
            )
        )
    return out
