"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingPlan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling_plans.errors import DeserializationError

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.application_source
    import capo_auto_scaling_plans.types.scaling_instructions
    import capo_auto_scaling_plans.types.scaling_plan_name
    import capo_auto_scaling_plans.types.scaling_plan_status_code
    import capo_auto_scaling_plans.types.scaling_plan_version
    import capo_auto_scaling_plans.types.timestamp_type
    import capo_auto_scaling_plans.types.xml_string


class ScalingPlan(TypedDict, closed=True):
    scaling_plan_name: "capo_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName"
    """<p>The name of the scaling plan.</p>"""
    scaling_plan_version: (
        "capo_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion"
    )
    """<p>The version number of the scaling plan.</p>"""
    application_source: (
        "capo_auto_scaling_plans.types.application_source.ApplicationSource"
    )
    """<p>A CloudFormation stack or a set of tags. You can create one scaling plan per application source.</p>"""
    scaling_instructions: (
        "capo_auto_scaling_plans.types.scaling_instructions.ScalingInstructions"
    )
    """<p>The scaling instructions.</p>"""
    status_code: (
        "capo_auto_scaling_plans.types.scaling_plan_status_code.ScalingPlanStatusCode"
    )
    """<p>The status of the scaling plan.</p> <ul> <li> <p> <code>Active</code> - The scaling plan is active.</p> </li> <li> <p> <code>ActiveWithProblems</code> - The scaling plan is active, but the scaling configuration for one or more resources could not be applied.</p> </li> <li> <p> <code>CreationInProgress</code> - The scaling plan is being created.</p> </li> <li> <p> <code>CreationFailed</code> - The scaling plan could not be created.</p> </li> <li> <p> <code>DeletionInProgress</code> - The scaling plan is being deleted.</p> </li> <li> <p> <code>DeletionFailed</code> - The scaling plan could not be deleted.</p> </li> <li> <p> <code>UpdateInProgress</code> - The scaling plan is being updated.</p> </li> <li> <p> <code>UpdateFailed</code> - The scaling plan could not be updated.</p> </li> </ul>"""
    status_message: NotRequired["capo_auto_scaling_plans.types.xml_string.XmlString"]
    """<p>A simple message about the current status of the scaling plan.</p>"""
    status_start_time: NotRequired[
        "capo_auto_scaling_plans.types.timestamp_type.TimestampType"
    ]
    """<p>The Unix time stamp when the scaling plan entered the current status.</p>"""
    creation_time: NotRequired[
        "capo_auto_scaling_plans.types.timestamp_type.TimestampType"
    ]
    """<p>The Unix time stamp when the scaling plan was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPlan) -> dict:
    out: dict = {}
    out["ScalingPlanName"] = value["scaling_plan_name"]
    out["ScalingPlanVersion"] = value["scaling_plan_version"]
    import capo_auto_scaling_plans.types.application_source

    out["ApplicationSource"] = (
        capo_auto_scaling_plans.types.application_source.serialize_aws_json_1_1(
            value["application_source"]
        )
    )
    import capo_auto_scaling_plans.types.scaling_instructions

    out["ScalingInstructions"] = (
        capo_auto_scaling_plans.types.scaling_instructions.serialize_aws_json_1_1(
            value["scaling_instructions"]
        )
    )
    import capo_auto_scaling_plans.types.scaling_plan_status_code

    out["StatusCode"] = (
        capo_auto_scaling_plans.types.scaling_plan_status_code.serialize_aws_json_1_1(
            value["status_code"]
        )
    )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "status_start_time" in value:
        import capo_auto_scaling_plans.types.timestamp_type

        out["StatusStartTime"] = (
            capo_auto_scaling_plans.types.timestamp_type.serialize_aws_json_1_1(
                value["status_start_time"]
            )
        )
    if "creation_time" in value:
        import capo_auto_scaling_plans.types.timestamp_type

        out["CreationTime"] = (
            capo_auto_scaling_plans.types.timestamp_type.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingPlan:
    out: ScalingPlan = {}  # type: ignore[typeddict-item]
    if data.get("ScalingPlanName") is not None:
        out["scaling_plan_name"] = data["ScalingPlanName"]
    else:
        out["scaling_plan_name"] = ""
    if data.get("ScalingPlanVersion") is not None:
        out["scaling_plan_version"] = data["ScalingPlanVersion"]
    else:
        out["scaling_plan_version"] = 0
    if data.get("ApplicationSource") is not None:
        import capo_auto_scaling_plans.types.application_source

        out["application_source"] = (
            capo_auto_scaling_plans.types.application_source.deserialize_aws_json_1_1(
                data["ApplicationSource"]
            )
        )
    else:
        raise DeserializationError("ScalingPlan.application_source required")
    if data.get("ScalingInstructions") is not None:
        import capo_auto_scaling_plans.types.scaling_instructions

        out["scaling_instructions"] = (
            capo_auto_scaling_plans.types.scaling_instructions.deserialize_aws_json_1_1(
                data["ScalingInstructions"]
            )
        )
    else:
        out["scaling_instructions"] = []
    if data.get("StatusCode") is not None:
        import capo_auto_scaling_plans.types.scaling_plan_status_code

        out["status_code"] = (
            capo_auto_scaling_plans.types.scaling_plan_status_code.deserialize_aws_json_1_1(
                data["StatusCode"]
            )
        )
    else:
        import typing

        out["status_code"] = typing.cast(
            "capo_auto_scaling_plans.types.scaling_plan_status_code.ScalingPlanStatusCode",
            "",
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("StatusStartTime") is not None:
        import capo_auto_scaling_plans.types.timestamp_type

        out["status_start_time"] = (
            capo_auto_scaling_plans.types.timestamp_type.deserialize_aws_json_1_1(
                data["StatusStartTime"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_auto_scaling_plans.types.timestamp_type

        out["creation_time"] = (
            capo_auto_scaling_plans.types.timestamp_type.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    return out
