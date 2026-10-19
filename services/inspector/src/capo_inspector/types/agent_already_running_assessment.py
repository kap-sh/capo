"""Generated from Smithy shape ``com.amazonaws.inspector#AgentAlreadyRunningAssessment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.agent_id
    import capo_inspector.types.arn


class AgentAlreadyRunningAssessment(TypedDict, closed=True):
    agent_id: "capo_inspector.types.agent_id.AgentId"
    """<p>ID of the agent that is running on an EC2 instance that is already participating in another started assessment run.</p>"""
    assessment_run_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the assessment run that has already been started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentAlreadyRunningAssessment) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["assessmentRunArn"] = value["assessment_run_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AgentAlreadyRunningAssessment:
    out: AgentAlreadyRunningAssessment = {}  # type: ignore[typeddict-item]
    if data.get("agentId") is not None:
        out["agent_id"] = data["agentId"]
    else:
        out["agent_id"] = ""
    if data.get("assessmentRunArn") is not None:
        out["assessment_run_arn"] = data["assessmentRunArn"]
    else:
        out["assessment_run_arn"] = ""
    return out
