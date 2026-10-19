"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunAgent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.agent_health
    import capo_inspector.types.agent_health_code
    import capo_inspector.types.agent_id
    import capo_inspector.types.arn
    import capo_inspector.types.auto_scaling_group
    import capo_inspector.types.message
    import capo_inspector.types.telemetry_metadata_list


class AssessmentRunAgent(TypedDict, closed=True):
    agent_id: "capo_inspector.types.agent_id.AgentId"
    """<p>The AWS account of the EC2 instance where the agent is installed.</p>"""
    assessment_run_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the assessment run that is associated with the agent.</p>"""
    agent_health: "capo_inspector.types.agent_health.AgentHealth"
    """<p>The current health state of the agent.</p>"""
    agent_health_code: "capo_inspector.types.agent_health_code.AgentHealthCode"
    """<p>The detailed health state of the agent.</p>"""
    agent_health_details: NotRequired["capo_inspector.types.message.Message"]
    """<p>The description for the agent health code.</p>"""
    auto_scaling_group: NotRequired[
        "capo_inspector.types.auto_scaling_group.AutoScalingGroup"
    ]
    """<p>The Auto Scaling group of the EC2 instance that is specified by the agent ID.</p>"""
    telemetry_metadata: (
        "capo_inspector.types.telemetry_metadata_list.TelemetryMetadataList"
    )
    """<p>The Amazon Inspector application data metrics that are collected by the agent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRunAgent) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["assessmentRunArn"] = value["assessment_run_arn"]
    import capo_inspector.types.agent_health

    out["agentHealth"] = capo_inspector.types.agent_health.serialize_aws_json_1_1(
        value["agent_health"]
    )
    import capo_inspector.types.agent_health_code

    out["agentHealthCode"] = (
        capo_inspector.types.agent_health_code.serialize_aws_json_1_1(
            value["agent_health_code"]
        )
    )
    if "agent_health_details" in value:
        out["agentHealthDetails"] = value["agent_health_details"]
    if "auto_scaling_group" in value:
        out["autoScalingGroup"] = value["auto_scaling_group"]
    import capo_inspector.types.telemetry_metadata_list

    out["telemetryMetadata"] = (
        capo_inspector.types.telemetry_metadata_list.serialize_aws_json_1_1(
            value["telemetry_metadata"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssessmentRunAgent:
    out: AssessmentRunAgent = {}  # type: ignore[typeddict-item]
    if data.get("agentId") is not None:
        out["agent_id"] = data["agentId"]
    else:
        out["agent_id"] = ""
    if data.get("assessmentRunArn") is not None:
        out["assessment_run_arn"] = data["assessmentRunArn"]
    else:
        out["assessment_run_arn"] = ""
    if data.get("agentHealth") is not None:
        import capo_inspector.types.agent_health

        out["agent_health"] = (
            capo_inspector.types.agent_health.deserialize_aws_json_1_1(
                data["agentHealth"]
            )
        )
    else:
        import typing

        out["agent_health"] = typing.cast(
            "capo_inspector.types.agent_health.AgentHealth", ""
        )
    if data.get("agentHealthCode") is not None:
        import capo_inspector.types.agent_health_code

        out["agent_health_code"] = (
            capo_inspector.types.agent_health_code.deserialize_aws_json_1_1(
                data["agentHealthCode"]
            )
        )
    else:
        import typing

        out["agent_health_code"] = typing.cast(
            "capo_inspector.types.agent_health_code.AgentHealthCode", ""
        )
    if data.get("agentHealthDetails") is not None:
        out["agent_health_details"] = data["agentHealthDetails"]
    if data.get("autoScalingGroup") is not None:
        out["auto_scaling_group"] = data["autoScalingGroup"]
    if data.get("telemetryMetadata") is not None:
        import capo_inspector.types.telemetry_metadata_list

        out["telemetry_metadata"] = (
            capo_inspector.types.telemetry_metadata_list.deserialize_aws_json_1_1(
                data["telemetryMetadata"]
            )
        )
    else:
        out["telemetry_metadata"] = []
    return out
