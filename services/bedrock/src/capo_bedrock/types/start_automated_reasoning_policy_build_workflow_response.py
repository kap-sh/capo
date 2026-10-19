"""Generated from Smithy shape ``com.amazonaws.bedrock#StartAutomatedReasoningPolicyBuildWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_id


class StartAutomatedReasoningPolicyBuildWorkflowResponse(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy.</p>"""
    build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId"
    """<p>The unique identifier of the newly started build workflow. Use this ID to track the workflow's progress and retrieve its results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAutomatedReasoningPolicyBuildWorkflowResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["buildWorkflowId"] = value["build_workflow_id"]
    return out


def deserialize_json(data: dict) -> StartAutomatedReasoningPolicyBuildWorkflowResponse:
    out: StartAutomatedReasoningPolicyBuildWorkflowResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        out["policy_arn"] = ""
    if data.get("buildWorkflowId") is not None:
        out["build_workflow_id"] = data["buildWorkflowId"]
    else:
        out["build_workflow_id"] = ""
    return out
